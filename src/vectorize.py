from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize(corpus):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    return vectors