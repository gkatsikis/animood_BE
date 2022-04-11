from datetime import datetime
from api.models.db import db

class Animood(db.Model):
  __tablename__= 'animoods'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  theme = db.Column(db.String(100))
  episode = db.Column(db.String(100))
  story = db.Column(db.String(250))
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  profile_id = db.Column(db.Integer, db.ForeignKey('proifles.id'))