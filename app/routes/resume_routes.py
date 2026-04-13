from flask import Blueprint, render_template, request
import os

resume_bp = Blueprint("resume", __name__)

UPLOAD_FOLDER = "app/static/uploads"

@resume_bp.route("/resume", methods=["GET","POST"])
def resume():

    if request.method == "POST":

        file = request.files.get("file")

        if not file or file.filename == "":
            return "No file selected ❌"

        # ensure folder exists
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        return f"Uploaded ✅: {file.filename}"

    return render_template("resume.html")