from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, AnyOf, URL
import csv

def create_app():
    app12 = Flask(__name__)
    Bootstrap(app12)
    
    return app12

app = create_app()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps', validators=[DataRequired(), URL()])
    opening = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing = StringField('Closing Time e.g. 6:30PM', validators=[DataRequired()])
    coffee_rating = SelectMultipleField('Coffee Rating', choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'], validators=[DataRequired()])
    wifi_strength = SelectMultipleField('Wifi Strength Rating', choices=['✘','💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[DataRequired()])
    power_socket_availability = SelectMultipleField('Power_socket_availability', choices=['✘','🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm(meta={'csrf': False})
    if request.method == 'POST':
        if form.validate_on_submit():
            cafe_name = str(form.cafe.data)
            cafe_link = str(form.cafe_location.data)
            cafe_open = str(form.opening.data)
            cafe_close = str(form.closing.data)
            cafe_coffee = str(form.coffee_rating.data[0])
            cafe_wifi = str(form.wifi_strength.data[0])
            cafe_power = str(form.power_socket_availability.data[0])
            with open('cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
                csv_file.write(f"\n{cafe_name},{cafe_link},{cafe_open},{cafe_close},{cafe_coffee},{cafe_wifi},{cafe_power}")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)
