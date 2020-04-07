import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.com/gp/product/B00SXTB0AY/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1'
headers = {"User-Agent": 'yourUserAgent'}

def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, features = "lxml")
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()
    convertedPrice = float(price[1:6])

    if (convertedPrice < 14.00):
        send_email()

    print(title)
    print('price: ' + price)

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email', 'password')

    subject = 'Aardvark Price Drop'
    body = 'Link for Aardvark: URL = https://www.amazon.com/gp/product/B00SXTB0AY/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1'
    content = f"Subject: {subject}\n\n{body}"
    server.sendmail(
    'fromEmail',
    'toEmail',
    content
    )
    print('Email was sent!')

    server.quit()


while(True):
    check_price()
    # run once a day
    time.sleep(86400)
