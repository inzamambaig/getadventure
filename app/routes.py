from marshmallow.fields import Email
from app import app, db, bcrypt, jwt, cors
from flask import Flask, json, jsonify, request, make_response, Response
from app.models import User, user_schema, users_schema, Group, group_schema, groups_schema
from app.models import Iteninary, iteninary_schema, iteninarys_schema, TourOperator, touroperator_schema, touroperators_schema
from app.models import Passport, passport_schema, passports_schema, Order, order_schema, orders_schema
from app.models import IteninaryDetails, iteninary_details, iteninarys_details, License, license_schema, licenses_schema
from app.models import Tour, tour_schema, tours_schema


from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from datetime import datetime, timedelta
from werkzeug.security import safe_str_cmp
from functools import wraps


# Test Routes

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})

# Tour Operator Sign In
@app.route('/signin', methods=['POST'])
@cross_origin()
def signin():
    email = request.json['email']
    password = request.json['password']

    user = TourOperator.query.filter_by(email=email).first()
    if(not user):
        return ({
            "status": 400,
            "msg": "Username not found"
        })
    
    additional_claims = {"name" : user.name, "company_name": user.company_name, "phone": user.phone, "website": user.website, "address": user.address, "city": user.city, "zip_code": user.zip_code, "country": user.country, "email": user.email, "facebook": user.facebook, "instagram": user.instagram, "linkedin": user.linkedin, "twitter": user.twitter }
    if (bcrypt.check_password_hash(user.password, password)):
        access_token = create_access_token(identity=user.email, additional_claims=additional_claims)
        return ({
            "user": touroperator_schema.jsonify(user).get_json(), 
            "token":  access_token, 
            "status": 200,
            "message": "login successful"
            })
    else:
        return jsonify({"msg": "Bad password"})


# Tour Operator Sign Up
@app.route('/signup', methods=['POST'])
def signup():
    name = request.json['name']
    company_name = request.json['company_name']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    country = request.json['country']
    city = request.json['city']
    zip_code = request.json['zip_code']
    gender = request.json['gender']
    address = request.json['address']
    website = request.json['website']
    facebook = request.json['facebook']
    linkedin = request.json['linkedin']
    twitter = request.json['twitter']
    instagram = request.json['instagram']


    new_tour_operator = TourOperator(name, company_name, email, password, phone, country, city, zip_code, gender, address, website, facebook, linkedin, twitter, instagram)

    db.session.add(new_tour_operator)
    db.session.commit()

    return ({"Tour Operator": name, "message": "Created"})



# Create new user
@app.route('/user', methods=['POST'])
def new_user():
    name = request.json['name']
    address = request.json['address']
    country = request.json['country']
    password = request.json['password']
    date_of_birth = request.json['date_of_birth']
    email = request.json['email']
    gender = request.json['gender']
    group = request.json['group']
    phone = request.json['phone']
    zip_code = request.json['zip_code']

    new_user = User(name, email, phone, country, gender, group,
                    address, date_of_birth, password, zip_code)

    db.session.add(new_user)
    db.session.commit()

    return ({"Tour Operator": name, "message": "Created"})





"""
# Create new group
@app.route('/group', methods=['POST'])
def new_group():
    name = request.json['name']
    group = Group(name)

    db.session.add(group)
    db.session.commit()
    return jsonify(group)

# get a groups list
@app.route('/group', methods=['GET'])
def get_groups():
    groups = Group.query.all()
    group_list = groups_schema.dump(groups)
    return jsonify(group_list)

# Get a single group
@app.route('/group/<id>', methods=['GET'])
def get_group(id):
    group = Group.query.get(id)
    return group_schema.jsonify(group)

# Update a group
@app.route('/group/<id>', methods=['PUT'])
def update_group(id):
    group = Group.query.get(id)
    group.group_name = request.json['name']
    db.session.commit()
    return group_schema.jsonify(group)

# Delete a group
@app.route('/group/<id>', methods=['DELETE'])
def delete_group(id):
    group = Group.query.get(id)
    db.session.delete(group)
    db.session.commit()
    return group_schema.jsonify(group)
"""



