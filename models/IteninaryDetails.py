from app import db, ma

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