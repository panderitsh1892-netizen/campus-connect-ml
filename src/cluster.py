from sklearn.cluster import KMeans

def create_clusters(vectors, k=5):
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(vectors)
    return labels