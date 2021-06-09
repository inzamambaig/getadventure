from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config



app = Flask(__name__)
app.config.from_object(Config)



db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)

from app import routes
from app import models