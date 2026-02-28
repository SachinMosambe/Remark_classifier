from fastapi import FastAPI
from load_model import predict_expense_category, load
from schema import Remark_input

app = FastAPI(
    title="Expense Classifier API",
    description="API to classify expense categories based on remarks"
)

@app.on_event("startup")
def startup_event():
    load()

# Root endpoint — Hugging Face uses this to check if app is alive
@app.get("/")
def root():
    return {"status": "Expense Classifier API is running!"}

@app.post("/classify")
def predict_category(input: Remark_input):
    prediction = predict_expense_category(input.remark)
    return {
        "remark": input.remark,
        "predicted_category": prediction
    }