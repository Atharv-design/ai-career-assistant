from flask import Blueprint, render_template, request, jsonify, session

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat")
def chat():
    return render_template("chat.html")

@chat_bp.route("/chat_api", methods=["POST"])
def chat_api():

    user_msg = request.json.get("message")

    # memory store
    if "history" not in session:
        session["history"] = []

    session["history"].append(user_msg)

    # smart response logic
    msg = user_msg.lower()

    if "career" in msg:
        reply = "Focus on skills + projects + internships. Build real-world experience."
    elif "python" in msg:
        reply = "Python is great for AI, backend, automation. Learn Flask, Django, and projects."
    elif "resume" in msg:
        reply = "Keep resume 1 page, highlight achievements, and use strong action words."
    elif "job" in msg:
        reply = "Apply daily, improve skills, and build strong GitHub projects."
    else:
        reply = "Based on your previous questions, I suggest focusing on consistent learning and projects 🚀"

    return jsonify({"reply": reply})