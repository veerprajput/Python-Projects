from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from pymongo import MongoClient
import hashlib
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, NumberRange
import math
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BLA'
Bootstrap(app)

client = MongoClient('mongodb://localhost:27017/')
db = client.user_cart
collection = db['users']
collection2 = db['payment']

n = 0

class AddToCartForm(FlaskForm):
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField("Add To Cart!")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In!")

class UpdateQuantityForm(FlaskForm):
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField("Update!")

class RemoveItemForm(FlaskForm):
    submit = SubmitField("Remove!")

class CheckoutForm(FlaskForm):
    submit = SubmitField("Checkout")

class ShippingForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State", validators=[DataRequired()])
    zip_code = StringField("ZIP Code", validators=[DataRequired()])
    submit = SubmitField("Apply!")

class PaymentForm(FlaskForm):
    full_name = StringField("First Name", validators=[DataRequired()])
    credit_card_number = StringField("Credit Card Number", validators=[DataRequired()])
    expiry_date = StringField("Expiry Date", validators=[DataRequired()])
    cvv_number = IntegerField("CVV", validators=[DataRequired()])
    submit = SubmitField("Place Your Order!")

items = [
    {
        'electronics':
            [
                [
                    {'item-name': 'PS5', 'item-description': 'The PlayStation 5 (PS5) is a home video game console developed by Sony Interactive Entertainment. It was announced as the successor to the PlayStation 4.', 'image-url': 'https://th.bing.com/th/id/R.91ac6b3335d3bf22fee90fa12e888d1b?rik=MUQjKkvYNVvPnQ&pid=ImgRaw&r=0', 'price': '$499.99'},
                    {'item-name': 'PS4', 'item-description': 'The PlayStation 4 (PS4) is a home video game console developed by Sony Interactive Entertainment. It was announced as the successor to the PlayStation 3.', 'image-url': 'https://th.bing.com/th/id/OIP.8DGIF0Z6x-I_8O2BQyS_qgHaHa?pid=ImgDet&rs=1', 'price': '$299.99'},
                    {'item-name': 'Nintendo Switch', 'item-description': 'The Nintendo Switch is a hybrid video game console developed by Nintendo. Its wireless Joy-Con controllers, with standard buttons and directional analog sticks for user input.', 'image-url': 'https://images2.corriereobjects.it/methode_image/2020/04/09/Tecnologia/Foto%20Tecnologia%20-%20Trattate/27263982827_9ec53ffb91_z1_ori_crop_MASTER__0x0.jpg?v=20200409162232', 'price': '$349.99'},
                ],
                [
                    {'item-name': 'Xbox Series X', 'item-description': 'The Xbox Series X is one of the fourth generation of the Xbox series of home video game consoles developed and sold by Microsoft.', 'image-url': 'https://www.deltarentals.com.au/wp-content/uploads/2020/09/Xbox-Series-X-1-1.jpg', 'price': '$499.99'},
                    {'item-name': 'Xbox Series S', 'item-description': 'The Xbox Series S is the other fourth generation of the Xbox series of home video game consoles developed and sold by Microsoft.', 'image-url': 'https://th.bing.com/th/id/R.aff2bfed051ae4a8092383e7d4108541?rik=euTNpBYb%2fVTRbg&pid=ImgRaw&r=0', 'price': '$299.99'},
                    {'item-name': 'Iphone 14', 'item-description': 'The iPhone 14 features a 6.1-inch and 6.7-inch display, improvements to the rear-facing camera, and satellite connectivity for contacting services when a user in trouble is beyond the range of Wi-Fi or cellular networks and is made by Apple.', 'image-url': 'https://m.xcite.com/media/catalog/product//i/p/iphone_14_5g_-_red_1_3.jpg', 'price': '$899.99'},
                ],
            ],
        'accessories':
            [
                [
                    {'item-name': 'AirPods Pro 2', 'item-description': 'AirPods are wireless earbuds that work with your iPhone and iPad. They use Bluetooth to connect to other devices and can play music, podcasts, and Siri', 'image-url': 'https://www.backmarket.com/cdn-cgi/image/format%3Dauto%2Cquality%3D75%2Cwidth%3D640/https://d28i4xct2kl5lp.cloudfront.net/product_images/ba5e52d9-8f1b-4adc-ac49-d5eb8a4eb47a-1_181eafb5-9396-445b-b757-adee3a9e1e5d.jpg', 'price': '$199.99'},
                    {'item-name': 'Sony Headphones', 'item-description': "These are Sony Wireless Headphones that use Bluetooth to connect to Ipad's, Iphone's and other devices. They give out great sound as well!!!", 'image-url': 'https://www.bhphotovideo.com/cdn-cgi/image/format=auto,fit=scale-down,width=500,quality=95/https://www.bhphotovideo.com/images/images500x500/sony_wh1000xm4_b_wh_1000xm4_wireless_noise_canceling_over_ear_1596715570_1582549.jpg', 'price': '$279.99'},
                ]
            ]
    }
]

