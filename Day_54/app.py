import flask

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'><em>Hello World!</em></h1>" \
        '<iframe src="https://giphy.com/embed/jP4pPl5z1lccFcGvR0" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/pokemongo-pokemon-go-rayquaza-shiny-jP4pPl5z1lccFcGvR0"></a></p><iframe src="https://giphy.com/embed/ovRSGTNrdq5va" width="480" height="422" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/lucario-pokemon-gif-mega-evolution-ovRSGTNrdq5va"></a></p><iframe src="https://giphy.com/embed/Ojr50aBQkwxsEIuY1H" width="480" height="272" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a style="padding: 50px;" href="https://giphy.com/gifs/pokemon-sun-solgaleo-lunala-Ojr50aBQkwxsEIuY1H"></a></p>'

@app.route("/bye")
def bye():
    return 'Bye!'

@app.route("/<name>")
def greet(name):
    return f'<h3><em>Hello {name}</em></h3>'

if __name__ == "__main__":
    app.run(debug=True)