import streamlit as st
import secrets
import string
import pyperclip

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

st.title("Password Generator")

length = st.slider("Select password length:", min_value=8, max_value=32, value=12, step=1)

if st.button("Generate Password"):
    password = generate_password(length)
    st.write("Generated Password:", password)
    if st.button("Copy Password"):
        pyperclip.copy(password)
        st.success("Password copied to clipboard!")