logged_in_user = 'Guest'
salt='asddiopsdj'
logout_yes = 'False'

@app.route("/", methods=['GET', 'POST'])
def home():
    global logout_yes
    global logged_in_user
    if logged_in_user == 'Guest':
        logout_yes = 'True'
    return render_template('index.html', n=n, logged_in_user=logged_in_user, logout_yes=logout_yes)

@app.route("/electronics")
def electronics():
    return render_template('electronics.html', electronics=items[0]['electronics'], topic=['electronics'.title(), 'electronic products.'], n=n)

@app.route("/accessories")
def accessories():
    return render_template('electronics.html', electronics=items[0]['accessories'], topic=['accessories'.title(), 'accessories.'], n=n)

@app.route('/item_website/<itemname><topic>', methods=["GET", "POST"])
def item_website(itemname, topic):
    global n
    form = AddToCartForm()
    if form.validate_on_submit():
        itemnamea=itemname
        exact_item = None
        item_lists = items[0][itemname.split(']')[1] + 's']
        for list in item_lists:
            for item in list:
                if item['item-name'] == itemname[2:].split(',')[0][:-1]:
                    exact_item = item
        exact_item['quantity'] = form.quantity.data
        didItAlreadyExist = False
        for user in collection.find():
                if user['name'] == logged_in_user:
                    for item in user['cart']:
                        if exact_item['item-name'] == item['item-name']:
                            collection.update_one(
                                {'name': logged_in_user, 'cart.item-name': item['item-name']},
                                {'$set': {'cart.$.quantity': int(form.quantity.data) + int(item['quantity'])}}
                            )
                            didItAlreadyExist = True
                            break
        if didItAlreadyExist == False:
            collection.update_one(
                {'name': logged_in_user},
                {'$push': {'cart': exact_item}}
            )
        return redirect(url_for('fic', exact_item=exact_item))
    itemnamea=itemname
    exact_item = None
    item_lists = items[0][itemname.split(']')[1] + 's']
    for list in item_lists:
        for item in list:
            if item['item-name'] == itemname[2:].split(',')[0][:-1]:
                exact_item = item
    return render_template('item.html', items=exact_item, form=form, n=n, topic=itemnamea.split(']')[1] + 's')

@app.route('/fic/', methods=['GET', 'POST'])
@app.route('/fic/<itename>', methods=['GET', 'POST'])
def fic(itename=None):
    form = UpdateQuantityForm()
    form2 = RemoveItemForm()
    form3 = CheckoutForm()
    global n
    if form2.validate_on_submit():
        items = []
        for user in collection.find():
            if user['name'] == logged_in_user:
                n = 0
                for item in user['cart']:
                    if item['item-name'] == itename:
                        collection.update_one(
                            {'name': logged_in_user},
                            {'$pull': {'cart': {'item-name': itename}}}
                        )
                    else:
                        n += int(item['quantity'])
        for user in collection.find():
            if user['name'] == logged_in_user:
                items = user['cart']
                break
        price_total = 0
        ite = []
        for item in items:
            price_int = float(item['price'][1:])
            item['price'] = price_int
            ite.append(item)
            price_total += item['price'] * item['quantity']
        for num in range(len(items)):
            items[num]['subtotal'] = float(str('{:.2f}').format(ite[num]['price'] * ite[num]['quantity']))
        print(items)
        price_total = float(str('{:.2f}').format(price_total))
        est = float(str('{:.2f}').format(price_total * 0.0965292375))
        total = float(str('{:.2f}').format(est + price_total))
        return render_template('cart.html', items=items, n=n, logged_in_user=logged_in_user, form=form, form2=form2, form3=form3, pt=price_total, estimated_sales_tax=est, total=total)
    items = []
    for user in collection.find():
        if user['name'] == logged_in_user:
            items = user['cart']
            n = 0
            for item in user['cart']:
                n += int(item['quantity'])
    price_total = 0
    ite = []
    for item in items:
        price_int = float(item['price'][1:])
        item['price'] = price_int
        ite.append(item)
        price_total += item['price'] * item['quantity']
    for num in range(len(items)):
        items[num]['subtotal'] = float(str('{:.2f}').format(ite[num]['price'] * ite[num]['quantity']))
    print(items)
    price_total = float(str('{:.2f}').format(price_total))
    est = float(str('{:.2f}').format(price_total * 0.0965292375))
    total = float(str('{:.2f}').format(est + price_total))
    return render_template('cart.html', items=items, n=n, logged_in_user=logged_in_user, form=form, form2=form2, form3=form3, pt=price_total, estimated_sales_tax=est, total=total)

