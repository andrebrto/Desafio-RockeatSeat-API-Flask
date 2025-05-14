from database import db
from datetime import datetime

#DB-MEAL--
class Meal(db.Model):
  # id (int), name (text), description (text), date (Date), time (time), is_in_diet (boolean), user_id (ForeignKey)
  id = db.Column(db.Integer, unique=True, primary_key=True)
  name = db.Column(db.String(32), nullable=False)
  description = db.Column(db.String(80), nullable=False)
  datetime = db.Column(db.DateTime, nullable=False, default=datetime.now)
  is_in_diet = db.Column(db.Boolean, default=False, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)