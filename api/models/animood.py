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
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

  def __repr__(self):
    return f"Animood('{self.id}', '{self.name}'"

  def serialize(self):
    animood = {a.name: getattr(self, a.name) for a in self.__table__.columns}
    return animood

# class Association(db.Model):
#   __tablename__= 'associations'
#   id = db.Column(db.Integer, primary_key=True)
#   profile_id = db.Column(db.Integer, db.ForeignKey('profile.id', ondelete='cascade'))
#   animood_id = db.Column(db.Integer, db.ForeignKey('animood.id', ondelete='cascade'))