from app import app, db
from flask import Flask, json, jsonify, request, make_response, Response
from app.models import User, user_schema, users_schema, Group, group_schema, groups_schema
from app.models import Iteninary, iteninary_schema, iteninarys_schema, TourOperator, touroperator_schema, touroperators_schema
from app.models import Passport, passport_schema, passports_schema, Order, order_schema, orders_schema
from app.models import IteninaryDetails, iteninary_details, iteninarys_details, License, license_schema, licenses_schema
from app.models import Tour, tour_schema, tours_schema

#from flask_jwt import JWT, jwt_required, current_identity

#import jwt

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from datetime import datetime, timedelta
from werkzeug.security import safe_str_cmp
from functools import wraps
import datetime
from flask_bcrypt import Bcrypt

KEY = 'Getanadventure'  # constant key declaration

app.config['SECRET_KEY'] = KEY
#app = Flask(__name__)
bcrypt = Bcrypt(app)

jwt = JWTManager(app)


@app.route('/signin', methods=['POST'])
def signin():
    name = request.json['name']
    password = request.json['password']

    user = TourOperator.query.filter_by(name=name).first()

    if (bcrypt.check_password_hash(user.password, password)):
        access_token = create_access_token(identity=user.id)
        return ({
            "user": touroperator_schema.jsonify(user).get_json(), 
            "token":  access_token, 
            "status": 200,
            "message": "login successful"
            })
    else:
        return jsonify({"msg": "Bad username or password"})


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


"""
def authenticate(username, password):
    user = User.query.filter_by(name=username).first()
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({ 'user' : auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30) }, app.config['SECRET_KEY'])

        return jsonify('token', token.decode('utf-8'))

    return make_response('could not verified', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

    return jsonify({'token', token.decode('UTF-8')})


def token_required(f):
    @wraps(f)
    def decoreted(*args, **kwargs):
        token = None
        
        token = request.json.get('token')
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])                  #to check whether token is valid
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403

        return f(*args, **kwargs)
    return decoreted


jwt = JWT(app, authenticate, identity)

@app.route('/protected')
def protected():
    return '%s' % current_identity

@app.route('/login', methods=['GET'])
def login():
    username = request.json['username']
    password = request.json['password']

    user = User.query.filter_by(name=username)

    print(user.name)

    if user and password == '12345678':
        tocken = jwt.encode({'user': 'The Quick', 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, key = 'Getanadventure')

        return jsonify({'tocken' : tocken.decode('UTF-8')})
    return make_response('Could not response', 401, {'WWW-Authencate' : 'Basic realm="Login Required"'})
"""


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})


"""
USER
"""

# Sign Up


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

#    hashed = bcrypt.generate_password_hash(password, 19).decode('utf8')

    new_tour_operator = TourOperator(name, company_name, email, password, phone, country, city, zip_code, gender, address, website, facebook, linkedin, twitter, instagram)

    db.session.add(new_tour_operator)
    db.session.commit()
    return touroperator_schema.jsonify(new_tour_operator)

# Create new user


@app.route('/user', methods=['POST'])
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

    new_user = User(name, email, phone, country, gender, group,
                    address, date_of_birth, "", zip_code)

    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

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

    return user_schema.jsonify(user)

# Delete a user


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


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
    return iteninary_schema.jsonify(iteninary)

# Get Single iteninaries


@app.route('/iteninary/<id>', methods=['GET'])
def get_iteninaries(id):
    iteninary = Iteninary.query.filter_by(tour_operator_id=id).all()
    iteninary_list = iteninarys_schema.dump(iteninary)
    return jsonify(iteninary_list)

# Get All iteninaries


@app.route('/iteninary', methods=['GET'])
def get_all_iteninaries():
    iteninary = Iteninary.query.all()
    iteninary_list = iteninarys_schema.dump(iteninary)
    return jsonify(iteninary_list)

# Update an iteninary


@app.route('/iteninary/<id>', methods=['PUT'])
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
    return iteninary_schema.jsonify(iteninary)

# Delete iteninary


@app.route('/iteninary/<id>', methods=['DELETE'])
def delete_itinerary(id):
    iteninary = Iteninary.query.get(id)
    db.session.delete(iteninary)
    db.session.commit()

    return ({"id": id, "message": "deleted"})

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

    return touroperator_schema.jsonify(touroperator)

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

    return touroperator_schema.jsonify(touroperator)

# Delete a Tour Operator


@app.route('/touroperator/<id>', methods=['DELETE'])
def delete_touroperator(id):
    touroperator = TourOperator.query.get(id)

    db.session.delete(touroperator)
    db.session.commit()

    return touroperator_schema.jsonify(touroperator)

# Create a Passport


@app.route('/passport', methods=['POST'])
def new_passport():
    passport_number = request.json['passport_number']
    issue_date = request.json['issue_date']
    expiry_date = request.json['expiry_date']
    user_id = request.json['user_id']

    passport = Passport(passport_number, issue_date, expiry_date, user_id)
    db.session.add(passport)
    db.session.commit()

    return passport_schema.jsonify(passport)

# Get all passports


