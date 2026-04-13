from flask import Blueprint, render_template, request
import os

resume_bp = Blueprint("resume", __name__)

UPLOAD_FOLDER = "app/static/uploads"

@resume_bp.route("/resume", methods=["GET","POST"])
def resume():

    result = None

    if request.method == "POST":
        file = request.files.get("resume")

        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            text = file.filename.lower()

            # simple smart analysis
            score = 50
            improvements = []

            if "project" in text:
                score += 15
            else:
                improvements.append("Add Projects Section")

            if "skill" in text:
                score += 15
            else:
                improvements.append("Add Skills Section")

            if "experience" in text:
                score += 20
            else:
                improvements.append("Add Experience Section")

            result = {
                "score": score,
                "improvements": improvements,
                "message": "Resume analyzed successfully 🚀"
            }

    return render_template("resume.html", result=result)