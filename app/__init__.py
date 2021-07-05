from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)

"""
# init JWT
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

@app.route("/v1/auth/login")
@jwt_required()
def protected():
    return f'{current_identity}'
"""
from app import routes
from app import models