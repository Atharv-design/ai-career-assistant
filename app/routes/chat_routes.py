from flask import Blueprint, render_template, request, jsonify
from app.services.chatbot_engine import generate_response

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat")
def chat():
    return render_template("chat.html")

@chat_bp.route("/chat_api", methods=["POST"])
def chat_api():

    msg = request.json.get("message")

    reply = generate_response("user1", msg)

    return jsonify({"reply": reply})