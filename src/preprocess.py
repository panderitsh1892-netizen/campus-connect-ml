import json

def load_data(path):
    with open(path, 'r') as f:
        return json.load(f)


def combine_features(student):
    skills = " ".join(student["skills"] * 3)        # HIGH weight
    interests = " ".join(student["interests"] * 2)  # MEDIUM weight
    music = " ".join(student["music"])
    movies = " ".join(student["movies"])
    personality = student["personality"]
    bio = student["bio"]

    return " ".join([skills, interests, music, movies, personality, bio])

def prepare_corpus(data):
    return [combine_features(student) for student in data]