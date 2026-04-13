import random

memory = {}

def generate_response(user, msg):

    history = memory.get(user, [])

    history.append(("user", msg))

    if "career" in msg.lower():
        reply = "Focus on skills + projects + consistency."
    elif "python" in msg.lower():
        reply = "Learn Flask, Django and build projects."
    else:
        reply = random.choice([
            "Keep learning 🚀",
            "Consistency is key",
            "Build projects"
        ])

    history.append(("ai", reply))

    memory[user] = history

    return reply