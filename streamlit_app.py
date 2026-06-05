import streamlit as st
import requests
import random
import string
import math

API_URL = "https://password-strength-ml-m21m.onrender.com/predict"
BASE_URL = "https://password-strength-ml-m21m.onrender.com"

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

theme = st.sidebar.radio("Theme", ["Dark", "Light"])

if theme == "Dark":
    bg = "#0E1117"
    text = "white"
else:
    bg = "white"
    text = "black"

st.markdown(f"""
<style>
body {{
    background-color: {bg};
    color: {text};
}}
.big-title {{
    font-size: 40px;
    font-weight: 700;
    text-align: center;
}}
.subtitle {{
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}}
</style>
""", unsafe_allow_html=True)

try:
    requests.get(BASE_URL, timeout=5)
    st.sidebar.success("API Online ✅")
except:
    st.sidebar.error("API Offline ❌")

st.markdown('<p class="big-title">🔐 Password Strength Checker</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-powered password analysis with smart insights</p>', unsafe_allow_html=True)

password = st.text_input("Enter your password", type="password")

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

if st.button("Generate Strong Password 🔁"):
    password = generate_password()
    st.code(password)

def calculate_entropy(pw):
    charset = 0
    if any(c.islower() for c in pw): charset += 26
    if any(c.isupper() for c in pw): charset += 26
    if any(c.isdigit() for c in pw): charset += 10
    if any(c in "!@#$%^&*" for c in pw): charset += 8
    if charset == 0:
        return 0
    return round(len(pw) * math.log2(charset), 2)

if password:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Length", len(password))
    with col2:
        st.metric("Digits", sum(c.isdigit() for c in password))
    with col3:
        entropy = calculate_entropy(password)
        st.metric("Entropy", entropy)
        st.caption("Entropy measures randomness — higher is more secure")

if st.button("Check Strength 🚀"):

    if not password:
        st.warning("Please enter a password")
    else:
        try:
            with st.spinner("Waking up server... (first request may take up to 60s)"):
                response = requests.post(
                    API_URL,
                    json={"password": password},
                    timeout=(5, 60)
                )

            if response.status_code == 200:
                result = response.json()
                strength = result.get("strength", "Unknown")

                score_map = {
                    "Weak": 30,
                    "Medium": 60,
                    "Strong": 100
                }
                score = score_map.get(strength, 0)

                st.progress(score)
                st.caption(f"Strength Score: {score}/100")

                if strength == "Weak":
                    st.error("🔴 Weak Password")
                elif strength == "Medium":
                    st.warning("🟡 Medium Password")
                elif strength == "