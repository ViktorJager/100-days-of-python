import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from twilio.rest import Client

load_dotenv(
    "C:/dev/py-proj/100-days-of-python/projects/day36/stock-news-extrahard-start/.env"
)

AV_API_KEY = os.getenv("AV_API_KEY")
av_endpoint = "https://www.alphavantage.co/query"

news_api_key = os.getenv("news_api_key")
news_endpoint = "https://newsapi.org/v2/everything"

twilio_account_sid = "AC7ed755ea19f6bfbb20737ffc6e2fbfc5"
twilio_auth_token = os.getenv("twilio_auth_token")
client = Client(twilio_account_sid, twilio_auth_token)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NUMBER_OF_NEWS_TO_SEND = 3


def get_dates():
    date_today = datetime.strftime(datetime.now() - timedelta(1), "%Y-%m-%d")
    date_yesterday = datetime.strftime(datetime.now() - timedelta(3), "%Y-%m-%d")
    return {"today": date_today, "yesterday": date_yesterday}


def close_price_change(close_price_yesterday, close_price_today):
    diff = (float(close_price_yesterday) / float(close_price_today)) - 1
    diff_percentage = round((diff * 100), 2)
    return diff_percentage


def major_market_move(close_price_today, close_price_yesterday):
    return (
        True
        if abs(close_price_change(close_price_today, close_price_yesterday)) >= 5
        else False
    )


def get_stock_data():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": AV_API_KEY,
    }

    response = requests.get(av_endpoint, params=stock_parameters)
    response.raise_for_status
    return response.json()


def get_top_news():
    news_parameters = {
        "q": STOCK,
        "from": date["today"],
        "sortBy": "popularity",
        "apikey": news_api_key,
    }

    response = requests.get(news_endpoint, params=news_parameters)
    response.raise_for_status
    news = response.json()

    top_news = []
    for n in range(NUMBER_OF_NEWS_TO_SEND):
        news_title = news["articles"][n]["title"]
        news_description = news["articles"][n]["description"]
        top_news.append(
            {
                "title": news_title,
                "description": news_description,
            }
        )
    return top_news


def format_news(price_change, top_news):
    formatted_news = []

    if price_change > 0:
        header = f"{STOCK}: 🔺{price_change}%"
    else:
        header = f"{STOCK}: 🔻{price_change}%"
    formatted_news.append(header)

    for article in top_news:
        formatted_news.append(f"{article['title']}\n\n{article['description']}")
    return formatted_news


def send_sms(message):
    client.messages.create(
        body=message,
        from_="+19853154701",
        to="+46709622936",
    )


def notify_user(formatted_news):
    for entry in formatted_news:
        send_sms(entry)


date = get_dates()
stock_data = get_stock_data()

# Check if todays data is "present"
if date["today"] in stock_data["Time Series (Daily)"]:
    close_price_today = stock_data["Time Series (Daily)"][date["today"]]["4. close"]
    close_price_yesterday = stock_data["Time Series (Daily)"][date["yesterday"]][
        "4. close"
    ]

if major_market_move(close_price_today, close_price_yesterday):
    price_change = close_price_change(close_price_today, close_price_yesterday)
    formatted_news = format_news(price_change, get_top_news())
    notify_user(formatted_news)
