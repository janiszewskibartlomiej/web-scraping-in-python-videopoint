import tkinter
from pprint import pprint
from tkinter import Tk, ttk

from tabulate import tabulate

from webscraping2 import extract_and_print_currencies

pad_x = 12
font_tuple = "Arial", 14
headers_items = ["Currency", "BUY (PLN)", "SELL (PLN)", "AVG (PLN)"]

table = extract_and_print_currencies()
pprint(table)

print(tabulate(table, headers=headers_items, tablefmt="pretty"))

gui = Tk()
gui.title("CURRENCIES")
gui.geometry("500x300")

headers = tkinter.Label(gui, text="LIVE CURRENCY WEBSCRAPING", font=("Arial", 18))
headers.pack(pady=15)

table_frame = ttk.Frame(gui)
table_frame.pack(pady=25)

for i, header in enumerate(headers_items):
    ttk.Label(table_frame, text=headers_items[i], font=font_tuple).grid(row=0, column=i, padx=pad_x)
    if i != 3:
        ttk.Label(table_frame, text=table[i][0], font=font_tuple).grid(row=i + 1, column=0, padx=pad_x)
        ttk.Label(table_frame, text=table[0][i + 1], font=font_tuple).grid(row=1, column=i + 1, padx=pad_x)
        ttk.Label(table_frame, text=table[1][i + 1], font=font_tuple).grid(row=2, column=i + 1, padx=pad_x)
        ttk.Label(table_frame, text=table[2][i + 1], font=font_tuple).grid(row=3, column=i + 1, padx=pad_x)

gui.mainloop()
