#!/usr/bin/env python
import os
import random
import re

from app import app, db
from constants import questions
from models.car import Car
from models.chat import Chat
from models.dtc import DTC
from models.history import History
from flask import abort, request, jsonify, g, url_for
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


@app.route('/api/hello')
def hello():
    all_args = request.args.to_dict()
    return jsonify(all_args)


@app.route('/api/cars/<car_id>')
def summary(car_id):
    car = Car.query.get(car_id)
    return jsonify(car.serialize())


@app.route('/api/summaries/<car_id>')
def summaries(car_id):
    summary = DTC.query.first()
    return jsonify(summary.serialize())


@app.route('/api/chats', methods=['POST'])
def chat_create():
    user_msg = request.json.get('message')
    chat_user = Chat(from_user=True, message=user_msg)
    db.session.add(chat_user)

    question = user_msg.lower()
    answer = random.choice([
        'TARS kurang mengerti maksudmu. Apakah bisa diperjelas?',
        'Maaf, TARS tidak dapat memahami kalimatmu.',
    ])
    for q, a in questions.items():
        if re.match(q.lower(), question):
            answer = a

    chat_bot = Chat(from_user=False, message=answer)
    db.session.add(chat_bot)
    db.session.commit()

    return jsonify([chat_user.serialize(), chat_bot.serialize()])


@app.route('/api/chats', methods=['GET'])
def chat_list():
    chats = [x.serialize() for x in Chat.query.all()]
    return jsonify(chats)


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)
