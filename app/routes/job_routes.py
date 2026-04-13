from flask import Blueprint, jsonify
from app.services.job_recommender import recommend_jobs

job_bp = Blueprint('job', __name__, url_prefix='/jobs')

@job_bp.route('/recommend')
def jobs():
    return jsonify(recommend_jobs())