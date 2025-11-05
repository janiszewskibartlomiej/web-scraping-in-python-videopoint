import os.path
import tkinter

import requests
import re
from bs4 import BeautifulSoup
from tabulate import tabulate
from pprint import pprint
from tkinter import Tk, ttk

from webscraping2 import extract_and_print_currencies

def repair_title(title: str):
    return re.sub(r"[| !?><]", "", title)

# response = requests.get("https://internetowykantor.pl/kursy-walut")
response = requests.get("https://www.kantor.pl/kursy-walut")
response.encoding = "UTF-8"

if response.status_code == 200:
    html_content = response.text
    # print(html_content)

    page = BeautifulSoup(html_content, "html.parser")

    if page.title:
        title = page.title.string.strip()
        print("Title: ",title)
    else:
        title = "No title"
        print(title)

    filename = f"pages/{repair_title(title=title)}.html"

    directory = "pages"

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file=filename, mode="w", encoding="UTF-8") as file:
        file.write(html_content)
    print("File saved")

    table = extract_and_print_currencies()
    pprint(table)

    headers_items = ["Currency", "BUY (PLN)", "SELL (PLN)", "AVG (PLN)"]
    print(tabulate(table, headers=headers_items, tablefmt="pretty"))

    gui = Tk()
    gui.title("CURRENCIES")
    gui.geometry("500x300")

    headers = tkinter.Label(gui, text="LIVE CURRENCY WEBSCRAPING", font=("Arial", 18))
    headers.pack(pady=15)

    table_frame = ttk.Frame(gui)
    table_frame.pack(pady=25)

    pad_x = 12

    ttk.Label(table_frame, text=headers_items[0], font=("Arial", 14)).grid(row=0, column=0, padx=pad_x)
    ttk.Label(table_frame, text=headers_items[1], font=("Arial", 14)).grid(row=0, column=1, padx=pad_x)
    ttk.Label(table_frame, text=headers_items[2], font=("Arial", 14)).grid(row=0, column=2, padx=pad_x)
    ttk.Label(table_frame, text=headers_items[3], font=("Arial", 14)).grid(row=0, column=3, padx=pad_x)

    ttk.Label(table_frame, text="USD", font=("Arial", 14)).grid(row=1, column=0, padx=pad_x)
    ttk.Label(table_frame, text=table[0][0], font=("Arial", 14)).grid(row=1, column=1, padx=pad_x)
    ttk.Label(table_frame, text=table[0][1], font=("Arial", 14)).grid(row=1, column=2, padx=pad_x)
    ttk.Label(table_frame, text=table[0][2], font=("Arial", 14)).grid(row=1, column=3, padx=pad_x)

    ttk.Label(table_frame, text="JPY", font=("Arial", 14)).grid(row=2, column=0, padx=pad_x)
    ttk.Label(table_frame, text=table[1][0], font=("Arial", 14)).grid(row=2, column=1, padx=pad_x)
    ttk.Label(table_frame, text=table[1][1], font=("Arial", 14)).grid(row=2, column=2, padx=pad_x)
    ttk.Label(table_frame, text=table[1][2], font=("Arial", 14)).grid(row=2, column=3, padx=pad_x)

    ttk.Label(table_frame, text="EUR", font=("Arial", 14)).grid(row=3, column=0, padx=pad_x)
    ttk.Label(table_frame, text=table[2][0], font=("Arial", 14)).grid(row=3, column=1, padx=pad_x)
    ttk.Label(table_frame, text=table[2][1], font=("Arial", 14)).grid(row=3, column=2, padx=pad_x)
    ttk.Label(table_frame, text=table[2][2], font=("Arial", 14)).grid(row=3, column=3, padx=pad_x)

    gui.mainloop()