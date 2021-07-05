from app import db, ma
from enum import unique
from sqlalchemy.orm import backref
from datetime import datetime
#from app.models import User, user_schema, users_schema, TourOperator, touroperator_schema, touroperators_schema
"""
def authenticate(username, password):
    user = User.query.filter_by(name=username)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)
"""
# M User ---> M Group
groups = db.Table('groups', 
db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True), 
db.Column('group_id', db.Integer, db.ForeignKey('group.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    country = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    group = db.Column(db.Boolean, default=False, nullable=False)
    address = db.Column(db.String(300), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    # cnic = db.Column(db.Integer)
    passport = db.relationship('Passport', backref='user', uselist=False, lazy=True)
    groups = db.relationship('Group', secondary=groups, lazy='subquery',
        backref=db.backref('user', lazy=True))
    orders = db.relationship('Order', backref='user', lazy=True)
    

    def __init__(self, name, email, phone, country, gender, group, address, date_of_birth, password, zip_code):
        self.name = name
        self.email = email
        self.phone = phone
        self.country = country
        self.gender = gender
        self.group = group
        self.address = address
        self.date_of_birth = date_of_birth
        self.password = password
        self.zip_code = zip_code

# Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone', 'country', 'gender', 'group', 'address', 'date_of_birth', 'zip_code')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(255), unique=True, nullable=False)


    def __init__(self, group_name):
        self.group_name = group_name

# Schema
class GroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'group_name')

# Initiliaze Schema

group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)



class Iteninary(db.Model):
    __tablename__ = 'iteninary'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    rating = db.Column(db.Integer)
    arrival_location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_days = db.Column(db.Integer, default=start_date - end_date)
    booked = db.Column(db.Boolean)
    hero_images = db.Column(db.String(300))
    tour_operator_id = db.Column(db.Integer, db.ForeignKey('touroperator.id'),
        nullable=False)
    tour = db.relationship('Tour', backref='iteninary', lazy=True)
    iteninary_details = db.relationship('IteninaryDetails', backref='iteninary', lazy=True)


    def __init__(self, title, type, description, rating, arrival_location, price, start_date, end_date, total_days, booked, hero_images, tour_operator_id):
        self.title = title
        self.type = type
        self.description = description
        self.rating = rating
        self.arrival_location = arrival_location
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.total_days = total_days
        self.booked = booked
        self.hero_images = hero_images
        self.tour_operator_id = tour_operator_id

# Schema
class IteninarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'type', 'description', 'rating', 'arrival', 'price', 'start_date', 'end_date', 'total_days', 'booked', 'tour_operator_id')

# Initialize Schema
iteninary_schema = IteninarySchema()
iteninarys_schema = IteninarySchema(many=True)

class IteninaryDetails(db.Model):
    __tablename__ = 'iteninarydetails'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    description = db.Column(db.String(700), nullable=False)
    accomodation = db.Column(db.String(255), nullable=False)
    breakfast = db.Column(db.String(255))
    lunch = db.Column(db.String(255))
    dinner = db.Column(db.String(255))
    other_meals = db.Column(db.String(255))
    iteninary_id = db.Column(db.Integer, db.ForeignKey('iteninary.id'), nullable=False)

    def __init__(self, day, description, accomodation, breakfast, lunch, dinner, other_meals, iteninary_id):
        self.day = day
        self.description = description
        self.accomodation = accomodation
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        self.other_meals = other_meals
        self.iteninary_id = iteninary_id

# Schema
class IteninaryDetailsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'day', 'description', 'accomodation', 'breakfast', 'lunch', 'dinner', 'other_meals', 'iteninary_id')


iteninary_details = IteninaryDetailsSchema()
iteninarys_details = IteninaryDetailsSchema(many=True)

class License(db.Model):
    __tablename__ = 'license'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    license_number = db.Column(db.String(255), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    expire_date = db.Column(db.DateTime, nullable=False)
    tour_operator_id = db.Column(db.Integer, db.ForeignKey('touroperator.id'),
        nullable=False)

    def __init__(self, type, license_number, issue_date, expire_date, tour_operator_id):
        self.type = type
        self.license_number = license_number
        self.issue_date = issue_date
        self.expire_date = expire_date
        self.tour_operator_id = tour_operator_id

# Schema
class LicenseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'license_number', 'issue_date', 'expire_date', 'tour_operator_id')

# Initialize Schema
license_schema = LicenseSchema()
licenses_schema = LicenseSchema(many=True)


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tours = db.relationship('Tour', backref='order', lazy=True)



    def __init__(self, total_price, user_id):
        self.total_price = total_price
        self.user_id = user_id


# Schema
class OrderSchema(ma.Schema):
    class Meta:
        fields = ('total_price', 'user_id')


# Initiliaze Schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

class Passport(db.Model):
    __tablename__ = 'passport'
    id = db.Column(db.Integer, primary_key=True)
    passport_number = db.Column(db.String(100), unique=True)
    issue_date = db.Column(db.DateTime, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, passport_number, issue_date, expiry_date, user_id):
        self.passport_number = passport_number
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.user_id = user_id


# Schema
class PassportSchema(ma.Schema):
    class Meta:
        fields = ('id', 'passport_number', 'issue_date', 'expiry_date', 'user_id')


# Initiliaze Schema
passport_schema = PassportSchema()
passports_schema = PassportSchema(many=True)

class Tour(db.Model):
    __tablename__ = 'tour'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    iteninary_id = db.Column(db.Integer, db.ForeignKey('iteninary.id'), nullable=False)


    def __init__(self, start_date, end_date, order_id, iteninary_id):
        self.start_date = start_date
        self.end_date = end_date
        self.order_id = order_id
        self.iteninary_id = iteninary_id

class TourSchema(ma.Schema):
    class Meta:
        fields = ('tour_id', 'start_date', 'end_date', 'order_id', 'iteninary_id')


tour_schema = TourSchema()
tours_schema = TourSchema(many=True)

class TourOperator(db.Model):
    __tablename__ = 'touroperator'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(100))
    facebook = db.Column(db.String(100))
    linkedin = db.Column(db.String(100))
    twitter = db.Column(db.String(100))
    instagram = db.Column(db.String(100))
    iteninary = db.relationship('Iteninary', backref='touroperator', lazy=True)
    license = db.relationship('License', backref='touroperator', lazy=True)

    def __init__(self, name, company_name, email, phone, country, city, zip_code, gender, address, website, facebook, linkedin, twitter, instagram):
        self.name = name
        self.company_name = company_name
        self.email = email
        self.phone = phone
        self.country = country
        self.city = city
        self.zip_code = zip_code
        self.gender = gender
        self.address = address
        self.website = website
        self.facebook = facebook
        self.linkedin = linkedin
        self.twitter = twitter
        self.instagram = instagram

# Schema
class TourOperatorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'company_name', 'email', 'phone', 'country', 'city', 'zip_code', 'gender', 'address', 'website', 'facebook', 'linkedin', 'twitter', 'instagram')

touroperator_schema = TourOperatorSchema()
touroperators_schema = TourOperatorSchema(many=True)