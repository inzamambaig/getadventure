from sqlalchemy.orm import backref
from app import db, ma
from datetime import DateTime


class Passport(db.Model):
    __tablename__ = 'passport'
    id = db.Column(db.Integer, primary_key=True)
    passport_number = db.Column(db.String(100), unique=True)
    issue_date = db.Column(db.DateTime)
    expiry_date = db.Column(db.DateTime)
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

