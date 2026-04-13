from flask import Blueprint, render_template, request
from app.services.resume_parser import analyze_resume

resume_bp = Blueprint("resume", __name__)

@resume_bp.route("/resume", methods=["GET", "POST"])
def resume():
    result = None

    if request.method == "POST":
        file = request.files.get("resume")

        if file:
            text = file.read().decode("utf-8", errors="ignore")
            result = analyze_resume(text)

    return render_template("resume.html", result=result)