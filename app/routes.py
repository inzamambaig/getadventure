from app import app, db
from flask import jsonify, request
from models import User


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})



""" 
USER
"""

# Get a Single User
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return User.users_schema.jsonify(user)
    

# # Get a Single Item
# @app.route('/check/<id>', methods=['GET'])
# def get_single_product(id):
#     single_product = Deez.Check.query.get(id)

#     return Deez.check_schema.jsonify(single_product)

# # Create SINGLE data
# @app.route("/check", methods=['POST'])
# def add_product():
#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']


#     new_product = Deez.Check(name, description, price)

#     db.session.add(new_product)
#     db.session.commit()

#     return Deez.check_schema.jsonify(new_product)

# # Get All
# @app.route('/check', methods=['GET'])
# def get_product():
#     all_products = Deez.Check.query.all()
#     result = Deez.checks_schema.dump(all_products)

#     return jsonify(result)

# # Get a Single Item
# @app.route('/check/<id>', methods=['GET'])
# def get_single_product(id):
#     single_product = Deez.Check.query.get(id)

#     return Deez.check_schema.jsonify(single_product)

# # Update Product
# @app.route("/check/<id>", methods=['PUT'])
# def update_product(id):
#     product = Deez.Check.query.get(id)

#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']

#     product.name = name
#     product.description = description
#     product.price = price

#     db.session.commit()


#     return Deez.check_schema.jsonify(product)


# # Delete a Single Item
# @app.route('/check/<id>', methods=['DELETE'])
# def delete_single_product(id):
#     product = Deez.Check.query.get(id)
#     db.session.delete(product)
#     db.session.commit()

#     return Deez.check_schema.jsonify(product)


