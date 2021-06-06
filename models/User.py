from enum import unique

from sqlalchemy.orm import backref
from app import db, ma
from datetime import datetime
from models import Group, Order, Passport

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