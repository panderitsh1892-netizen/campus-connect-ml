from src.preprocess import load_data, prepare_corpus
from src.vectorize import vectorize
from src.recommend import recommend
from src.cluster import create_clusters
from collections import defaultdict
from src.analyze import find_isolated_students
from src.explain import explain_match
from src.icebreaker import generate_icebreaker
from src.mentor import find_mentors
from src.graph import build_graph   

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
    explanation = explain_match(data[user_index], data[idx])
    icebreaker = generate_icebreaker(data[user_index], data[idx])

    print(f"Student {data[idx]['id']} | Score: {score:.2f}")
    print(f"→ {explanation}")
    print(f"💬 Icebreaker: {icebreaker}\n")

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

# ------------------ ISOLATION DETECTION ------------------

isolated = find_isolated_students(vectors)

print("\nIsolated Students:\n")

for idx, score in isolated:
    print(f"Student {data[idx]['id']} | Avg Similarity: {score:.2f}")

# ------------------ MENTOR MATCHING ------------------

mentors = find_mentors(data, user_index)

print("\nRecommended Mentors:\n")

if mentors:
    for m in mentors:
        print(f"Mentor Student ID: {m}")
else:
    print("No suitable mentors found")

# ------------------ GRAPH NETWORK ------------------

graph = build_graph(vectors)

print("\nGraph Stats:\n")
print("Nodes:", graph.number_of_nodes())
print("Edges:", graph.number_of_edges())