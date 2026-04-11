import random

def generate_icebreaker(student_a, student_b):
    topics = list(set(student_a["interests"]) & set(student_b["interests"]))

    if not topics:
        return "Hey! I'd love to know more about your interests and experiences."

    topic = random.choice(topics)

    prompts = {
        "Music": "What's your favorite song these days?",
        "Movies": "What's the best movie you've watched recently?",
        "Poetry": "Do you write or read poetry? Any favorite lines?",
        "Gaming": "What games are you into right now?",
        "Sports": "Do you follow any sports regularly?"
    }

    return prompts.get(topic, "Tell me more about what you enjoy doing!")