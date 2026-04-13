from flask import Blueprint, jsonify
from app.services.roadmap_generator import generate_roadmap

roadmap_bp = Blueprint('roadmap', __name__, url_prefix='/roadmap')

@roadmap_bp.route('/')
def roadmap():
    return jsonify(generate_roadmap())