from app import db, ma

class Group(db.Mode):
    __tablename__ = 'group'
    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(255), unique=True, nullable=False)


    def __init__(self, group_name):
        self.group_name = group_name



# Schema
class GroupSchema(ma.Schema):
    class Meta:
        fields = ('group_id', 'group_name')


# Initiliaze Schema

group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)