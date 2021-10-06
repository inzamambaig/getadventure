from flask import Flask, request, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jsonschema import JsonSchema, ValidationError
from flask_cors import CORS

app = Flask(__name__)
KEY = '\x8f\xe9\xf7b\xfd\x0f\xd3\xcdiJ4\x1aH\xae\xebw\xa6%r.\xca\x12jM!\xdfc\xdcf\x92h5\xec}\xb3tgcW\xbe\xd2\x82~W\x83\nBE\x9d\xfeq]\x11\xce"\xc3d9\x10\xfb1cp7'  # constant key declaration
app.config['SECRET_KEY'] = KEY
app.config['JSONSCHEMA_DIR'] = os.path.join(app.root_path, 'schemas')

bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config.from_object(Config)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)

jsonschema = JsonSchema(app)

bcrypt = Bcrypt(app)

@app.errorhandler(ValidationError)
def on_validation_error(e):
    return jsonify({"status": 400, "error": str(e.message)})

from app import routes
from app import models