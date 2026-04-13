from flask import Blueprint, jsonify
from app.services.interview_ai import get_questions

interview_bp = Blueprint('interview', __name__, url_prefix='/interview')

@interview_bp.route('/questions')
def questions():
    return jsonify(get_questions())