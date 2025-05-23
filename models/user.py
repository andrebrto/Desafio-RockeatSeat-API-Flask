from database import db
from flask_login import UserMixin

#DB-USER--
class User(db.Model, UserMixin):
    # id (int), username(text), password(text)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    roles = db.Column(db.String(80), nullable=False)
    
    meals = db.relationship('Meal', backref='user', lazy=True)
    

