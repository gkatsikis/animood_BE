from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.animood import Animood

animoods = Blueprint('animoods', 'animoods')

@animoods.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  animood = Animood(**data)
  db.session.add(animood)
  db.session.commit()
  return jsonify(animood.serialize()), 201

@animoods.route('/', methods=["GET"])
def index():
  animoods = Animood.query.all()
  return jsonify([animood.serialize() for animood in animoods]), 200

@animoods.route('/<id>', methods=["GET"])
def show(id):
  animood = Animood.query.filter_by(id=id).first()
  animood_data = animood.serialize()
  return jsonify(animood=animood_data), 200

@animoods.route('/<id>', methods=["PUT"])
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  animood = Animood.query.filter_by(id=id).first()

  if animood.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(animood, key, data[key])

  db.session.commit()
  return jsonify(animood.serialize()), 200

@animoods.route('/<id>', methods=["DELETE"])
@login_required
def delete(id):
  profile = read_token(request)
  animood = Animood.query.filter_by(id=id).first()

  if animood.profile_id != profile["id"]:
    return 'Forbidden', 403

  db.session.delete(animood)
  db.session.commit()
  return jsonify(message="Success"), 200