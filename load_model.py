import joblib
from sentence_transformers import SentenceTransformer

model = None
embedder = None

def load():
    global model, embedder
    model = joblib.load("expense_classifier.pkl")
    embedder = SentenceTransformer('all-MiniLM-L6-v2')


def predict_expense_category(text:str):
    if model is None:
        load()
    embedding = embedder.encode([text])
    return model.predict(embedding)[0]
