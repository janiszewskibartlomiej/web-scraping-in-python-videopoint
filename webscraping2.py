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
    currencies = ["USD", "JPY", "EUR" ]

    for currency in currencies:
        buy, sell = get_price(currency)
        avg = (float(buy.replace(",", ".")) + float(sell.replace(",", ".")))/ 2
        # print(f"Currency:  {currency},  buy:  {buy} PLN,  sell:  {sell} PLN,  AVG:  {round(avg, 2)} PLN")
        table.append([currency, buy, sell, avg])
    return table