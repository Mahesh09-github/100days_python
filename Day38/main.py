import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

#variables
load_dotenv()
stock = os.getenv("STOCK")
company_name = os.getenv("COMPANY_NAME")
api_key = os.getenv("API_KEY")
news_apikey = os.getenv("NEWS_APIKEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("ACCOUNT_LOGIN")
to_phone = os.getenv("MY_PHONE")

STOCK_ENDPOINT = "https://www.alphavantage.co/query1"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_parameters ={
    "function":"TIME_SERIES_DAILY",
    "symbol": stock,
    "apikey":api_key
}

response = requests.get(url=STOCK_ENDPOINT,params=stock_parameters)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key,value) in data.items()]

yerterday_data = data_list[0]
yesterday_close_price = yerterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_close_price) - float(day_before_yesterday_closing_price)
diff_percent = (difference/float(yesterday_close_price))*100

if abs(diff_percent) > 1:
    news_params = {
        "apikey": news_apikey,
        "qInTitle": company_name
    }

    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client =  Client(account_sid,auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_="+13502474949",
            to=to_phone
        )
