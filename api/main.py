import pandas as pd

from fastapi import FastAPI
import joblib

from api.schema import PasswordRequest
from src.feature_engineering import extract_features

app = FastAPI(title="Password Strength API")

# Load trained model
model = joblib.load("models/password_model.pkl")

label_map = {
    0: "Weak",
    1: "Medium",
    2: "Strong"
}

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.post("/predict")
def predict(request: PasswordRequest):
    password = request.password

    features = extract_features(password)
    df = pd.DataFrame([features])   # VERY IMPORTANT
    prediction = model.predict(df)[0]

    return {
        "password": password,
        "strength": label_map[prediction]
    }