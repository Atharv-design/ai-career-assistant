from flask import Blueprint, render_template, request

job_bp = Blueprint("jobs", __name__)

jobs_data = [
    "Python Developer",
    "Frontend Developer",
    "Backend Engineer",
    "AI Engineer",
    "Data Scientist"
]

@job_bp.route("/jobs", methods=["GET","POST"])
def jobs():
    query = request.form.get("query")

    if query:
        filtered = [j for j in jobs_data if query.lower() in j.lower()]
    else:
        filtered = jobs_data

    return render_template("jobs.html", jobs=filtered)