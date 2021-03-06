from datetime import datetime
from api.models.db import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    animoods = db.relationship("Animood", backref='author', lazy=True)

    def serialize(self):
      profile = {a.name: getattr(self, a.name) for a in self.__table__.columns}
      # animoods = [animoods.serialize() for animood in self.animoods]
      # profile['animoods'] = animoods
      return profile

