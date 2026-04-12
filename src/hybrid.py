from sklearn.metrics.pairwise import cosine_similarity

def hybrid_score(vectors, data, i, j):
    # Base similarity (BERT)
    base_score = cosine_similarity([vectors[i]], [vectors[j]])[0][0]

    # Skill overlap
    common_skills = set(data[i]["skills"]) & set(data[j]["skills"])
    skill_bonus = 0.1 * len(common_skills)

    # Interest overlap
    common_interests = set(data[i]["interests"]) & set(data[j]["interests"])
    interest_bonus = 0.05 * len(common_interests)

    return base_score + skill_bonus + interest_bonus