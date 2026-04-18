import streamlit as st
import joblib
import pandas as pd
from src.feature_engineering import extract_features

# Load model
model = joblib.load("models/password_model.pkl")

# Title
st.title("🔐 Password Strength Checker")
st.write("Enter a password to evaluate its strength")

# Input
password = st.text_input("Enter Password", type="password")

# Prediction
if st.button("Check Strength"):
    if password:
        features = extract_features(password)
        df = pd.DataFrame([features])
        result = model.predict(df)[0]

        mapping = {
            0: "Weak 🔴",
            1: "Medium 🟡",
            2: "Strong 🟢"
        }

        st.subheader(f"Password Strength: {mapping[result]}")
    else:
        st.warning("Please enter a password")