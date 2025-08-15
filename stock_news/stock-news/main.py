import requests
import datetime
from datetime import timedelta
from twilio.rest import Client


yesterday=str((datetime.datetime.now()-timedelta(1)).date())
before_yesterday=str((datetime.datetime.now()-timedelta(2)).date())
today=datetime.datetime.now().date()
last_today=(datetime.datetime.now()-timedelta(7)).date()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters={
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':'5R9QO4R9XC9RD9BF'
}
response_stock=requests.get('https://www.alphavantage.co/query',params=parameters)
response_stock.raise_for_status()
# print(response_stock.status_code)

yesterday_closing_price=float(response_stock.json()['Time Series (Daily)'][yesterday]['4. close'])
before_yesterday_closing_price=float(response_stock.json()['Time Series (Daily)'][before_yesterday]['4. close'])

percent=(yesterday_closing_price-before_yesterday_closing_price)/before_yesterday_closing_price*100
differ_percent=round(percent,2)
# print(differ_percent)
title=body=link=''
if differ_percent>2 or differ_percent<2:
    news_parameters = {
        'q': COMPANY_NAME,
        'from': today,
        'to': last_today,
        'language': 'en',
        'sortBy': 'popularity',
        'apikey': '6bfd6886fa3842b999a0ff7895a6fd3c'
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    print(news_response.status_code)
    title = news_response.json()['articles'][0]['title']
    body = news_response.json()['articles'][0]['description']
    link = news_response.json()['articles'][0]['url']
    print(title)
    print(body)
    print(link)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

account_sid='AC500e8d2172d2a5d91d5d782fe14bd90b'
auth_token='405c6adf7e1deea6370608e525c333aa'
# api_key='tsnDhJQZHDmJf2K7p6JB4WzqRq0CikXT'
# sid='SK5f31d0e810df78684913dd91fe719e4f'
client=Client(account_sid,auth_token)
up_down=''
if differ_percent>2:
    up_down='INC'
else:
    up_down='DEC'
article=f"\nSTOCK PRICE is {up_down} by {abs(differ_percent)}% Headline:{title} Brief:{body}"
message1=client.messages.create(
    # body=f'STOCK PRICE IS :{symbol,differ_percent} %\n The Reason must be:{title}\n {body}\n READ MORE AT:{link}',
    body=article,
    from_='+16403561373',
    to='+919363071055'
)
print(message1.status)

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

