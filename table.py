from pprint import pprint

import requests
from tabulate import tabulate

url = "https://api.forexapi.eu/v2/live?base=PLN&counter=EUR,GBP&apikey=1CS5HCNMGY9PsLtp8Z7N2o"

response = requests.get(url=url)
content = response.json()
# pprint(content)
table_data = [(content['quotes'][w]['counter'], content['quotes'][w]['ask']) for w in ["EUR", "GBP"]]
# pprint(table_data)
print(tabulate(tabular_data=table_data, headers=["Currency", "Value"], tablefmt="pretty"))