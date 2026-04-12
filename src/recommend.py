from src.hybrid import hybrid_score

def recommend(user_index, vectors, data, top_n=2):
    scores = []

    for i in range(len(vectors)):
        if i == user_index:
            continue

        score = hybrid_score(vectors, data, user_index, i)
        scores.append((i, score))

    # sort by score descending
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    return scores[:top_n]