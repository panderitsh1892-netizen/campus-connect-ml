def explain_match(student_a, student_b):
    common_skills = list(set(student_a["skills"]) & set(student_b["skills"]))
    common_interests = list(set(student_a["interests"]) & set(student_b["interests"]))
    common_music = list(set(student_a["music"]) & set(student_b["music"]))
    common_movies = list(set(student_a["movies"]) & set(student_b["movies"]))

    explanation = []

    if common_skills:
        explanation.append(f"common skills: {', '.join(common_skills)}")

    if common_interests:
        explanation.append(f"common interests: {', '.join(common_interests)}")

    if common_music:
        explanation.append(f"both like {', '.join(common_music)} music")

    if common_movies:
        explanation.append(f"both enjoy {', '.join(common_movies)} movies")

    if not explanation:
        return "You both have diverse interests — great opportunity to explore new perspectives!"

    return "You both share " + " | ".join(explanation)