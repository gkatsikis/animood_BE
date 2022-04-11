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