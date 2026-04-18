# 🔐 Password Strength Detection using Machine Learning

## 📌 Overview

This project builds a machine learning model to classify password strength into three categories:

* Weak
* Medium
* Strong

The model is trained using real-world leaked password datasets and synthetic strong passwords, and uses feature engineering techniques to evaluate password complexity.

---

## 🚀 Features

* Modular ML pipeline (data loading → preprocessing → feature engineering → training)
* Feature-based password analysis (length, entropy, patterns, etc.)
* Random Forest classifier for prediction
* CLI-based password strength checker
* Clean and scalable project structure

---

## 📂 Project Structure

```
password-strength-ml/
│
├── data/                  # Dataset (rockyou.txt)
├── models/                # Saved trained models
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── train.py
│
├── main.py                # Prediction script
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

Download RockYou dataset from Kaggle and place it in:

data/rockyou.txt

* RockYou password dataset (real-world leaked passwords)
* Synthetic strong passwords generated programmatically

⚠️ Note: Dataset contains weak passwords, so strong passwords are artificially generated to balance the dataset.

---

## 🧠 Feature Engineering

The model uses the following features:

* Password length
* Number of uppercase/lowercase characters
* Number of digits and special characters
* Character ratios
* Entropy (randomness measure)
* Detection of common weak patterns (e.g., "123", "password")
* Maximum repeated character sequence

---

## 🤖 Model

* Algorithm: Random Forest Classifier
* Library: scikit-learn
* Multi-class classification (0 = Weak, 1 = Medium, 2 = Strong)

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/password-strength-ml.git
cd password-strength-ml
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

### Step 1: Train the model

```
python -m src.train
```

### Step 2: Run prediction

```
python main.py
```

### Example

```
Enter password: P@ssw0rd123
Password strength: Medium
```

---

## 📈 Evaluation

The model is evaluated using:

* Accuracy
* Precision / Recall / F1-score

---

## ⚠️ Limitations

* Does not check if password has been leaked (no breach database integration)
* Strength is estimated based on patterns, not real attack simulations
* Synthetic data may not fully represent real strong passwords

---

## 📸 Demo

### Password Predictions
![Demo 1](https://raw.githubusercontent.com/prathameshsail72-hue/password-strength-ml/main/assets/s1.png)
![Demo 2](https://raw.githubusercontent.com/prathameshsail72-hue/password-strength-ml/main/assets/s2.png)
![Demo 3](https://raw.githubusercontent.com/prathameshsail72-hue/password-strength-ml/main/assets/s3.png)

### Training Output
![Output](https://raw.githubusercontent.com/prathameshsail72-hue/password-strength-ml/main/assets/d4.png)

### Project Structure
![Structure](https://raw.githubusercontent.com/prathameshsail72-hue/password-strength-ml/main/assets/d5.png)
---

## 🌐 Web App Demo (Streamlit)

Run the app locally:

```bash```
streamlit run app.py
---

## 🔮 Future Improvements

* Add API using FastAPI
* Deploy it using Render
* Integrate Have I Been Pwned API
* Use deep learning (LSTM/Transformer)
* Improve labeling strategy

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Prathamesh Sail
GitHub: https://github.com/prathameshsail72-hue
