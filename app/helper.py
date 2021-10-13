from flask import jsonify
from app import app
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from werkzeug.exceptions import HTTPException
from flask_jsonschema import ValidationError

@app.errorhandler(ValidationError)
def on_validation_error(e):
    return jsonify({"status": 400, "error": str(e.message)})

@app.errorhandler(SQLAlchemyError)
def on_sql_error(e):
    status = 502
    msg = str(e)
    if('\n' in msg):
        msg = msg.split('\n')[1]
    return jsonify({"status": status, "error": msg})

@app.errorhandler(AttributeError)
def on_sql_error(e):
    status = 502
    msg = str(e)
    return jsonify({"status": status, "error": msg})

@app.errorhandler(TypeError)
def on_sql_error(e):
    status = 502
    msg = str(e)
    return jsonify({"status": status, "error": msg})

@app.errorhandler(NameError)
def on_sql_error(e):
    status = 502
    msg = str(e)
    return jsonify({"status": status, "error": msg})

@app.errorhandler(HTTPException)
def on_http_error(e):
    status = e.code
    msg = e.description
    return jsonify({"status": status, "error": msg})