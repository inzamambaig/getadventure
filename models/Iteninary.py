from app import db, ma
from datetime import DateTime

class Iteninary(db.Model):
    __tablename__ = 'iteninary'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    rating = db.Column(db.Integer)
    arrival_location = db.Column(db.Column(100), nullable=False)
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