import streamlit as st
import requests

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    st.caption(f"Length: {len(password)}")

if st.button("Check Strength"):
    if password:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={"password": password}
        )

        if response.status_code == 200:
            result = response.json()
            strength = result["strength"]

            if strength == "Weak":
                st.error("🔴 Weak Password")
                st.write("Try adding numbers, symbols, and uppercase letters.")
            elif strength == "Medium":
                st.warning("🟡 Medium Password")
                st.write("Consider increasing length and complexity.")
            else:
                st.success("🟢 Strong Password")
                st.write("Good job! This is a strong password 💪")
        else:
            st.error(f"API error: {response.status_code}")
            st.write(response.text)

with st.spinner("Analyzing password..."):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"password": password}
    )