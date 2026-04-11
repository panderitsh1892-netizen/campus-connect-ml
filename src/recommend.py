from sklearn.metrics.pairwise import cosine_similarity

def recommend(user_index, vectors, top_n=2):
    similarity_matrix = cosine_similarity(vectors)

    scores = list(enumerate(similarity_matrix[user_index]))

    # sort by similarity
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # remove self
    scores = scores[1:top_n+1]

    return scores