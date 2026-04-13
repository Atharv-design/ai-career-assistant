from flask import Blueprint, render_template, request
from app.services.job_recommender import recommend_jobs

job_bp = Blueprint("job", __name__)

@job_bp.route("/jobs", methods=["GET", "POST"])
def jobs():
    jobs = []

    if request.method == "POST":
        skills = request.form.get("skills")
        jobs = recommend_jobs(skills.split(","))

    return render_template("jobs.html", jobs=jobs)