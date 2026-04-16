import os

import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
api_key_stock = os.getenv("STOCK_API_KEY")
api_key_news = os.getenv("NEWS_API_KEY")
phone = os.getenv("MY_PHONE")
t_phone = os.getenv("TWILIO_PHONE")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def sending_sms(up_down, percentage, articles):
    client = Client(account_sid, auth_token)
    message_list = [
        f"{STOCK}{up_down}{round(percentage, 2)}%\nHeadline: {article['title'][:40]}\nBrief: {article['description'][:60]}"
        for article in articles]

    for msg in message_list:

        message = client.messages.create(
            body=msg,
            from_=t_phone,
            to=phone,
        )
    print(f"Status do envio: {message.status}")


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": api_key_stock
}

news_params = {
    "q": COMPANY_NAME,
    "apiKey": api_key_news,
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()



news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()

articles = news_data["articles"][:3]

daily_date = stock_data["Time Series (Daily)"]
daily_price = [value for(key, value) in daily_date.items()]

yesterday_value = float(daily_price[0]["4. close"])
before_yesterday_value = float(daily_price[1]["4. close"])

difference = yesterday_value - before_yesterday_value
up_down = "🔺(UP)"
if difference < 0:
    up_down = "🔻(DOWN)"
percentage = (abs(difference) / yesterday_value)*100

if percentage > 2:
    sending_sms(up_down, percentage, articles)

elif percentage < 5:
    sending_sms(up_down, percentage, articles)

else:
    print(f"{round(percentage, 2)}% too small, no sms sent.")


#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

