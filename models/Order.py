from app import db, ma

class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
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