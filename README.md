# 💸 Expense Classifier

A machine learning web app that classifies expense remarks into categories using a pre-trained classifier and semantic sentence embeddings.

Built with **FastAPI** (backend) + **Streamlit** (frontend), deployable on **Hugging Face Spaces**.

---

## Project Structure

```
├── app.py                    # Streamlit frontend
├── main.py                   # FastAPI backend
├── load_model.py             # Model loading & prediction logic
├── schema.py                 # Pydantic request schema
├── expense_classifier.pkl    # Pre-trained classifier (required)
├── requirements.txt          # Python dependencies
└── README.md
```

---

## How It Works

1. The user enters a free-text expense remark in the Streamlit UI.
2. The remark is sent to the FastAPI `/classify` endpoint.
3. The backend encodes the remark using `all-mpnet-base-v2` sentence transformer.
4. The vector is passed to the trained classifier, which returns a predicted expense category.
5. The result is displayed in the Streamlit app.

---

## Local Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your model file

Place `expense_classifier.pkl` in the root directory.

### 3. Start the FastAPI backend

```bash
uvicorn main:app --reload
```

### 4. Start the Streamlit frontend

In a separate terminal:

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Deploy on Hugging Face Spaces

### Step 1 — Create a new Space

1. Go to [https://huggingface.co/new-space](https://huggingface.co/new-space)
2. Choose **Docker** as the SDK (needed to run both FastAPI + Streamlit).
3. Set visibility to **Public** or **Private**.

### Step 2 — Add a `requirements.txt`

```
fastapi
uvicorn
streamlit
sentence-transformers
scikit-learn
joblib
requests
```

### Step 3 — Add a startup script

Create `start.sh` to launch both services together:

```bash
#!/bin/bash
uvicorn main:app --host 0.0.0.0 --port 8000 &
streamlit run app.py --server.port 7860 --server.address 0.0.0.0
```

### Step 4 — Add a `Dockerfile`

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["bash", "start.sh"]
```

### Step 5 — Upload your model file

Use `git-lfs` to push the `.pkl` file (Hugging Face requires LFS for large files):

```bash
git lfs install
git lfs track "*.pkl"
git add .gitattributes expense_classifier.pkl
git commit -m "Add model file"
git push
```

### Step 6 — Push everything and go live

```bash
git add .
git commit -m "Initial deployment"
git push
```

Your app will be live at:
`https://huggingface.co/spaces/<your-username>/<your-space-name>`

---

## API Reference

### `POST /classify`

**Request**
```json
{ "remark": "Team lunch at the Italian restaurant" }
```

**Response**
```json
{
  "remark": "Team lunch at the Italian restaurant",
  "predicted_category": "Meals & Entertainment"
}
```

---

## Interactive API Docs

Once the server is running, visit:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
