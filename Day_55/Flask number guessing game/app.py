import flask
import random 

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:number>")
def game(number):
    randnum = random.randint(1, 9)
    if randnum == number:
        return '<h1 style="color: green">You found me!</h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif randnum < number:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
        '<iframe src="https://giphy.com/embed/7lz6nPd56aHh6" width="480" height="258" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/animal-running-7lz6nPd56aHh6"></a></p>'
    elif randnum > number:
        return '<h1 style="color: red">Too low, try again!</h1>' \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img>'


if __name__ == "__main__":
    app.run(debug=True)