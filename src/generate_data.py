import json
import random

skills_pool = ["C++", "Python", "ML", "Data Science", "Web Dev", "Design", "DSA", "Java"]
interests_pool = ["Music", "Movies", "Poetry", "Sports", "Gaming", "Art"]
music_pool = ["Lo-fi", "Bollywood", "Rock", "Classical", "Pop"]
movies_pool = ["Sci-fi", "Romance", "Thriller", "Comedy", "Action"]
personality_pool = ["Introvert", "Extrovert", "Ambivert"]

bios = [
    "I love coding and exploring new technologies",
    "Music and movies are my escape",
    "Passionate about learning and building projects",
    "Creative thinker and problem solver",
    "I enjoy deep conversations and ideas",
    "Tech enthusiast and startup dreamer",
    "I like writing poetry and reading books",
    "Always curious and eager to learn"
]

years = ["1st", "2nd", "3rd", "4th"]
goals_pool = ["ML", "Web Dev", "Data Science", "Design"]

def generate_student(id):
    return {
        "id": id,
        "skills": random.sample(skills_pool, k=2),
        "interests": random.sample(interests_pool, k=2),
        "music": random.sample(music_pool, k=1),
        "movies": random.sample(movies_pool, k=1),
        "personality": random.choice(personality_pool),
        "bio": random.choice(bios),  # ✅ FIXED (comma added)
        "year": random.choice(years),
        "goals": random.sample(goals_pool, k=1)
    }

def generate_dataset(n=100):
    return [generate_student(i) for i in range(1, n+1)]

if __name__ == "__main__":
    data = generate_dataset(100)

    with open("data/students.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Generated 100 students successfully!")