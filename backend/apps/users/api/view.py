from flask import jsonify, request, Flask

from core.factory import db
from core.ext import jwt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, index=True)
    email = db.Column(db.String(100), unique=True, index=True)
    passwor = db.Column(db.String(200))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.passwor = jwt(password)