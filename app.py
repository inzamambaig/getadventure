from models import Deez
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_bcrypt import Bcrypt
# import os

# from Test import Test


# Initilization
app = Flask(__name__)




# Database
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    user = 'postgres'
    pwd = 'Getanadventure'
    port = 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{pwd}@localhost:{port}/getadventure'.format(user=user, pwd=pwd, port=port)
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Init DB
db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)



@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})

# Create SINGLE data
@app.route("/check", methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']


    new_product = Deez.Check(name, description, price)

    db.session.add(new_product)
    db.session.commit()

    return Deez.check_schema.jsonify(new_product)

# Get All
@app.route('/check', methods=['GET'])
def get_product():
    all_products = Deez.Check.query.all()
    result = Deez.checks_schema.dump(all_products)

    return jsonify(result)

# Get a Single Item
@app.route('/check/<id>', methods=['GET'])
def get_single_product(id):
    single_product = Deez.Check.query.get(id)

    return Deez.check_schema.jsonify(single_product)

# Update Product
@app.route("/check/<id>", methods=['PUT'])
def update_product(id):
    from Deez import db
    product = Deez.Check.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']

    product.name = name
    product.description = description
    product.price = price

    db.session.commit()


    return Deez.check_schema.jsonify(product)


# Delete a Single Item
@app.route('/check/<id>', methods=['DELETE'])
def delete_single_product(id):
    from Deez import db
    product = Deez.Check.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return Deez.check_schema.jsonify(product)


# Run Server
if __name__ == '__main__':
    app.run()

