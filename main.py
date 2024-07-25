import MetaTrader5 as mt5
from classes import Bot
from threading import Thread
import tkinter as tk


"""bot1 = Bot('EURUSD', 0.01, 10, 1)
bot2 = Bot('GBPUSD', 0.01, 10, 1)         # not needed bcz of the run_botX functions
bot3 = Bot('USDCAD', 0.01, 10, 1)"""

window = tk.Tk()
window.title('Forex Grid Bot')
window.configure(bg='#2c2f33')
window.resizable(False, False)
window.geometry('370x630')

icon = tk.PhotoImage(file= 'logo.png')
window.iconphoto(False, icon)

# bot1.run()     only this will work without threading
# bot2.run()
# bot3.run()

login_var = tk.StringVar()
password_var = tk.StringVar()
server_var = tk.StringVar()

bot1_symbol = tk.StringVar()
bot1_volume = tk.StringVar()
bot1_no_of_levels = tk.StringVar()
bot1_profit_target = tk.StringVar()

bot2_symbol = tk.StringVar()
bot2_volume = tk.StringVar()
bot2_no_of_levels = tk.StringVar()
bot2_profit_target = tk.StringVar()

bot3_symbol = tk.StringVar()
bot3_volume = tk.StringVar()
bot3_no_of_levels = tk.StringVar()
bot3_profit_target = tk.StringVar()

def initialize():
    login = int(login_var.get())
    password = password_var.get()
    server = server_var.get()

    mt5.initialize(login=login, password=password, server=server)

def run_bot1():
    symbol = bot1_symbol.get()
    volume = float(bot1_volume.get())
    no_of_levels = int(bot1_no_of_levels.get())
    profit_target = float(bot1_profit_target.get())

    bot1 = Bot(symbol, volume, no_of_levels, profit_target)
    thread = Thread(target=bot1.run)
    thread.start()

def run_bot2():
    symbol = bot2_symbol.get()
    volume = float(bot2_volume.get())
    no_of_levels = int(bot2_no_of_levels.get())
    profit_target = float(bot2_profit_target.get())

    bot2 = Bot(symbol, volume, no_of_levels, profit_target)
    thread = Thread(target=bot2.run)
    thread.start()

def run_bot3():
    symbol = bot3_symbol.get()
    volume = float(bot3_volume.get())
    no_of_levels = int(bot3_no_of_levels.get())
    profit_target = float(bot3_profit_target.get())

    bot3 = Bot(symbol, volume, no_of_levels, profit_target)
    thread = Thread(target=bot3.run)
    thread.start()

"""def b1():
    bot1.run()
def b2():
    bot2.run()

def b3():
    bot3.run()

thread1 = Thread(target=b1)
thread2 = Thread(target=b2)
thread3 = Thread(target=b3)
"""
# thread1.start()
# thread2.start()
# thread3.start()

login_label = tk.Label(window, text='Login', bg='#2c2f33', fg='white')
login_entry = tk.Entry(window, textvariable=login_var)
password_label = tk.Label(window, text='Password', bg='#2c2f33', fg='white')
password_entry = tk.Entry(window, textvariable=password_var)
server_label = tk.Label(window, text='Server', bg='#2c2f33', fg='white')
server_entry = tk.Entry(window, textvariable=server_var)
initialize_button = tk.Button(window, text='Initialize MT5', command=initialize)

# bot 1

symbol_bot1_label = tk.Label(window, text='Symbol', bg='#2c2f33', fg='white')
symbol_bot1_entry = tk.Entry(window, textvariable=bot1_symbol)
volume_bot1_label = tk.Label(window, text='Volume', bg='#2c2f33', fg='white')
volume_bot1_entry = tk.Entry(window, textvariable=bot1_volume)
no_of_levels_bot1_label = tk.Label(window, text='No.Levels', bg='#2c2f33', fg='white')
no_of_levels_bot1_entry = tk.Entry(window, textvariable=bot1_no_of_levels)
profit_target_bot1_label = tk.Label(window, text='Profit Target', bg='#2c2f33', fg='white')
profit_target_bot1_entry = tk.Entry(window, textvariable=bot1_profit_target)
bot1_run_button = tk.Button(window, text='Run Bot1', command=run_bot1)

# bot 2

symbol_bot2_label = tk.Label(window, text='Symbol', bg='#2c2f33', fg='white')
symbol_bot2_entry = tk.Entry(window, textvariable=bot2_symbol)
volume_bot2_label = tk.Label(window, text='Volume', bg='#2c2f33', fg='white')
volume_bot2_entry = tk.Entry(window, textvariable=bot2_volume)
no_of_levels_bot2_label = tk.Label(window, text='No.Levels', bg='#2c2f33', fg='white')
no_of_levels_bot2_entry = tk.Entry(window, textvariable=bot2_no_of_levels)
profit_target_bot2_label = tk.Label(window, text='Profit Target', bg='#2c2f33', fg='white')
profit_target_bot2_entry = tk.Entry(window, textvariable=bot2_profit_target)
bot2_run_button = tk.Button(window, text='Run Bot2', command=run_bot2)

