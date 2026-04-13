from flask import Blueprint, request, jsonify
from app.services.resume_parser import parse_resume

resume_bp = Blueprint('resume', __name__, url_prefix='/resume')

@resume_bp.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get("text", "")
    return jsonify(parse_resume(text))