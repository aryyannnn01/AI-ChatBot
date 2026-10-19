import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)["intents"]

questions = []
tags = []

for intent in intents:
    for pattern in intent["patterns"]:
        questions.append(pattern)
        tags.append(intent["tag"])

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_bot_response(message):
    user_vector = vectorizer.transform([message])
    scores = cosine_similarity(user_vector, question_vectors)[0]
    best_match = scores.argmax()

    if scores[best_match] < 0.25:
        return "Sorry, I couldn't understand your question. Please try another question."

    matched_tag = tags[best_match]

    for intent in intents:
        if intent["tag"] == matched_tag:
            return random.choice(intent["responses"])

    return "Sorry, I couldn't find an answer."