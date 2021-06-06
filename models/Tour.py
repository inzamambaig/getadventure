from app import db, ma
from datetime import datetime

from models import Iteninary
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
    