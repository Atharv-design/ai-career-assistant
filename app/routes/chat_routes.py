from flask import Blueprint, render_template, request, jsonify

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat")
def chat():
    return render_template("chat.html")

@chat_bp.route("/chat_api", methods=["POST"])
def chat_api():
    user_msg = request.json.get("message", "").lower()

    # basic AI logic (upgrade later with OpenAI)
    if "job" in user_msg:
        reply = "You should focus on skills like Python, SQL, and projects."
    elif "resume" in user_msg:
        reply = "Keep your resume clean, add projects, and quantify achievements."
    elif "interview" in user_msg:
        reply = "Practice DSA + explain your projects clearly."
    else:
        reply = "I am your AI career assistant 🚀 Ask me anything!"

    return jsonify({"reply": reply})