@app.route('/passport', methods=['GET'])
def get_passports():
    passports = Passport.query.all()
    passport_list = passports_schema.dump(passports)

    return jsonify(passport_list)

# Get a Passport


@app.route('/passport/<id>', methods=['GET'])
def get_passport(id):
    passport = Passport.query.get(id)

    return passport_schema.jsonify(passport)

# Update a Passport


@app.route('/passport/<id>', methods=['PUT'])
def update_passport(id):
    passport = Passport.query.get(id)

    passport.passport_number = request.json['passport_number']
    passport.issue_date = request.json['issue_date']
    passport.expiry_date = request.json['expiry_date']

    db.session.commit()

    return passport_schema.jsonify(passport)

# Delete a Passport


@app.route('/passport/<id>', methods=['DELETE'])
def delete_passport(id):
    passport = Passport.query.get(id)

    db.session.delete(passport)
    db.session.commit()

    return passport_schema.jsonify(passport)

# create an order


@app.route('/order', methods=['POST'])
def new_order():
    user_id = request.json['user_id']
    total_price = request.json['total_price']

    order = Order(total_price, user_id)

    db.session.add(order)
    db.session.commit()

    return order_schema.jsonify(order)

# get an order


@app.route('/order/<id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    return order_schema.jsonify(order)

# get all orders


@app.route('/order', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    order_list = orders_schema.dump(orders)

    return jsonify(order_list)

# update an order


@app.route('/order/<id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)
    order.total_price = request.json['total_price']

    db.session.commit()

    return order_schema.jsonify(order)

# Delete an order


@app.route('/order/<id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)

    db.session.delete(order)
    db.session.commit()

    return order_schema.jsonify(order)

# Create a tour


@app.route('/tour', methods=['POST'])
def new_tour():
    order_id = request.json['order_id']
    iteninary_id = request.json['iteninary_id']
    start_date = request.json['start_date']
    end_date = request.json['end_date']

    tour = Tour(start_date, end_date, order_id, iteninary_id)

    db.session.add(tour)
    db.session.commit()

    return tour_schema.jsonify(tour)

# Get all tours


@app.route('/tour', methods=['GET'])
def get_tours():
    tours = Tour.query.all()
    tour_list = tours_schema.dump(tours)

    return jsonify(tour_list)

# Get a tour


@app.route('/tour/<id>', methods=['GET'])
def get_tour(id):
    tour = Tour.query.get(id)
    return order_schema.jsonify(tour)

# Update a tour


@app.route('/tour/<id>', methods=['PUT'])
def update_tour(id):
    tour = Tour.query.get(id)

    tour.order_id = request.json['order_id']
    tour.iteninary_id = request.json['iteninary_id']
    tour.start_date = request.json['start_date']
    tour.end_date = request.json['end_date']

    return tour_schema.jsonify(tour)

# Delete a tour


@app.route('/tour/<id>', methods=['DELETE'])
def delete_tour(id):
    tour = Tour.query.get(id)

    db.session.delete(tour)
    db.session.commit()

    return tour_schema.jsonify(tour)

# Create a itenirary_detail


@app.route('/iteninary_detail', methods=['POST'])
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
def get_iteninary_datails():
    iteninarydetails = IteninaryDetails.query.all()
    iteninarydetails_list = iteninarys_details.dump(iteninarydetails)

    return jsonify(iteninarydetails_list)

# get an iteninary_detail


@app.route('/iteninary_detail/<id>', methods=['GET'])
def get_iteninary_detail(id):
    iteninarydetail = IteninaryDetails.query.get(id)

    return iteninary_details.jsonify(iteninarydetail)

# update itinerary detail


@app.route('/iteninary_detail/<id>', methods=['PUT'])
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

    return iteninary_details.jsonify(iteninarydetail)

# delete an itinerary detail


@app.route('/iteninary_detail/<id>', methods=['DELETE'])
def delete_itenirary(id):
    iteninarydetail = IteninaryDetails.query.get(id)

    db.session.delete(iteninarydetail)
    db.session.commit()

    return iteninary_details.jsonify(iteninarydetail)

# Create a license


@app.route('/license', methods=['POST'])
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

    return license_schema.jsonify(license)

# Get all licenses


@app.route('/license', methods=['GET'])
def get_licenses():
    licenses = License.query.all()
    license_list = licenses_schema.dump(licenses)

    return jsonify(license_list)

# Get a license


@app.route('/license/<id>', methods=['GET'])
def get_license(id):
    license = License.query.get(id)

    return license_schema.jsonify(license)

# Update a license


@app.route('/license/<id>', methods=['PUT'])
def update_license(id):
    license = License.query.get(id)

    license.type = request.json.get('type')
    license.license_number = request.json.get('license_number')
    license.issue_date = request.json.get('issue_date')
    license.expiry_date = request.json.get('expire_date')
    license.tour_operator_id = request.json.get('tour_operator_id')

    db.session.commit()

    return license_schema.jsonify(license)

# Delete a license


@app.route('/license/<id>', methods=['DELETE'])
def delete_license(id):
    license = License.query.get(id)

    db.session.delete(license)
    db.session.commit()

    return license_schema.jsonify(license)

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
