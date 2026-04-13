from flask import Blueprint, render_template, request

job_bp = Blueprint("job", __name__)

JOBS_DB = [
    {"title": "Python Developer", "company": "Google"},
    {"title": "Frontend Developer", "company": "Microsoft"},
    {"title": "Data Analyst", "company": "Amazon"},
    {"title": "AI Engineer", "company": "OpenAI"},
    {"title": "Backend Developer", "company": "Meta"},
    {"title": "Full Stack Developer", "company": "Netflix"},
    {"title": "DevOps Engineer", "company": "Infosys"},
]

@job_bp.route("/jobs", methods=["GET","POST"])
def jobs():
    results = []

    if request.method == "POST":
        query = request.form.get("query","").lower()

        for job in JOBS_DB:
            if query in job["title"].lower():
                results.append(job)

    return render_template("jobs.html", results=results)