# bot 3

symbol_bot3_label = tk.Label(window, text='Symbol', bg='#2c2f33', fg='white')
symbol_bot3_entry = tk.Entry(window, textvariable=bot3_symbol)
volume_bot3_label = tk.Label(window, text='Volume', bg='#2c2f33', fg='white')
volume_bot3_entry = tk.Entry(window, textvariable=bot3_volume)
no_of_levels_bot3_label = tk.Label(window, text='No.Levels', bg='#2c2f33', fg='white')
no_of_levels_bot3_entry = tk.Entry(window, textvariable=bot3_no_of_levels)
profit_target_bot3_label = tk.Label(window, text='Profit Target', bg='#2c2f33', fg='white')
profit_target_bot3_entry = tk.Entry(window, textvariable=bot3_profit_target)
bot3_run_button = tk.Button(window, text='Run Bot3', command=run_bot3)

# ----------------------------------------------------------------------------------------------------------------------

login_label.grid(row=0, column=0, padx=10, pady=10)
login_entry.grid(row=0, column=1, padx=10, pady=5)
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry.grid(row=1, column=1, padx=10, pady=5)
server_label.grid(row=2, column=0, padx=10, pady=5)
server_entry.grid(row=2, column=1, padx=10, pady=5)
initialize_button.grid(row=1, column=2, padx=10, pady=5)
seperator_1 = tk.Label(window, text='--------------------------------------------------', bg='#2c2f33', fg='white')
seperator_1.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

symbol_bot1_label.grid(row=4, column=0, padx=10, pady=5)
symbol_bot1_entry.grid(row=4, column=1, padx=10, pady=5)
volume_bot1_label.grid(row=5, column=0, padx=10, pady=5)
volume_bot1_entry.grid(row=5, column=1, padx=10, pady=5)
no_of_levels_bot1_label.grid(row=6, column=0, padx=10, pady=5)
no_of_levels_bot1_entry.grid(row=6, column=1, padx=10, pady=5)
profit_target_bot1_label.grid(row=7, column=0, padx=10, pady=5)
profit_target_bot1_entry.grid(row=7, column=1, padx=10, pady=5)
bot1_run_button.grid(row=8, column=2, padx=10, pady=5)
bot1_run_button.grid(row=7, column=2, padx=10, pady=5)
seperator_2 = tk.Label(window, text='--------------------------------------------------', bg='#2c2f33', fg='white')
seperator_2.grid(row=9, column=0, columnspan=3, padx=10, pady=5)

symbol_bot2_label.grid(row=10, column=0, padx=10, pady=5)
symbol_bot2_entry.grid(row=10, column=1, padx=10, pady=5)
volume_bot2_label.grid(row=11, column=0, padx=10, pady=5)
volume_bot2_entry.grid(row=11, column=1, padx=10, pady=5)
no_of_levels_bot2_label.grid(row=12, column=0, padx=10, pady=5)
no_of_levels_bot2_entry.grid(row=12, column=1, padx=10, pady=5)
profit_target_bot2_label.grid(row=13, column=0, padx=10, pady=5)
profit_target_bot2_entry.grid(row=13, column=1, padx=10, pady=5)
bot2_run_button.grid(row=14, column=2, padx=10, pady=5)
bot2_run_button.grid(row=13, column=2, padx=10, pady=5)
seperator_3 = tk.Label(window, text='--------------------------------------------------', bg='#2c2f33', fg='white')
seperator_3.grid(row=15, column=0, columnspan=3, padx=10, pady=5)

symbol_bot3_label.grid(row=16, column=0, padx=10, pady=5)
symbol_bot3_entry.grid(row=16, column=1, padx=10, pady=5)
volume_bot3_label.grid(row=17, column=0, padx=10, pady=5)
volume_bot3_entry.grid(row=17, column=1, padx=10, pady=5)
no_of_levels_bot3_label.grid(row=18, column=0, padx=10, pady=5)
no_of_levels_bot3_entry.grid(row=18, column=1, padx=10, pady=5)
profit_target_bot3_label.grid(row=19, column=0, padx=10, pady=5)
profit_target_bot3_entry.grid(row=19, column=1, padx=10, pady=5)
bot3_run_button.grid(row=20, column=2, padx=10, pady=5)
bot3_run_button.grid(row=19, column=2, padx=10, pady=5)

window.mainloop()