@app.route('/cart', methods=['GET', 'POST'])
@app.route('/cart/<itename>', methods=['GET', 'POST'])
def cart(itename=None):
    form = UpdateQuantityForm()
    form2 = RemoveItemForm()
    form3 = CheckoutForm()
    global n
    if form.validate_on_submit():
        items = []
        for user in collection.find():
            if user['name'] == logged_in_user:
                for item in user['cart']:
                    if item['item-name'] == itename:
                        item['quantity'] = form.quantity.data
                        collection.update_one(
                            {'name': logged_in_user, 'cart.item-name': itename},
                            {'$set': {'cart.$.quantity': int(form.quantity.data)}}
                        )
                items = user['cart']
                n = 0
                price_total = 0
                ite = []
                for item in items:
                    price_int = float(item['price'][1:])
                    item['price'] = price_int
                    ite.append(item)
                    price_total += item['price'] * item['quantity']
                for num in range(len(items)):
                    items[num]['subtotal'] = float(str('{:.2f}').format(ite[num]['price'] * ite[num]['quantity']))
                print(items)
                price_total = float(str('{:.2f}').format(price_total))
                est = float(str('{:.2f}').format(price_total * 0.0965292375))
                total = float(str('{:.2f}').format(est + price_total))
        return render_template('cart.html', items=items, n=n, logged_in_user=logged_in_user, form=form, form2=form2, form3=form3, pt=price_total, estimated_sales_tax=est, total=total)
    items = []
    for user in collection.find():
        if user['name'] == logged_in_user:
            items = user['cart']
            n = 0
            for item in user['cart']:
                n += int(item['quantity'])
    price_total = 0
    ite = []
    for item in items:
        price_int = float(item['price'][1:])
        item['price'] = price_int
        ite.append(item)
        price_total += item['price'] * item['quantity']
    for num in range(len(items)):
        items[num]['subtotal'] = float(str('{:.2f}').format(ite[num]['price'] * ite[num]['quantity']))
    price_total = float(str('{:.2f}').format(price_total))
    est = float(str('{:.2f}').format(price_total * 0.0965292375))
    total = float(str('{:.2f}').format(est + price_total))
    return render_template('cart.html', items=items, n=n, logged_in_user=logged_in_user, form=form, form2=form2, form3=form3, pt=price_total, estimated_sales_tax=est, total=total)

