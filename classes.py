import MetaTrader5 as mt5
import pandas as pd

class Bot:
    def __init__(self, symbol, volume, no_of_levels, profit_target):
        self.symbol = symbol
        self.volume = volume
        self.no_of_levels = no_of_levels
        self.profit_target = profit_target

    def buy_limit(self, symbol, volume, price):
        response = mt5.order_send({
            "action": mt5.TRADE_ACTION_PENDING,
            "symbol": symbol,
            "volume": volume,
            "type": mt5.ORDER_TYPE_BUY_LIMIT,
            "price": price,
            "deviation": 20,
            "magic": 100,
            "comment": "python market order",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        })
        print(response)

    def sell_limit(self, symbol, volume, price):
        response = mt5.order_send({
            "action": mt5.TRADE_ACTION_PENDING,
            "symbol": symbol,
            "volume": volume,
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "price": price,
            "deviation": 20,
            "magic": 100,
            "comment": "python market order",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        })
        print(response)

    """sell_limit('EURUSD', 0.01, 1.08630)
    buy_limit('EURUSD', 0.01, 1.08380)"""

    def cal_profit(self, symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        # print(df)
        profit = float(df['profit'].sum())
        return profit

    def cal_buy_profit(self, symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        # print(df)
        df = df.loc[df.type == 0]
        profit = float(df['profit'].sum())
        return profit

    def cal_sell_profit(self, symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        # print(df)
        df = df.loc[df.type == 1]
        profit = float(df['profit'].sum())
        return profit

    def cal_volume(self, symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        # print(df)
        volume = float(df['volume'].sum())
        return volume

    """profit = cal_buyprofit('EURUSD')
    volume = cal_volume('EURUSD')
    print(profit)
    print(volume)"""

    def cal_buy_margin(self, symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        df = df.loc[df.type == 0]
        sum = 0

        for i in df.index:
            volume = df.volume[i]
            open_price = df.price_open[i]
            margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, symbol, volume, open_price)
            sum += margin

        if sum == 0:
            sum = 0.0
        return float(sum)

    def cal_sell_margin(self, symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        df = df.loc[df.type == 1]
        sum = 0

        for i in df.index:
            volume = df.volume[i]
            open_price = df.price_open[i]
            margin = mt5.order_calc_margin(mt5.ORDER_TYPE_SELL, symbol, volume, open_price)
            sum += margin

        if sum == 0:
            sum = 0.0
        return float(sum)

    """margin_b = cal_buy_margin('EURUSD')
    print(margin_b)
    margin_s = cal_sell_margin('EURUSD')
    print(margin_s)"""

    def cal_buy_pct_profit(self, symbol) -> float:
        profit = self.cal_buy_profit(symbol)
        margin_b = self.cal_buy_margin(symbol)
        pct_profit = float((profit / margin_b) * 100)
        return pct_profit

    def cal_sell_pct_profit(self, symbol) -> float:
        profit = self.cal_sell_profit(symbol)
        margin_s = self.cal_sell_margin(symbol)
        pct_profit = float((profit / margin_s) * 100)
        return pct_profit

    """pct_b = cal_buy_pct_profit("EURUSD")
    pct_s = cal_sell_pct_profit("EURUSD")
    print(pct_b)
    print(pct_s)"""

    def close_position(self, position):
        tick = mt5.symbol_info_tick(position.symbol)

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "position": position.ticket,
            "symbol": position.symbol,
            "volume": position.volume,
            "type": mt5.ORDER_TYPE_BUY if position.type == 1 else mt5.ORDER_TYPE_SELL,
            "price": tick.ask if position.type == 1 else tick.bid,
            "deviation": 20,
            "magic": 100,
            "comment": "python script close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        result = mt5.order_send(request)
        return result

    def close_all(self, symbol):
        positions = mt5.positions_get(symbol=symbol)
        for i in positions:
            self.close_position(i)

    # close_all('EURUSD')

    def delete_pending(self, tickets):
        close_request = {
            "action": mt5.TRADE_ACTION_REMOVE,
            "order": tickets,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(close_request)

        if result.retcode != mt5.TRADE_RETCODE_DONE:
            result_dict = result._asdict()
            print(result_dict)
        else:
            print("Delete complete...")

    def close_all_pending(self, symbol):
        orders = mt5.orders_get(symbol=symbol)
        df = pd.DataFrame(list(orders), columns=orders[0]._asdict().keys())
        df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial',
                 'price_stoplimit'], axis=1, inplace=True)
        df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
        for ticket in df.ticket:
            self.delete_pending(ticket)

    # close_all_pending("EURUSD")

    def draw_grid(self, symbol, volume, no_of_levels):
        pct_change_sell = 1
        tick = mt5.symbol_info_tick(symbol)
        current_price_sell = tick.bid

        for i in range(no_of_levels):
            price = ((pct_change_sell / (100 * 100)) * current_price_sell) + current_price_sell
            self.sell_limit(symbol, volume, price)
            pct_change_sell += 1

        pct_change_buy = -1
        tick = mt5.symbol_info_tick(symbol)
        current_price_buy = tick.ask

        for i in range(no_of_levels):
            price = ((pct_change_buy / (100 * 100)) * current_price_buy) + current_price_buy
            self.buy_limit(symbol, volume, price)
            pct_change_buy -= 1

    def run(self):
        self.draw_grid(self.symbol, self.volume, self.no_of_levels)

        while True:
            positions = mt5.positions_get(symbol=self.symbol)
            if len(positions) > 0:
                margin_s = float(self.cal_sell_margin(self.symbol))
                margin_b = float(self.cal_buy_margin(self.symbol))

                if margin_s > 0:
                    try:
                        pct_profit_sell = float(self.cal_sell_pct_profit(self.symbol))
                        if pct_profit_sell >= self.profit_target:
                            self.close_all(self.symbol)
                    except:
                        pass

                if margin_b > 0:
                    try:
                        pct_profit_buy = float(self.cal_buy_pct_profit(self.symbol))
                        if pct_profit_buy >= self.profit_target:
                            self.close_all(self.symbol)
                    except:
                        pass

            """positions = mt5.positions_get(symbol=self.symbol)
            if len(positions) == 0:
                try:
                    self.close_all_pending(self.symbol)
                    break
                except:
                    pass"""