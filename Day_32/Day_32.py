import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = 'wishtoinvest@gmail.com'
# password = 'technocrat$4'
password = 'xaepcteelgwppybw'
server = 'smtp.gmail.com'
port = 587

msg = MIMEMultipart("alternative")
msg["Subject"] = 'Why,Oh why!'
msg["From"] = my_email
msg["To"] = "wishtoinvest@gmail.com"
msg.attach(MIMEText('\nsent via python', 'plain'))

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

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# print(year)

# birthday = dt.datetime(year=2012, month=9, day=4, hour=6, minute=23)
# print(birthday)




