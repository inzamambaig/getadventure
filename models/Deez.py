from app import db, ma


class Check(db.Model):
    __tablename__ = 'Check'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    price = db.Column(db.Integer)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


# # Schema
class CheckSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price')

# Initilize Schema
check_schema = CheckSchema()
checks_schema = CheckSchema(many=True)