# Create new iteninary
@app.route('/iteninary', methods=['POST'])
@jwt_required()
def new_iteninary():
    title = request.json['title']
    type = request.json['type']
    description = request.json['description']
    title = request.json['title']
    total_days = request.json['total_days']
    rating = request.json['rating']
    arrival_location = request.json['arrival_location']
    price = request.json['price']
    end_date = request.json['end_date']
    start_date = request.json['start_date']
    booked = request.json['booked']
    hero_images = request.json['hero_images']
    tour_operator_id = request.json['tour_operator_id']

    iteninary = Iteninary(title, type, description, rating, arrival_location, price,
                          start_date, end_date, total_days, booked, hero_images, tour_operator_id)

    db.session.add(iteninary)
    db.session.commit()
    return ({"Iteninary": title, "message": "Created Successfully"})

# Get Single iteninaries
@app.route('/iteninary/<id>', methods=['GET'])
@jwt_required()
def get_iteninaries(id):
    iteninary = Iteninary.query.filter_by(tour_operator_id=id).all()
    iteninary_list = iteninarys_schema.dump(iteninary)
    return jsonify(iteninary_list)

# Get All iteninaries
@app.route('/iteninary', methods=['GET'])
@jwt_required()
def get_all_iteninaries():
    iteninary = Iteninary.query.all()
    iteninary_list = iteninarys_schema.dump(iteninary)
    return jsonify(iteninary_list)

# Update an iteninary
@app.route('/iteninary/<id>', methods=['PUT'])
@jwt_required()
def update_iteninary(id):
    iteninary = Iteninary.query.get(id)

    iteninary.title = request.json['title']
    iteninary.type = request.json['type']
    iteninary.description = request.json['description']
    iteninary.tour_operator_id = request.json['tour_operator_id']
    iteninary.title = request.json['title']
    iteninary.total_days = request.json['total_days']
    iteninary.rating = request.json['rating']
    iteninary.arrival_location = request.json['arrival_location']
    iteninary.price = request.json['price']
    iteninary.end_date = request.json['end_date']
    iteninary.start_date = request.json['start_date']
    iteninary.booked = request.json['booked']
    iteninary.hero_images = request.json['hero_images']

    db.session.commit()
    return ({"Iteninary": id, "message": "Updated Successfully"})

# Delete iteninary
@app.route('/iteninary/<id>', methods=['DELETE'])
@jwt_required()
def delete_itinerary(id):
    iteninary = Iteninary.query.get(id)
    db.session.delete(iteninary)
    db.session.commit()

    return ({"Iteninary": id, "message": "Deleted Successfully"})


""" 
Admin
"""

# Get a single user
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

# Get All Users
@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = users_schema.dump(users)
    return jsonify(users_list)

# Update a user
@app.route('/user/<id>', methods=['PUT'])
@jwt_required()
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

    return ({"User": user.name, "message": "Updated"})

