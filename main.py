from src.preprocess import load_data, prepare_corpus
from src.vectorize import vectorize
from src.recommend import recommend

# Load data
data = load_data("data/students.json")

# Convert to text corpus
corpus = prepare_corpus(data)

# Convert to vectors
vectors = vectorize(corpus)

# Choose a student (index starts from 0)
user_index = 0

# Get recommendations
results = recommend(user_index, vectors)

print("Recommended connections:\n")

for idx, score in results:
    print(f"Student {data[idx]['id']} | Score: {score:.2f}")