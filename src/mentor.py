def find_mentors(data, user_index):
    user = data[user_index]
    mentors = []

    for i, student in enumerate(data):
        if i == user_index:
            continue

        # senior condition
        if student["year"] > user["year"]:
            # skill match
            if any(skill in student["skills"] for skill in user["goals"]):
                mentors.append(student["id"])

    return mentors