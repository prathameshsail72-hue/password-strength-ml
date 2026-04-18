import joblib
import pandas as pd
from src.feature_engineering import extract_features

model = joblib.load("models/password_model.pkl")


def predict(password):
    features = extract_features(password)
    df = pd.DataFrame([features])
    return model.predict(df)[0]


if __name__ == "__main__":
    pwd = input("Enter password: ")

    result = predict(pwd)

    mapping = {
        0: "Weak",
        1: "Medium",
        2: "Strong"
    }

    print("Password strength:", mapping[result])