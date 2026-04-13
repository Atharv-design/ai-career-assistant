import re

# ---- basic datasets ----
SKILLS_DB = [
    "python","java","c++","sql","html","css","javascript","react",
    "node","flask","django","aws","docker","kubernetes","git","linux",
    "machine learning","data analysis","pandas","numpy","tensorflow"
]

SECTION_HINTS = {
    "education": ["education","degree","university","college"],
    "experience": ["experience","work","internship","employment"],
    "projects": ["project","projects"],
    "skills": ["skills","technologies","tech stack"],
    "summary": ["summary","profile","objective"]
}

ACTION_VERBS = [
    "built","developed","designed","implemented","led","created",
    "optimized","improved","automated","analyzed","deployed"
]

def _clean(text: str):
    return re.sub(r"\s+", " ", text).strip().lower()

def _find_sections(text: str):
    found = {k: False for k in SECTION_HINTS}
    for sec, keys in SECTION_HINTS.items():
        for k in keys:
            if k in text:
                found[sec] = True
                break
    return found

def _extract_skills(text: str):
    found = []
    for s in SKILLS_DB:
        if s in text:
            found.append(s)
    return sorted(list(set(found)))

def _action_verb_score(text: str):
    score = 0
    for v in ACTION_VERBS:
        if v in text:
            score += 2
    return min(score, 10)

def _length_score(text: str):
    words = len(text.split())
    if 300 <= words <= 900:
        return 10
    if words < 300:
        return 4
    return 7

def _keyword_score(found_skills):
    return min(len(found_skills) * 2, 20)

def _section_score(sections):
    score = 0
    for k, v in sections.items():
        if v:
            score += 4
    return score  # max 20

def _formatting_score(text: str):
    # crude heuristic: bullet-like symbols / line breaks
    bullets = len(re.findall(r"[-•\*]", text))
    return 5 if bullets >= 5 else 2

def _suggestions(sections, skills):
    sug = []

    if not sections["summary"]:
        sug.append("Add a short professional summary at the top.")

    if not sections["projects"]:
        sug.append("Include 2–3 strong projects with measurable outcomes.")

    if len(skills) < 6:
        sug.append("Add more relevant technical skills (target 8–12).")

    if not sections["experience"]:
        sug.append("Add internships or work experience (even academic).")

    if "aws" not in skills:
        sug.append("Consider adding cloud skills like AWS/GCP.")

    if "docker" not in skills:
        sug.append("Add DevOps exposure (Docker/Kubernetes).")

    return sug

def analyze_resume(text: str):
    raw = text or ""
    t = _clean(raw)

    sections = _find_sections(t)
    skills = _extract_skills(t)

    score = 0
    score += _section_score(sections)       # /20
    score += _keyword_score(skills)         # /20
    score += _action_verb_score(t)          # /10
    score += _length_score(t)               # /10
    score += _formatting_score(raw)         # /5

    # normalize to /100
    score = int(min((score / 65) * 100, 100))

    missing = sorted(list(set(SKILLS_DB) - set(skills)))[:10]

    return {
        "score": score,
        "skills": skills,
        "missing": missing,
        "sections": sections,
        "suggestions": _suggestions(sections, skills)
    }