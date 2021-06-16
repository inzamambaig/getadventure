from app import app, db
from flask import json, jsonify, request
from app.models import User, user_schema, users_schema, Group, group_schema, groups_schema
from app.models import Iteninary, iteninary_schema, iteninarys_schema, TourOperator, touroperator_schema, touroperators_schema

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})

""" 
USER
"""

# Create new user
@app.route('/users', methods=['POST'])
def new_user():
    name = request.json['name']
    address = request.json['address']
    country = request.json['country']
    date_of_birth = request.json['date_of_birth']
    email = request.json['email']
    gender = request.json['gender']
    group = request.json['group']
    phone = request.json['phone']
    zip_code = request.json['zip_code']
    
    new_user = User( name, email, phone, country, gender, group, address, date_of_birth, password, zip_code)
 
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

# Get a single user
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

# Get All Users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = users_schema.dump(users)
    return jsonify(users_list)

# Update a user
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    
    user.name = request.json['name']
    user.address = request.json['address']
    user.country = request.json['country']
    user.date_of_birth = request.json['date_of_birth']
    user.email = request.json['email']
    user.gender = request.json['gender']
    user.group = request.json['group']
    user.phone = request.json['phone']
    user.zip_code = request.json['zip_code']
    
    db.session.commit()

    return jsonify(user)

# Delete a user
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
     user = User.query.get(id)
     db.session.delete(user)
     db.session.commit()

     return user_schema.jsonify(user)

# Create new group
@app.route('/groups', methods=['POST'])
def new_group():
    name = request.json['name']
    group = Group(name)

    db.session.add(group)
    db.session.commit()
    return jsonify(group)

# get a groups list
@app.route('/groups', methods=['GET'])
def get_groups():
    groups = Group.query.all()
    group_list = groups_schema.dump(groups)
    return jsonify(group_list)

# Get a single group
@app.route('/groups/<id>', methods=['GET'])
def get_group(id):
    group = Group.query.get(id)
    return group_schema.jsonify(group)

# Update a group
@app.route('/groups/<id>', methods=['PUT'])
def update_group(id):
    group = Group.query.get(id)
    group.group_name = request.json['name']
    db.session.commit()
    return group_schema.jsonify(group)

# Delete a group
@app.route('/groups/<id>', methods=['DELETE'])
def delete_group(id):
    group = Group.query.get(id)
    db.session.delete(group)
    db.session.commit()
    return group_schema.jsonify(group)

# Create new itinerary
@app.route('/itinerary', methods=['POST'])
def new_itinerary():
    title = request.json['title']
    type = request.json['type']
    description = request.json['description']
    destination = request.json['destination']
    title = request.json['title']
    total_days = request.json['total_days']
    rating = request.json['rating']
    arrival = request.json['arrival']
    price = request.json['price']
    end_date = request.json['end_date']
    start_date = request.json['start_date']
    booked = request.json['booked']
    hero_images = request.json['hero_images']

    itinerary = Iteninary(title, type, description, destination, tour_operator_id, title, total_days, rating, arrival, price, end_date, start_date, booked, hero_images)

    db.session.add(itinerary)
    db.session.commit()
    return jsonify(itinerary)

# Get All itineraries
@app.route('/itinerary', methods=['GET'])
def get_itineraries():
    itinerary = Iteninary.query.all()
    itinerary_list = iteninarys_schema.dump(itinerary)
    return jsonify(itinerary_list)

# Get Single itinerary
@app.route('/itinerary/<id>', methods=['GET'])
def get_itinerary(id):
    itinerary = Iteninary.query.get(id)
    return iteninary_schema.jsonify(itinerary)

# Update an itenerary
@app.route('/itinerary/<id>', methods=['PUT'])
def update_itinerary(id):
    itinerary = Itinerary.query.get(id)

    itinerary.title = request.json['title']
    itinerary.type = request.json['type']
    itinerary.description = request.json['description']
    itinerary.destination = request.json['destination']
    itinerary.tour_operator_id = request.json['tour_operator_id']
    itinerary.title = request.json['title']
    itinerary.total_days = request.json['total_days']
    itinerary.rating = request.json['rating']
    itinerary.arrival = request.json['arrival']
    itinerary.price = request.json['price']
    itinerary.end_date = request.json['end_date']
    itinerary.start_date = request.json['start_date']
    itinerary.booked = request.json['booked']
    itinerary.hero_images = request.json['hero_images']

    db.session.commit()
    return jsonify(itinerary)

# Delete Itinerary
@app.route('/itinerary/<id>', methods=['DELETE'])
def delete_itinerary(id):
    iteninary = Itinerary.query.get(id)
    db.session.delete(iteninary)
    db.session.commit()

    return itinerary_schema.jsonify(itenerary)

# Create new Tour Operator
@app.route('/touroperator', methods=['POST'])
def new_touroperator():
    name = request.json['name']
    company_name = request.json['company_name']
    email = request.json['email']
    phone = request.json['phone']
    country = request.json['country']
    city = request.json['city']
    zip_code = request.json['zip_code']
    gender = request.json['gender']
    address = request.json['address']
    website = request.json['website']
    insta = request.json['insta']

    touroperator = TourOperator(name, company_name, email, phone, country, city, zip_code, gender, address, website, insta)
    db.session.add(touroperator)
    db.session.commit()
    
    return jsonify(group)
 
# get a Tour Operator list
@app.route('/touroperators', methods=['GET'])
def get_touroperators():
    touroperators = TourOperator.query.all()
    touroperator_list = groups_schema.dump(touroperators)
    return jsonify(touroperator_list)
 
# Get a single Tour Operator
@app.route('/touroperators/<id>', methods=['GET'])
def get_touroperator(id):
    touroperator = TourOperator.query.get(id)
    return touroperator_schema.jsonify(touroperator)
 
# Update a Tour Operator
@app.route('/touroperators/<id>', methods=['PUT'])
def update_touroperator(id):
    touroperator = TourOperator.query.get(id)

    name = request.json['name']
    company_name = request.json['company_name']
    email = request.json['email']
    phone = request.json['phone']
    country = request.json['country']
    city = request.json['city']
    zip_code = request.json['zip_code']
    gender = request.json['gender']
    address = request.json['address']
    website = request.json['website']
    insta = request.json['insta']

    db.session.commit()

    return touroperator_schema.jsonify(touroperator)

# Delete a Tour Operator
@app.route('/touroperators/<id>', methods=['DELETE'])
def delete_touroperator(id):
    touroperator = TourOperator.query.get(id)

    db.session.delete(touroperator)
    db.session.commit()
    
    return touroperator_schema.jsonify(touroperator)

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