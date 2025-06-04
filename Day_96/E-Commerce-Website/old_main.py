from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
# from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'BLA'
Bootstrap(app)
# db = SQLAlchemy(app)



n = 0

class AddToCartForm(FlaskForm):
    quantity = StringField('Quantity')
    submit = SubmitField("Add To Cart")

# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     item_name = db.Column(db.String(100))
#     item_description = db.Column(db.String(100))
#     image_url = db.Column(db.String(100))
#     price = db.Column(db.Float)
#     quantity = db.Column(db.Integer)

# db.create_all()

items = [
    {'electronics':
        [
            [
                {'item-name': 'PS5', 'item-description': 'The PlayStation 5 (PS5) is a home video game console developed by Sony Interactive Entertainment. It was announced as the successor to the PlayStation 4.', 'image-url': 'https://th.bing.com/th/id/R.91ac6b3335d3bf22fee90fa12e888d1b?rik=MUQjKkvYNVvPnQ&pid=ImgRaw&r=0', 'price': '$499.99'},
                {'item-name': 'PS4', 'item-description': 'The PlayStation 4 (PS4) is a home video game console developed by Sony Interactive Entertainment. It was announced as the successor to the PlayStation 3.', 'image-url': 'https://th.bing.com/th/id/OIP.8DGIF0Z6x-I_8O2BQyS_qgHaHa?pid=ImgDet&rs=1', 'price': '$299.99'},
                {'item-name': 'Nintendo OLED Switch', 'item-description': 'The Nintendo Switch is a hybrid video game console developed by Nintendo. Its wireless Joy-Con controllers, with standard buttons and directional analog sticks for user input.', 'image-url': 'https://th.bing.com/th/id/OIP.doBKh_Et7hOqy03qyGZzLwHaEK?pid=ImgDet&rs=1', 'price': '$349.99'},
            ],
            [
                {'item-name': 'Xbox Series X', 'item-description': 'The Xbox Series X is one of the fourth generation of the Xbox series of home video game consoles developed and sold by Microsoft.', 'image-url': 'https://www.deltarentals.com.au/wp-content/uploads/2020/09/Xbox-Series-X-1-1.jpg', 'price': '$499.99'},
                {'item-name': 'Xbox Series S', 'item-description': 'The Xbox Series S is the other fourth generation of the Xbox series of home video game consoles developed and sold by Microsoft.', 'image-url': 'https://th.bing.com/th/id/R.aff2bfed051ae4a8092383e7d4108541?rik=euTNpBYb%2fVTRbg&pid=ImgRaw&r=0', 'price': '$299.99'},
                {'item-name': 'Iphone 14', 'item-description': 'The iPhone 14 features a 6.1-inch and 6.7-inch display, improvements to the rear-facing camera, and satellite connectivity for contacting services when a user in trouble is beyond the range of Wi-Fi or cellular networks and is made by Apple.', 'image-url': 'https://m.xcite.com/media/catalog/product//i/p/iphone_14_5g_-_red_1_3.jpg', 'price': '$899.99'},
            ],
        ],
    }
]

@app.route("/")
def home():
    return render_template('index.html', n=n)

@app.route("/electronics")
def electronics():
    return render_template('electronics.html', electronics=items[0]['electronics'], topic='electronics', n=n)

@app.route('/item_website/<itemname>', methods=["GET", "POST"])
def item_website(itemname):
    global n
    form = AddToCartForm()
    if form.validate_on_submit():
        itemnamea=itemname[2:][:-2].split(',')
        exact_item = None
        item_lists = items[0][itemnamea[1][2:]]
        for list in item_lists:
            for item in list:
                if item['item-name'] == itemnamea[0][:-1]:
                    exact_item = item
        return redirect(url_for('cart_from_item', exact_item=exact_item))
    itemnamea=itemname[2:][:-2].split(',')
    exact_item = None
    item_lists = items[0][itemnamea[1][2:]]
    for list in item_lists:
        for item in list:
            if item['item-name'] == itemnamea[0][:-1]:
                exact_item = item
    return render_template('item.html', items=exact_item, form=form, n=n)

@app.route('/fic/', methods=['GET', 'POST'])
def cart_from_item():
    # quantity = request.args.get('quantity')
    
    # item = Cart(
    #     item_name=request.args.get('item_name'),
    #     item_description=request.args.get('item_desc'),
    #     image_url=request.args.get('img_url'),
    #     price=float(request.args.get('price')[1:]),
    #     quantity=int(quantity)
    # )
    
    # db.session.add(item)
    # db.session.commit()
    
    # print(Cart.query.all()[-1])
    # n = Cart.query.all()[-1]
    
    return render_template('cart.html', items=request.args.get('exact_item'), n=n)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    pass

if __name__ == "__main__":
    db.session.close_all()
    app.run(debug=True)