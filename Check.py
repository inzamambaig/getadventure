from app import db
from app import ma


class Check(db.Model):
    __tablename__ = 'Check'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique = True)
    description = db.Column(db.String(100))
    price = db.Column(db.Integer)

def __init__(self, name, desc, price):
    self.name = name
    self.desc = desc
    self.price = price


# # Schema
# class TestSchema(ma.schema):
#     class Meta:
#         fields = ('id', 'name', 'description', 'price')

# # Initilize Schema
# test_schema = TestSchema(strict=True)
# tests_schema = TestSchema(many=True, strict=True)
