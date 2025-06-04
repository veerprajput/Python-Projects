import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = 'wishtoinvest@gmail.com'
# password = 'technocrat$4'
password = 'xaepcteelgwppybw'
server = 'smtp.gmail.com'
port = 587

msg = MIMEMultipart("alternative")
msg["Subject"] = 'It will rain today!'
msg["From"] = my_email
msg["To"] = "wishtoinvest@gmail.com"
msg.attach(MIMEText('\nRemember to bring an umbrella', 'plain'))

connection = smtplib.SMTP(server, port)
connection.ehlo()
connection.starttls()
connection.login(my_email, password)

api = 'https://api.openweathermap.org/data/2.5/onecall?'
api_key = '93766e26345a95f1f9688bc413cfb2d9'

response = requests.get(f'{api}lat=38.602100&lon=-121.290901&exclude=current,minutely,daily&appid={api_key}')
# print(response.status_code)
data = response.json()
# print(data)

# print(data['hourly'][0])
# print('\n\n\n\n\n')
for i in range(12):
    eyed = data['hourly'][i]['weather'][0]['id']
    if eyed < 700:
        connection.sendmail(
        my_email, 
        'wishtoinvest@yahoo.com',
        msg.as_string()
        )
        connection.close()
        exit()
