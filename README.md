# 🔐 Password Strength Detection using Machine Learning

## 🌐 Live Demo

- 🔗 **Frontend (Streamlit App):** https://password-strength-ml.streamlit.app/ 
- 🔗 **Backend API (FastAPI on Render):** https://password-strength-ml-m21m.onrender.com  
- 📘 **API Docs:** https://password-strength-ml-m21m.onrender.com/docs  

---

## 📌 Overview

This project is a **full-stack Machine Learning application** that evaluates password strength in real time.

It combines:
- 🧠 A trained ML model (Random Forest)
- ⚡ A REST API built with FastAPI  
- 🎨 An interactive UI built with Streamlit  

Users can input a password and instantly get:
- Strength classification (Weak / Medium / Strong)
- Security insights (entropy, patterns)
- Improvement suggestions

---

## 🚀 Features

### 🧠 Machine Learning
- Feature-engineered password analysis
- Entropy-based complexity measurement
- Random Forest classifier (multi-class)

### ⚡ Backend (API)
- REST API using FastAPI  
- JSON-based prediction endpoint (`/predict`)
- Deployed on Render  

### 🎨 Frontend (UI)
- Interactive UI using Streamlit  
- Password generator 🔁  
- Strength score (0–100)  
- Entropy calculation 📊  
- Real-time feedback & suggestions  
- API health monitoring  

---


## 📂 Project Structure
```
password-strength-ml/
│
├── assets/ # Screenshots
├── data/ # Dataset (rockyou.txt)
├── models/ # Trained model (.pkl)
│
├── src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── feature_engineering.py
│ ├── model.py
│ ├── train.py
│
├── api/
│ └── main.py # FastAPI backend
│
├── streamlit_app.py # Streamlit frontend
├── main.py # CLI prediction
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
Password length
Uppercase / lowercase count
Digits & special characters
Character ratios
Entropy (randomness measure)
Weak pattern detection ("123", "password")
Repetition patterns

---

## 📊 Model Details
Algorithm: Random Forest Classifier
Library: scikit-learn
Classes:
0 → Weak
1 → Medium
2 → Strong
---


## 📊 Model Performance

📈 Performance
Accuracy: ~91%
F1 Score: ~0.89
---

---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/prathameshsail72-hue/password-strength-ml.git
cd password-strength-ml

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

Run Backend (API)
uvicorn api.main:app --reload

Visit:
http://127.0.0.1:8000/docs

Run Frontend (Streamlit)
streamlit run streamlit_app.py



---

## 📈 Evaluation

The model is evaluated using:

* Accuracy
* Precision / Recall / F1-score

---

## ⚠️ Limitations
No breach detection (e.g. leaked passwords)
Rule-based + ML hybrid (not attack simulation)
Synthetic strong passwords used for balancing
Render free tier causes cold start delays

---

## 📸 Demo

### Password Strength Predictions
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
🔍 Integrate Have I Been Pwned API
🧠 Deep Learning (LSTM / Transformers)
📊 Confidence score output
⚡ Caching & performance optimization
🌍 Multi-language password analysis

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