@app.route('/register', methods=['GET', 'POST'])
def register():
    global logged_in_user
    global logout_yes
    global n
    form = RegisterForm()
    if form.validate_on_submit():
        s = salt + form.password.data
        user = {
            'name': form.name.data,
            'email': form.email.data,
            'password': hashlib.sha256(s.encode()).hexdigest(),
            'cart': []
        }
        logged_in_user = form.name.data
        logout_yes = False
        collection.insert_one(user)
        for user in collection.find():
            if user['name'] == logged_in_user:
                n = 0
                for item in user['cart']:
                    n += int(item['quantity'])
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in_user
    global logout_yes
    global n
    form = LoginForm()
    if form.validate_on_submit():
        salt_hash = salt + form.password.data
        for user in collection.find():
            if user['email'] == form.email.data:
                if user['password'] ==  hashlib.sha256(salt_hash.encode()).hexdigest():
                    logged_in_user=user['name']
                    logout_yes = False
        for user in collection.find():
            if user['name'] == logged_in_user:
                n = 0
                for item in user['cart']:
                    n += int(item['quantity'])
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    global logged_in_user
    global n
    logged_in_user = 'Guest'
    n = 0
    return redirect(url_for('home'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    global logged_in_user
    global n
    form = ShippingForm()
    form2 = PaymentForm()
    if form.validate_on_submit():
        items = []
        for user in collection.find():
            if user['name'] == logged_in_user:
                items = user['cart']
                n = 0
                for item in user['cart']:
                    n += int(item['quantity'])
        price_total = 0
        ite = []
        for item in items:
            price_int = float(item['price'][1:])
            item['price'] = price_int
            ite.append(item)
            price_total += item['price'] * item['quantity']
        for num in range(len(items)):
            items[num]['subtotal'] = float(str('{:.2f}').format(ite[num]['price'] * ite[num]['quantity']))
        price_total = float(str('{:.2f}').format(price_total))
        est = float(str('{:.2f}').format(price_total * 0.0965292375))
        shipping = float(str('{:.2f}').format(price_total * 0.06280915872))
        total = float(str('{:.2f}').format(est + price_total))
        return render_template('checkout.html', items=items, form=form, form2=form2, pt=price_total, estimated_sales_tax=est, total=total, s=shipping)
    if form2.validate_on_submit():
        message = ''
        login_id = ''
        for payment_data in collection2.find():
            if payment_data['cardholder_name'] == form2.full_name.data:
                if payment_data['credit_card_number'] == form2.credit_card_number.data:
                    if payment_data['expiry_date'] == form2.expiry_date.data:
                        if payment_data['cvv_number'] == form2.cvv_number.data:
                            items = []
                            for user in collection.find():
                                if user['name'] == logged_in_user:
                                    items = user['cart']
                                    n = 0
                                    for item in user['cart']:
                                        n += int(item['quantity'])
                            price_total = 0
                            ite = []
                            for item in items:
                                price_int = float(item['price'][1:])
                                item['price'] = price_int
                                ite.append(item)
                                price_total += item['price'] * item['quantity']
                            for num in range(len(items)):
                                items[num]['subtotal'] = float(str('{:.2f}').format(ite[num]['price'] * ite[num]['quantity']))
                            price_total = float(str('{:.2f}').format(price_total))
                            est = float(str('{:.2f}').format(price_total * 0.0965292375))
                            shipping = float(str('{:.2f}').format(price_total * 0.06280915872))
                            total = float(str('{:.2f}').format(est + price_total + shipping))
                            if payment_data['bank_balance'] >= total:
                                collection2.update_one(
                                    {'cardholder_name': form2.full_name.data},
                                    {'$set': {'bank_balance': payment_data['bank_balance'] - total}}
                                )
                                message = 'Payment Successful!'
                            else:
                                message = 'Payment declined due to insufficient funds.'
                        else:
                            continue 
                    else:
                        continue
                else:
                    continue
            else:
                continue
        if message == 'Payment Successful!':
            for user in collection.find():
                print(user['name'])
                print(logged_in_user)
                if user['name'] == logged_in_user:
                    collection.update_one(
                        {'name': logged_in_user},
                        {'$set': {'cart': []}}
                    )
                    n = 0
                    login_id = user['email']
                    print(login_id)
            return render_template('successful.html', order_number=random.randint(10000000, 99999999), login_id=login_id)
        elif message == 'Payment declined due to insufficient funds.':
            return render_template('declined.html', message='Payment declined due to insufficient funds!')
        else:
            return render_template('declined.html', message='Payment declined due to incorrect card details!')
    items = []
    for user in collection.find():
        if user['name'] == logged_in_user:
            items = user['cart']
            n = 0
            for item in user['cart']:
                n += int(item['quantity'])
    price_total = 0
    ite = []
    for item in items:
        price_int = float(item['price'][1:])
        item['price'] = price_int
        ite.append(item)
        price_total += item['price'] * item['quantity']
    for num in range(len(items)):
        items[num]['subtotal'] = float(str('{:.2f}').format(ite[num]['price'] * ite[num]['quantity']))
    price_total = float(str('{:.2f}').format(price_total))
    est = float(str('{:.2f}').format(price_total * 0.0965292375))
    total = float(str('{:.2f}').format(est + price_total))
    return render_template('checkout.html', items=items, form=form, form2=form2, pt=price_total, estimated_sales_tax=est, total=total, s='FREE')

if __name__ == "__main__":
    app.run(debug=True)
