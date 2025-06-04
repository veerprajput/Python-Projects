from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp
from flask_bootstrap import Bootstrap

def create_app():
    app12 = Flask(__name__)
    Bootstrap(app12)
    
    return app12

app = create_app()

class LoginForm(FlaskForm):
    username = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Regexp('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')])
    submit = SubmitField(label='Log In')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    reg_form = LoginForm(meta={'csrf': False})
    if reg_form.validate_on_submit():
        email = reg_form.username.data
        password = reg_form.password.data
        if email == 'admin@gmail.com' and password == 'Technocrat$4':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=reg_form)

if __name__ == '__main__':
    app.run(debug=True)