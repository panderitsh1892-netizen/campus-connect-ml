from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def find_isolated_students(vectors, threshold=0.2):
    similarity_matrix = cosine_similarity(vectors)
    
    isolated = []

    for i in range(len(similarity_matrix)):
        # ignore self similarity
        similarities = np.delete(similarity_matrix[i], i)

        avg_similarity = np.mean(similarities)

        if avg_similarity < threshold:
            isolated.append((i, avg_similarity))

    return isolated