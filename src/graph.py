import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity

def build_graph(vectors, threshold=0.75):
    G = nx.Graph()
    similarity_matrix = cosine_similarity(vectors)

    n = vectors.shape[0]

    for i in range(n):
        G.add_node(i)

    for i in range(n):
        for j in range(i+1, n):
            if similarity_matrix[i][j] > threshold:
                G.add_edge(i, j)

    return G