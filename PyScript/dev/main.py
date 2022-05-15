import requests
import pandas as pd

#from pyodide.http import pyfetch
#import asyncio



def create_crypto_ids_url(crypto_ids):
    url = "?ids="
    for crypto in crypto_ids:
        url = url + f"{crypto}%2C"
    return url[:-3]


coingecko_simple_price_endpoint = "https://api.coingecko.com/api/v3/simple/price"
crypto_ids = [
    "bitcoin",
    "ethereum",
    "cardano",
]
vs_currency = "usd"

crypto_ids_url = create_crypto_ids_url(crypto_ids)
vs_currency_url = f"&vs_currencies={vs_currency}"
additional_data_url = "&include_24hr_change=true&include_market_cap=true"

request_url = (
    coingecko_simple_price_endpoint
    + crypto_ids_url
    + vs_currency_url
    + additional_data_url
)

# response = pyfetch(url=request_url, method="GET")
# crypto_data = response.json()

response = requests.get(request_url)
# print(response.text)
crypto_data = response.json()
# print(crypto_data)
# print()
# print()


# Create dataframe
df = pd.DataFrame(crypto_data)
df = df.transpose()

# Swap col index
columns_titles = ["usd", "usd_24h_change", "usd_market_cap"]
df = df.reindex(columns=columns_titles)

# Beautify data, round and sort
df["usd"] = df["usd"].map(lambda val: round(val, 2))
df["usd_24h_change"] = df["usd_24h_change"].map(lambda val: round(val, 2))
df["usd_market_cap"] = df["usd_market_cap"].map(lambda val: round(val))
df = df.sort_values(by="usd_market_cap", ascending=False)


# Set tiles before printout
columns_titles = ["USD", "24h %", "Market"]
df = df.rename(
    columns={
        "usd": "USD",
        "usd_market_cap": "Market cap",
        "usd_24h_change": "24h %",
    }
)
#print(df)

display = df.to_html()
print(display)
