from flask import Blueprint, render_template, request, session

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["GET", "POST"])
def chat():
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        msg = request.form["msg"]

        response = f"You asked: {msg}. Focus on skills + projects."

        session["history"].append({"user": msg, "bot": response})

    return render_template("chat.html", history=session["history"])