import os
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
load_dotenv()
# constants
my_email = os.getenv("my_email")
password = os.getenv("password")
url = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1_sspa?crid=1DUDAT2QUPBMD&keywords=instant+pot+dual&qid=1674161703&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTzhCQTFFTU5DWFlEJmVuY3J5cHRlZElkPUEwNjM1NzMzM09FVFlYUkRIRzNQMyZlbmNyeXB0ZWRBZElkPUEwNjg1MTEzMTRBUDJSNUxDVTZIQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="


def send_email(message, email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"{email}", msg=f"Subject:Cooker Price\n\n{message}")


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ha;q=0.8"
}
response = requests.get(
    url=url, headers=header)
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "html.parser")
price = float(soup.find(class_="a-price-whole").get_text().split(".")[0])
target_price = 300.0
if price < target_price:
    send_email(
        f"The price of cooker is down check {url}", "basharu83@gmail.com")
else:
    print(f"Price still not lower than {target_price}")
