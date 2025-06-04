from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 100)
    year = datetime.now().strftime('%Y')
    return render_template('index.html', num=random_number, date=year)

@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/0007aaf95e0eaad8b81c')
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)