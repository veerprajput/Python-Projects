import requests
from flask import Flask, render_template, request
import random

app = Flask(__name__)

response = requests.get('https://hp-api.onrender.com/api/spells')
data = response.json()
# print(data)

all_spells = []
for spell in data:
    all_spells.append({'spell':spell['name'] + '\n', 'des':spell['description']})

response = requests.get('https://hp-api.onrender.com/api/characters')
data = response.json()
# print(data)

cast = []
for person in data:
    num = random.randint(1, 4)
    if person['house'] == '':
        if num == 1:
            person['house'] = 'Gryffindor'
        elif num == 2:
            person['house'] = 'Slytherin'
        elif num == 2:
            person['house'] = 'Hufflepuff'
        else:
            person['house'] = 'Ravenclaw'
    else:
        cast.append({'name':person['name'] + '\n', 'house':person['house']})
# print(all_spells)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/spell')
def spell():
    return render_template('spells.html' , spells=all_spells)

@app.route('/characters')
def characters():
    return render_template('characters.html' , cast=cast)

if __name__ == '__main__':
    app.run(debug=True)