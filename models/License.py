from app import db, ma
from datetime import datetime

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
