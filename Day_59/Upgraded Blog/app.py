from flask import Flask, render_template, request
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = 'wishtoinvest@gmail.com'
# password = 'technocrat$4'
password = 'xaepcteelgwppybw'
server = 'smtp.gmail.com'
port = 587

app = Flask(__name__)
response = requests.get('https://api.npoint.io/0007aaf95e0eaad8b81c')

author='Veer Rajput'

@app.route('/1')
def post1():
    title1 = response.json()[0]['title']
    subtitle1 = response.json()[0]['subtitle']
    body1 = response.json()[0]['body']
    return render_template("post.html", title=title1, subtitle=subtitle1, body=body1, author=author)

@app.route('/2')
def post2():
    title1 = response.json()[1]['title']
    subtitle1 = response.json()[1]['subtitle']
    body1 = response.json()[1]['body']
    return render_template("post.html", title=title1, subtitle=subtitle1, body=body1, author=author)

@app.route('/3')
def post3():
    title1 = response.json()[2]['title']
    subtitle1 = response.json()[2]['subtitle']
    body1 = response.json()[2]['body']
    return render_template("post.html", title=title1, subtitle=subtitle1, body=body1, author=author)

@app.route('/')
def home():
    title1 = response.json()[0]['title']
    subtitle1 = response.json()[0]['subtitle']
    title2 = response.json()[1]['title']
    subtitle2 = response.json()[1]['subtitle']
    title3 = response.json()[2]['title']
    subtitle3 = response.json()[2]['subtitle']
    return render_template('index.html', title1=title1, subtitle1=subtitle1, title2=title2, subtitle2=subtitle2, title3=title3, subtitle3=subtitle3, author='Veer Rajput', date='June 30, 2022')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    else:
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        message = request.form['message']
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = 'User comment'
        msg["From"] = my_email
        msg["To"] = "wishtoinvest@gmail.com"
        msg.attach(MIMEText(f'\nName: {name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}', 'plain'))

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
        print(name, email, phone_number, message)
        return '<h1>Successfully sent your message.</h1>'

@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form['name']
    print(name)
    return '<h1>Successfully sent your message.</h1>'


if __name__ == '__main__':
    app.run(debug=True)