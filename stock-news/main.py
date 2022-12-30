import requests
from datetime import *
from newsapi import NewsApiClient
import html
# constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "NEJ72R0QYJ188QGF"
NEWS_API_KEY = "1a6dfff7e91b4cb39accfe01bb159aea"
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY
}


# Get data of yesterday and day before yesterday
today = datetime.today()
yesterday_date = today - timedelta(days=1)
yesterday = str(yesterday_date).split()[0]
day_before_yesterday_date = today - timedelta(days=2)
day_before_yesterday = str(day_before_yesterday_date).split()[0]


def get_news():
    # Init
    newsapi = NewsApiClient(api_key="1a6dfff7e91b4cb39accfe01bb159aea")

    # # /v2/top-headlines
    # top_headlines = newsapi.get_top_headlines(q='bitcoin',
    #                                           sources='bbc-news,the-verge',
    #                                           category='business',
    #                                           language='en',
    #                                           country='us')

    # /v2/everything
    all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                          #   sources='bbc-news,the-verge',
                                          #   domains='bbc.co.uk,techcrunch.com',
                                          from_param=day_before_yesterday,
                                          to=yesterday,
                                          language='en',
                                          sort_by='relevancy',
                                          )

    # /v2/top-headlines/sources
    # sources = newsapi.get_sources()
    return all_articles['articles'][:3]


def send_sms(source, title, description):
    sms_username = "your username"
    sms_password = "your password"
    sms_url = "https://portal.nigeriabulksms.com/api/"
    mobile = "your mobile"
    message = f"""{source}
    Headline: {title} 
    Brief: {description}"""
    sms_parameters = {
        "username": sms_username,
        "password": sms_password,
        "sender": "Bashar",
        "message": html.unescape(message),
        "mobiles": mobile
    }
    sms_response = requests.get(url=sms_url, params=sms_parameters)
    sms_response.raise_for_status()
    sms_data = sms_response.json()
    status = sms_data['status']
    if status == 'OK':
        print("Success")
    # STEP 1: Use https://newsapi.org/docs/endpoints/everything
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    # HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
    # HINT 2: Work out the value of 5% of yerstday's closing stock price.


# Fetch the closing prices of yesterday and day before yesterday
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()['Time Series (Daily)']
yesterday_price = float(data[yesterday]['4. close'])
day_before_yesterday_price = float(data[day_before_yesterday]['4. close'])

# Calculate the percentage increase
percentage_increase = abs(
    yesterday_price - day_before_yesterday_price) / day_before_yesterday_price * 100
# check if the percentage increase is greater than 5%

# yesterdays_percentage = 5/100 * yesterday_price
# print(int(yesterdays_percentage))


# percentage_increase = price_difference / (yesterday_price * 100)
# print(int(percentage_increase))


# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator
if percentage_increase > 5:
    all_articles = get_news()
    number_of_articles = len(all_articles)
    for article in range(number_of_articles):
        source = all_articles[article]['source']['name']
        title = all_articles[article]['title']
        description = all_articles[article]['description']
        send_sms(source, title, description)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
