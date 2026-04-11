import json

def load_data(path):
    with open(path, 'r') as f:
        return json.load(f)

def combine_features(student):
    return " ".join(
        student["skills"] +
        student["interests"] +
        student["music"] +
        student["movies"] +
        [student["personality"]] +
        [student["bio"]]
    )

def prepare_corpus(data):
    return [combine_features(student) for student in data]