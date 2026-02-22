import os
import re

import requests
from bs4 import BeautifulSoup

table = []


def get_content_from_file():
    with open("pages/Aktualnekursywalut-kursNBP-Kantor.pl.html", mode="r", encoding="UTF-8") as file:
        content = file.read()
        return BeautifulSoup(content, "html.parser")


def get_price(currency):
    page = get_content_from_file()
    buy = page.find("span", id=f"buy_{currency}").text.strip()
    sell = page.find("span", id=f"sell_{currency}").text.strip()
    return buy, sell


def extract_and_print_currencies():
    currencies = ["USD", "JPY", "EUR"]
    get_html()

    for currency in currencies:
        buy, sell = get_price(currency)
        avg = round((float(buy.replace(",", ".")) + float(sell.replace(",", "."))) / 2, 4)
        # print(f"Currency:  {currency},  buy:  {buy} PLN,  sell:  {sell} PLN,  AVG:  {round(avg, 2)} PLN")
        table.append([currency, buy, sell, avg])
    return table


def repair_title(title: str):
    return re.sub(r"[| !?><]", "", title)


def get_html():
    # response = requests.get("https://internetowykantor.pl/kursy-walut")
    response = requests.get("https://www.kantor.pl/kursy-walut")
    response.encoding = "UTF-8"
    if response.status_code == 200:
        html_content = response.text
        # print(html_content)

        page = BeautifulSoup(html_content, "html.parser")

        if page.title:
            title = page.title.string.strip()
            print("Title: ", title)
        else:
            title = "No title"
            print(title)

        filename = get_html_file_path(title=title)

        directory = "pages"

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(file=filename, mode="w", encoding="UTF-8") as file:
            file.write(html_content)
            print(f"File saved: {filename}")
        return filename
    else:
        print("CONNECTION PROBLEM")
        return None


def get_html_file_path(title):
    return f"pages/{repair_title(title=title)}.html"
