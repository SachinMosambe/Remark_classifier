import streamlit as st
import requests

# URL of the FastAPI service (adjust host/port if you start it differently)
API_URL = "http://localhost:8000/classify"

st.title("Expense Classifier")

remark = st.text_input("Enter expense remark:")

if st.button("Classify"):
    if not remark:
        st.warning("Please enter a remark before classifying.")
    else:
        try:
            response = requests.post(API_URL, json={"remark": remark})
            response.raise_for_status()
            result = response.json()
            st.success(f"Predicted category: {result.get('predicted_category')}")
        except Exception as exc:
            st.error(f"Failed to get prediction: {exc}")
