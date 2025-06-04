from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/0007aaf95e0eaad8b81c')
    title1 = response.json()[0]['title']
    subtitle1 = response.json()[0]['subtitle']
    title2 = response.json()[1]['title']
    subtitle2 = response.json()[1]['subtitle']
    title3 = response.json()[2]['title']
    subtitle3 = response.json()[2]['subtitle']
    return render_template("index.html", title1=title1, subtitle1=subtitle1, title2=title2, subtitle2=subtitle2, title3=title3, subtitle3=subtitle3)

@app.route('/post/1')
def post_1():
    response = requests.get('https://api.npoint.io/0007aaf95e0eaad8b81c')
    title1 = response.json()[0]['title']
    subtitle1 = response.json()[0]['subtitle']
    body1 = response.json()[0]['body']
    return render_template("post.html", title=title1, subtitle=subtitle1, body=body1)

@app.route('/post/2')
def post_2():
    response = requests.get('https://api.npoint.io/0007aaf95e0eaad8b81c')
    title1 = response.json()[1]['title']
    subtitle1 = response.json()[1]['subtitle']
    body1 = response.json()[1]['body']
    return render_template("post.html", title=title1, subtitle=subtitle1, body=body1)

@app.route('/post/3')
def post_3():
    response = requests.get('https://api.npoint.io/0007aaf95e0eaad8b81c')
    title1 = response.json()[1]['title']
    subtitle1 = response.json()[2]['subtitle']
    body1 = response.json()[2]['body']
    return render_template("post.html", title=title1, subtitle=subtitle1, body=body1)

if __name__ == "__main__":
    app.run(debug=True)
