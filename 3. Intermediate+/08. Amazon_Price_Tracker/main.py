import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

target = 100

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7",
#     "Priority": "u=0, i",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
# }

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

cookies = {
    "csm-hit": "tb:TQG9EPVZSZ300BQKDN18+s-4W34MR0SXCZVRCDSVBBD|1725706547070&t:1725706547070&adb:adblk_yes",
    "i18n-prefs": "USD",
    "session-id": "132-0806064-4766417",
    "session-id-time": "2082787201l",
    "session-token": "X0nAYUS3Jy4HN0S1WcTrTzCu+HbCJvq0pFKUghqbMeZtwjitnP94fKyCjQm7DGCYSIkD9tP1yor0uUzQfycv+1I3d0gPX489pXRLcPikgF1+EjtKgbFKK0PTEgb3nqGoZHQtazPu+A9Zx+213mY8uefGspLNJmFnZ8Qg7R/Vtf/20YxWjEN6CsJoVh8cfPHlOREMRluMO1vD0PPpWlTZbDc/+t/IXjuL6ET6v3QYMfE9nKjvmq2fw+/0Cc6W4qBLtQi9Xwp55dJD/6ot8Zp1ES/TDMDwz61TzMM+6gUoZDz49UtJU0AwV9aQAxPnmhM8sqLPjhKdQoiMcupOc/MqFJoUzuH2sLVc",
    "ubid-main": "134-2225964-3874823",
}

response = requests.get(url=url, cookies=cookies, headers=header)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())

price = float(soup.find(class_="a-offscreen").getText()[1:])
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price <= target:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
        connection.sendmail(from_addr=os.environ["EMAIL_ADDRESS"], to_addrs=os.environ["EMAIL_ADDRESS"], msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))
        print("Message Sent!")
else:
    print("Price is greater than target. Message Not Sent!")