# Delete a user
@app.route('/user/<id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return ({"User": id, "message": "Deleted"})

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
    facebook = request.json['facebook']
    linkedin = request.json['linkedin']
    twitter = request.json['twitter']
    instagram = request.json['instagram']

    touroperator = TourOperator(name, company_name, email, phone, country, city,
                                zip_code, gender, address, website, facebook, linkedin, twitter, instagram)
    db.session.add(touroperator)
    db.session.commit()

    return ({"Tour Operator": name, "message": "Created"})

# get a Tour Operator list
@app.route('/touroperator', methods=['GET'])
def get_touroperators():
    touroperators = TourOperator.query.all()
    touroperator_list = touroperators_schema .dump(touroperators)
    return jsonify(touroperator_list)

# Get a single Tour Operator
@app.route('/touroperator/<id>', methods=['GET'])
def get_touroperator(id):
    touroperator = TourOperator.query.get(id)
    return touroperator_schema.jsonify(touroperator)

# Update a Tour Operator
@app.route('/touroperator/<id>', methods=['PUT'])
@jwt_required()
def update_touroperator(id):
    touroperator = TourOperator.query.get(id)

    touroperator.name = request.json['name']
    touroperator.company_name = request.json['company_name']
    touroperator.email = request.json['email']
    touroperator.phone = request.json['phone']
    touroperator.country = request.json['country']
    touroperator.city = request.json['city']
    touroperator.zip_code = request.json['zip_code']
    touroperator.gender = request.json['gender']
    touroperator.address = request.json['address']
    touroperator.website = request.json['website']
    touroperator.facebook = request.json['facebook']
    touroperator.linkedin = request.json['linkedin']
    touroperator.twitter = request.json['twitter']
    touroperator.instagram = request.json['instagram']

    db.session.commit()

    return ({"Tour Operator": id, "message": "Updated Successfully"})

# Delete a Tour Operator
@app.route('/touroperator/<id>', methods=['DELETE'])
@jwt_required()
def delete_touroperator(id):
    touroperator = TourOperator.query.get(id)

    db.session.delete(touroperator)
    db.session.commit()

    return ({"Tour Operator": id, "message": "Deleted Successfully"})

# Create a Passport
@app.route('/passport', methods=['POST'])
@jwt_required()
def new_passport():
    passport_number = request.json['passport_number']
    issue_date = request.json['issue_date']
    expiry_date = request.json['expiry_date']
    user_id = request.json['user_id']

    passport = Passport(passport_number, issue_date, expiry_date, user_id)
    db.session.add(passport)
    db.session.commit()

    return ({"Passport": passport_number, "message": "Created Successfully"})

# Get all passports
@app.route('/passport', methods=['GET'])
@jwt_required()
def get_passports():
    passports = Passport.query.all()
    passport_list = passports_schema.dump(passports)

    return jsonify(passport_list)

# Get a Passport
@app.route('/passport/<id>', methods=['GET'])
@jwt_required()
def get_passport(id):
    passport = Passport.query.get(id)

    return passport_schema.jsonify(passport)

# Update a Passport
@app.route('/passport/<id>', methods=['PUT'])
@jwt_required()
def update_passport(id):
    passport = Passport.query.get(id)

    passport.passport_number = request.json['passport_number']
    passport.issue_date = request.json['issue_date']
    passport.expiry_date = request.json['expiry_date']

    db.session.commit()

    return ({"Passport": id, "message": "Updated Successfully"})

# Delete a Passport
@app.route('/passport/<id>', methods=['DELETE'])
@jwt_required()
def delete_passport(id):
    passport = Passport.query.get(id)

    db.session.delete(passport)
    db.session.commit()

    return ({"Passport": id, "message": "Deleted Successfully"})

# Create an order
@app.route('/order', methods=['POST'])
@jwt_required()
def new_order():
    user_id = request.json['user_id']
    total_price = request.json['total_price']

    order = Order(total_price, user_id)

    db.session.add(order)
    db.session.commit()

    return ({"Order": user_id, "message": "Created Successfully"})

# Get an order
@app.route('/order/<id>', methods=['GET'])
@jwt_required()
def get_order(id):
    order = Order.query.get(id)
    return order_schema.jsonify(order)

# Get all orders
@app.route('/order', methods=['GET'])
@jwt_required()
def get_orders():
    orders = Order.query.all()
    order_list = orders_schema.dump(orders)

    return jsonify(order_list)

# Update an order
@app.route('/order/<id>', methods=['PUT'])
@jwt_required()
def update_order(id):
    order = Order.query.get(id)
    order.total_price = request.json['total_price']

    db.session.commit()

    return ({"Order": id, "message": "Updated Successfully"})

# Delete an order
@app.route('/order/<id>', methods=['DELETE'])
@jwt_required()
def delete_order(id):
    order = Order.query.get(id)

    db.session.delete(order)
    db.session.commit()

    return ({"Order": id, "message": "Deleted Successfully"})

# Create a tour
@app.route('/tour', methods=['POST'])
@jwt_required()
def new_tour():
    order_id = request.json['order_id']
    iteninary_id = request.json['iteninary_id']
    start_date = request.json['start_date']
    end_date = request.json['end_date']

    tour = Tour(start_date, end_date, order_id, iteninary_id)

    db.session.add(tour)
    db.session.commit()

    return ({"Passport": order_id, "message": "Created Successfully"})

# Get all tours
@app.route('/tour', methods=['GET'])
@jwt_required()
def get_tours():
    tours = Tour.query.all()
    tour_list = tours_schema.dump(tours)

    return jsonify(tour_list)

# Get a tour
@app.route('/tour/<id>', methods=['GET'])
@jwt_required()
def get_tour(id):
    tour = Tour.query.get(id)
    return order_schema.jsonify(tour)

# Update a tour
@app.route('/tour/<id>', methods=['PUT'])
@jwt_required()
def update_tour(id):
    tour = Tour.query.get(id)

    tour.order_id = request.json['order_id']
    tour.iteninary_id = request.json['iteninary_id']
    tour.start_date = request.json['start_date']
    tour.end_date = request.json['end_date']

    return ({"Tour": id, "message": "Updated Successfully"})

# Delete a tour
@app.route('/tour/<id>', methods=['DELETE'])
@jwt_required()
def delete_tour(id):
    tour = Tour.query.get(id)

    db.session.delete(tour)
    db.session.commit()

    return ({"Order": id, "message": "Deleted Successfully"})

# Create a itenirary_detail
@app.route('/iteninary_detail', methods=['POST'])
@jwt_required()
def new_itinerary_detail():
    iteninary_id = request.json.get('iteninary_id')
    day = request.json.get('day')
    description = request.json.get('description')
    accomodation = request.json.get('accomodation')
    breakfast = request.json.get('breakfast')
    lunch = request.json.get('lunch')
    dinner = request.json.get('dinner')
    other_meals = request.json.get('other_meals')

    iteninarydetail = IteninaryDetails(
        day, description, accomodation, breakfast, lunch, dinner, other_meals, iteninary_id)

    db.session.add(iteninarydetail)
    db.session.commit()

    # return iteninary_details.jsonify(iteninarydetail)

    return ({
        "status": 200,
        "message": "Details Added Succesfully"
    })

# get all iteninary_delails
@app.route('/iteninary_details', methods=['GET'])
@jwt_required()
def get_iteninary_datails():
    iteninarydetails = IteninaryDetails.query.all()
    iteninarydetails_list = iteninarys_details.dump(iteninarydetails)

    return jsonify(iteninarydetails_list)



# get an iteninary_detail
@app.route('/iteninary_detail/<id>', methods=['GET'])
@jwt_required()
def get_iteninary_detail(id):
    iteninarydetail = IteninaryDetails.query.filter_by(iteninary_id=id)
    iteninarydetails = iteninarys_details.dump(iteninarydetail)
    return jsonify(iteninarydetails)

    

# update itinerary detail
@app.route('/iteninary_detail/<id>', methods=['PUT'])
@jwt_required()
def update_itenirary_detail(id):
    iteninarydetail = IteninaryDetails.query.get(id)

    iteninarydetail.iteninary_id = request.json.get('iteninary_id')
    iteninarydetail.day = request.json.get('day')
    iteninarydetail.description = request.json.get('description')
    iteninarydetail.accomodation = request.json.get('accomodation')
    iteninarydetail.breakfast = request.json.get('breakfast')
    iteninarydetail.lunch = request.json.get('lunch')
    iteninarydetail.dinner = request.json.get('dinner')
    iteninarydetail.other_meals = request.json.get('other_meals')

    db.session.commit()

    return ({"Iteninary Details": id, "message": "Updated Successfully"})


# delete an itinerary detail
@app.route('/iteninary_detail/<id>', methods=['DELETE'])
@jwt_required()
def delete_itenirary(id):
    iteninarydetail = IteninaryDetails.query.get(iteninary_id=id)

    db.session.delete(iteninarydetail)
    db.session.commit()

    return ({"Iteninary Details": id, "message": "Deleted Successfully"})

# Create a license
@app.route('/license', methods=['POST'])
@jwt_required()
def new_license():
    type = request.json.get('type')
    license_number = request.json.get('license_number')
    issue_date = request.json.get('issue_date')
    expiry_date = request.json.get('expire_date')
    tour_operator_id = request.json.get('tour_operator_id')

    license = License(type, license_number, issue_date,
                      expiry_date, tour_operator_id)

    db.session.add(license)
    db.session.commit()

    return ({"License": license_number, "message": "Created Successfully"})


# Get all licenses
@app.route('/license', methods=['GET'])
@jwt_required()
def get_licenses():
    licenses = License.query.all()
    license_list = licenses_schema.dump(licenses)

    return jsonify(license_list)


# Get a license
@app.route('/license/<id>', methods=['GET'])
@jwt_required()
def get_license(id):
    print(id)
    license = License.query.filter_by(tour_operator_id=id)
    licenses = licenses_schema.dump(license)

    return jsonify(licenses)


# Update a license
@app.route('/license/<id>', methods=['PUT'])
@jwt_required()
def update_license(id):
    license = License.query.get(id)

    license.type = request.json.get('type')
    license.license_number = request.json.get('license_number')
    license.issue_date = request.json.get('issue_date')
    license.expiry_date = request.json.get('expire_date')
    license.tour_operator_id = request.json.get('tour_operator_id')

    db.session.commit()

    return ({"License": id, "message": "Updated Successfully"})

# Delete a license
@app.route('/license/<id>', methods=['DELETE'])
@jwt_required()
def delete_license(id):
    license = License.query.get(id)

    db.session.delete(license)
    db.session.commit()

    return ({"License": id, "message": "Deleted Successfully"})
