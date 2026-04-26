from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = [
    "pricing details",
    "product demo",
    "login issue",
    "subscription cost"
]

def find_similar(query):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data + [query])
    sim = cosine_similarity(vectors[-1], vectors[:-1])
    return data[sim.argmax()]
