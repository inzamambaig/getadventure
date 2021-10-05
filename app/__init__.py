from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from flask_cors import CORS

app = Flask(__name__)
KEY = '\x8f\xe9\xf7b\xfd\x0f\xd3\xcdiJ4\x1aH\xae\xebw\xa6%r.\xca\x12jM!\xdfc\xdcf\x92h5\xec}\xb3tgcW\xbe\xd2\x82~W\x83\nBE\x9d\xfeq]\x11\xce"\xc3d9\x10\xfb1cp7'  # constant key declaration
app.config['SECRET_KEY'] = KEY
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config.from_object(Config)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)




bcrypt = Bcrypt(app)

from app import routes
from app import models