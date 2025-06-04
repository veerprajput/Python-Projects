from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, AnyOf, URL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

def create_app():
    app12 = Flask(__name__)
    Bootstrap(app12)
    
    return app12

app = create_app()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name?', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps?')
    cafe_img = StringField('Cafe Picture?')
    location = StringField('Which City?', validators=[DataRequired()])
    seats = StringField('How many people can fit?', validators=[DataRequired()])
    has_toilet = SelectMultipleField('Has Toilet?', choices=[True, False], validators=[DataRequired()])
    has_wifi = SelectMultipleField('Has Wifi?', choices=['True', 'False'], validators=[DataRequired()])
    has_sockets = SelectMultipleField('Power_socket_availability', choices=[True, False], validators=[DataRequired()])
    can_take_calls = SelectMultipleField('Can take calls', choices=['True', 'False'], validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.String, nullable=False)
    has_wifi = db.Column(db.String, nullable=False)
    has_sockets = db.Column(db.String, nullable=False)
    can_take_calls = db.Column(db.String, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

db.create_all()




# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm(meta={'csrf': False})
    if request.method == 'POST':
            c = Cafe(
                name=form.cafe.data,
                map_url=form.cafe_location.data,
                img_url=form.cafe_img.data,
                location=form.location.data,
                has_sockets=bool(form.has_sockets.data),
                has_toilet=bool(form.has_toilet.data),
                has_wifi=bool(form.has_wifi.data),
                can_take_calls=bool(form.can_take_calls.data),
                seats=form.seats.data,
                coffee_price=form.coffee_price.data,
            )
            print(c)
            db.session.add(c)
            db.session.commit()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
    #     csv_data = csv.reader(csv_file)
    #     list_of_rows = []
    #     for row in csv_data:
    #         list_of_rows.append(row)
    list_of_rows = Cafe.query.all()
    return render_template('cafes.html', cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)
