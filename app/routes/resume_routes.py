from flask import Blueprint, jsonify
from app.services.resume_parser import parse_resume

resume_bp = Blueprint('resume', __name__, url_prefix='/resume')

@resume_bp.route('/analyze')
def analyze():
    data = parse_resume()
    return jsonify(data)