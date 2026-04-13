from flask import Blueprint, render_template, request, redirect
from app.models.user_model import User
from app import db
from flask_login import login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET"])
def home():
    return render_template("auth/login.html")

@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email, password=password).first()

    if user:
        login_user(user)
        return redirect("/dashboard")

    return "Invalid login"

@auth_bp.route("/register", methods=["POST"])
def register():
    user = User(
        email=request.form["email"],
        password=request.form["password"]
    )
    db.session.add(user)
    db.session.commit()
    return redirect("/")