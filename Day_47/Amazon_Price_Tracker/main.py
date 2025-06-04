from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = 'wishtoinvest@gmail.com'
# password = 'technocrat$4'
password = 'xaepcteelgwppybw'
server = 'smtp.gmail.com'
port = 587



header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

url='https://www.amazon.com/Assorted-Cards-Rares-Special-Cosplay/dp/B0B1M1KGQH/ref=sr_1_3_sspa?keywords=pokemon+cards&qid=1655156602&sprefix=poke%2Caps%2C163&sr=8-3-spons&psc=1&smid=A2FT8QUNCF8Q4X&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMzQ0Sko1T0NVNzg2JmVuY3J5cHRlZElkPUEwMjkzNDI2TzMzVFExRENLNThJJmVuY3J5cHRlZEFkSWQ9QTAxNTE4NzJaTkJJOEJQWkg0NlAmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

response = requests.get(f"{url}", headers=header)

soup = BeautifulSoup(response.text, 'lxml')
price = soup.find(name='span', class_='a-price-whole').get_text()
price2 = soup.find(name='span', class_='a-price-fraction').get_text()
name = soup.find(name='span', class_='a-size-large product-title-word-break').get_text()
print(name)

price = float(price + price2)
print(price)

if price < 36.00:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = 'Low price alert'
    msg["From"] = my_email
    msg["To"] = "wishtoinvest@gmail.com"
    msg.attach(MIMEText(f'\n\nLow price alert, {name} is now {price}.\nBuy now at this url: {url}', 'plain'))

    connection = smtplib.SMTP(server, port)
    connection.ehlo()   
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        my_email, 
        'wishtoinvest@yahoo.com',
        msg.as_string()
    )
    connection.close()