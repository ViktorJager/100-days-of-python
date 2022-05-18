import requests
import pandas as pd

# from pyodide.http import pyfetch
# import asyncio



def create_crypto_ids_url(crypto_ids):
  url = "?ids="
  for crypto in crypto_ids:
    url = url + f"{crypto}%2C"
  return url[:-3]


coingecko_simple_price_endpoint = "https://api.coingecko.com/api/v3/simple/price"
crypto_ids = ["bitcoin","ethereum","cardano"]
vs_currency = "usd"

crypto_ids_url = create_crypto_ids_url(crypto_ids)
vs_currency_url = f"&vs_currencies={vs_currency}"
additional_data_url = "&include_24hr_change=true&include_market_cap=true"

request_url = (coingecko_simple_price_endpoint + crypto_ids_url + vs_currency_url + additional_data_url)

# response = await pyfetch(url=request_url, method="GET")
# crypto_data = await response.json()

response = requests.get(request_url)
crypto_data = response.json()
# print(crypto_data)

for crypto in crypto_data.keys():
    str = f"{crypto.title()} "
    str += "\t|\t"
    str += f"💵 {round(crypto_data[crypto]['usd'], 2)} usd"
    str += "\t|\t"
    if crypto_data[crypto]['usd_24h_change'] > 0:
        str += f"📈 {round(crypto_data[crypto]['usd_24h_change'], 2)} "
    else:
        str += f"📉 {round(crypto_data[crypto]['usd_24h_change'], 2)} "
    str += " | "
    str += f"🏦 {round(crypto_data[crypto]['usd_market_cap'] / 1000000)}m"

    print(str)



