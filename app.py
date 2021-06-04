from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# import os

# from Test import Test


# Initilization
app = Flask(__name__)


# Database
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    user = 'postgres'
    pwd = 'Getanadventure'
    port = 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{pwd}@localhost:{port}/getadventure'.format(user=user, pwd=pwd, port=port)
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Init DB
db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)



@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})

# Run Server
if __name__ == '__main__':
    app.run()

