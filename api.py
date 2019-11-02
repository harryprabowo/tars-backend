#!/usr/bin/env python
import os
from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret tars backend lulz'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# extensions
db = SQLAlchemy(app)

@app.route('/api/hello')
def hello():
    all_args = request.args.to_dict()
    return jsonify(all_args)


@app.route('/api/cars/<car_id>')
def summary(car_id):
    car = Car.query.get(car_id)
    return jsonify(car.serialize())


@app.route('/api/histories/<car_id>')
def histories(car_id):
    car = Car.query.get(car_id)


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)
