from flask import Blueprint, render_template, request

job_bp = Blueprint("job", __name__)

jobs_data = [
    {"title": "Python Developer"},
    {"title": "Frontend Developer"},
    {"title": "AI Engineer"},
    {"title": "Data Scientist"}
]

@job_bp.route("/jobs", methods=["GET", "POST"])
def jobs():
    results = []

    if request.method == "POST":
        query = request.form["query"].lower()
        results = [job for job in jobs_data if query in job["title"].lower()]

    return render_template("jobs.html", jobs=results)