def analyze_resume(text):
    text = text.lower()

    skills = ["python", "java", "sql", "html", "css", "javascript", "flask", "react"]
    found_skills = [s for s in skills if s in text]

    score = min(100, 40 + len(found_skills) * 10)

    suggestions = []

    if "project" not in text:
        suggestions.append("Add projects section")

    if "experience" not in text:
        suggestions.append("Add experience")

    if len(found_skills) < 3:
        suggestions.append("Add more skills")

    return {
        "score": score,
        "skills": found_skills,
        "suggestions": suggestions or ["Good resume 👍"]
    }