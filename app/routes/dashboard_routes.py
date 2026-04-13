from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    # safe fallback (error fix)
    data = {
        "resumes": 0,
        "jobs_applied": 0,
        "interviews": 0,
        "username": getattr(current_user, "name", "User")
    }

    return render_template("dashboard.html", data=data)