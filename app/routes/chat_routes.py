from flask import Blueprint, render_template, request, jsonify

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat")
def chat():
    return render_template("chat.html")

@chat_bp.route("/chat_api", methods=["POST"])
def chat_api():
    msg = request.json.get("message").lower()

    if "career" in msg:
        reply = "Focus on skills, projects and internships."
    elif "python" in msg:
        reply = "Learn Flask, Django and build projects."
    else:
        reply = "Keep learning consistently 🚀"

    return jsonify({"reply": reply})