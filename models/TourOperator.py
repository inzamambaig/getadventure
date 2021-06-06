from models.Iteninary import Iteninary
from app import db, ma

from models import Iteninary, License

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