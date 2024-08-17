import requests
import smtplib
from email.message import EmailMessage
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

sender_email = "malikasimak33@gmail.com"
sender_pass = "mbvkscfwnlumqsti"
reciever_email = "masimwork43@gmail.com"


stock_price_apikey = "2PMT8YHM4BQKTPF3"
stock_price_url = f'https://www.alphavantage.co/query'
news_apikey = "6015299c82814a989cbb848cc5638f05"
news_url = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_price_apikey
}
news_parameters = {
    "apiKey": news_apikey,
    "qInTitle": COMPANY_NAME,
}

stock_response = requests.get(url=stock_price_url, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = float(data_list[0]['4. close'])
prevday_data = float(data_list[1]['4. close'])

diff = yesterday_data - prevday_data
emoji = None
if diff > 0:
    emoji = "📈"
else:
    emoji = "📉"
diff_percent = round((diff / yesterday_data) * 100)
if abs(diff_percent) >= 5:
    news_response = requests.get(url=news_url, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_pass)
        for article in news_data:
            message = f"Subject: Headline: {article['title']}\nBrief: {article['description']}"
            em = EmailMessage()
            em.set_content(message)
            em['To'] = reciever_email
            em['From'] = sender_email
            em['Subject'] = f"{COMPANY_NAME}: {emoji}{abs(diff_percent)}% Here's Why"
            connection.send_message(em)
    
    print("Emails Sent.")
    
