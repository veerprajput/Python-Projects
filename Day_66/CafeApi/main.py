from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

all_cafes = db.session.query(Cafe).all()
random_cafe = random.choice(all_cafes)

class CoffeeJson():
    def __init__(self):
        pass
    def return_random_json():
        random_cafe = random.choice(all_cafes)
        coffee_json = {
            'can_take_calls':random_cafe.can_take_calls,
            'coffee_price':random_cafe.coffee_price,
            'has_sockets':random_cafe.has_sockets,
            'has_toilet':random_cafe.has_toilet,
            'has_wifi':random_cafe.has_wifi,
            'id':random_cafe.id,
            'img_url':random_cafe.img_url,
            'location':random_cafe.location,
            'map_url':random_cafe.map_url,
            'name':random_cafe.name,
            'seats':random_cafe.seats,
        }
        
        return jsonify(
            coffee_json
        )
# Pound Symbol £
    def return_all_json():
        all_json = {'cafes': []}
        for random_cafe in all_cafes:
            coffee_json = {
                'can_take_calls':random_cafe.can_take_calls,
                'coffee_price':random_cafe.coffee_price,
                'has_sockets':random_cafe.has_sockets,
                'has_toilet':random_cafe.has_toilet,
                'has_wifi':random_cafe.has_wifi,
                'id':random_cafe.id,
                'img_url':random_cafe.img_url,
                'location':random_cafe.location,
                'map_url':random_cafe.map_url,
                'name':random_cafe.name,
                'seats':random_cafe.seats,
            }    
            all_json['cafes'].append(coffee_json)
        return jsonify(cafes=all_json['cafes'])
    def return_search_json():
        nq = request.args.get("name")
        random_cafe = db.session.query(Cafe).filter_by(name=nq).first()
        if random_cafe:
            coffee_json = {
                'can_take_calls':random_cafe.can_take_calls,
                'coffee_price':random_cafe.coffee_price,
                'has_sockets':random_cafe.has_sockets,
                'has_toilet':random_cafe.has_toilet,
                'has_wifi':random_cafe.has_wifi,
                'id':random_cafe.id,
                'img_url':random_cafe.img_url,
                'location':random_cafe.location,
                'map_url':random_cafe.map_url,
                'name':random_cafe.name,
                'seats':random_cafe.seats,
            }
            return jsonify(
                coffee_json
            )
        else:
            return jsonify(error={'Not Found': "Sorry, we don't have a cafe with that name"})

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    return CoffeeJson.return_random_json()

@app.route("/all")
def all():
    return CoffeeJson.return_all_json()

@app.route("/search")
def search():
    return CoffeeJson.return_search_json()

## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    c = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(c)
    db.session.commit()
    return jsonify({'Success': 'Successfully added your cafe'})

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update(cafe_id):
    new_price = request.args.get("new_price")
    price_update = Cafe.query.get(cafe_id)
    price_update.coffee_price = new_price
    db.session.commit()
    return jsonify(success='Successfully updated the price.')

## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "CharizardVSTAR":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    


if __name__ == '__main__':
    app.run(debug=True)
