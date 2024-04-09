import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "3QXM9CG2H68A3ZMD"
stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}



response = requests.get(STOCK_API_ENDPOINT , stock_param)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

stock_indicator = ""
if difference > 0:
    stock_indicator = "🔺"
else:
    stock_indicator = "🔻"

diff_percent = round((abs(difference)/float(yesterday_closing_price) * 100), 2)
print(diff_percent)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if diff_percent > 4:
    NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = "8048e2f380434b659ebef263565dfbd2"
    news_param = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "apiKey": NEWS_API_KEY
    }
    
    news_response = requests.get(NEWS_API_ENDPOINT, news_param)
    news_articles = news_response.json()["articles"][:3]
    # print(news_data)

    messages = [f"{STOCK}: {stock_indicator} {diff_percent}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in news_articles]

    for message in messages:
        print(message)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

