from src.preprocess import load_data, prepare_corpus
from src.vectorize import vectorize
from src.recommend import recommend
from src.cluster import create_clusters
from collections import defaultdict

# Load data
data = load_data("data/students.json")

# Convert to text corpus
corpus = prepare_corpus(data)

# Convert to vectors
vectors = vectorize(corpus)

# ------------------ RECOMMENDATION ------------------

user_index = 0  # test for first student

results = recommend(user_index, vectors)

print("Recommended connections:\n")

for idx, score in results:
    print(f"Student {data[idx]['id']} | Score: {score:.2f}")

# ------------------ CLUSTERING ------------------

clusters = create_clusters(vectors, k=5)

print("\nCluster assignments:\n")

for i, cluster_id in enumerate(clusters):
    print(f"Student {data[i]['id']} → Cluster {cluster_id}")

# ------------------ GROUPED CLUSTERS ------------------

cluster_groups = defaultdict(list)

for i, cluster_id in enumerate(clusters):
    cluster_groups[cluster_id].append(data[i]["id"])

print("\nGrouped Clusters:\n")

for cluster_id, members in cluster_groups.items():
    print(f"Cluster {cluster_id}: {members}")