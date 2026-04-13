def analyze_resume(text):
    score = 0
    suggestions = []

    if "python" in text.lower():
        score += 20
    else:
        suggestions.append("Add Python skills")

    if "project" in text.lower():
        score += 20
    else:
        suggestions.append("Add projects")

    if len(text) > 200:
        score += 20

    return {
        "score": score,
        "suggestions": suggestions
    }