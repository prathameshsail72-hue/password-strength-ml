import pandas as pd
import joblib

from src.data_loader import load_passwords
from src.preprocessing import generate_strong_password, label_password
from src.feature_engineering import extract_features
from src.model import get_model

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def build_dataset():
    print("Loading weak passwords...")
    weak_passwords = load_passwords("data/rockyou.txt", limit=50000)

    print("Generating strong passwords...")
    strong_passwords = [generate_strong_password() for _ in range(50000)]

    all_passwords = weak_passwords + strong_passwords

    print("Labeling data...")
    labels = [label_password(p) for p in all_passwords]

    print("Extracting features...")
    features = [extract_features(p) for p in all_passwords]

    df = pd.DataFrame(features)
    df['label'] = labels

    return df


def train():
    df = build_dataset()

    X = df.drop(columns=['label'])
    y = df['label']

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training model...")
    model = get_model()
    model.fit(X_train, y_train)

    print("Evaluating model...")
    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

    print("Saving model...")
    joblib.dump(model, "models/password_model.pkl")

    print("Done!")


if __name__ == "__main__":
    train()