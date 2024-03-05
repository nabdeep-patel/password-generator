import streamlit as st
import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

st.title("Password Generator")

length = st.slider("Select password length:", min_value=8, max_value=32, value=12, step=1)

if st.button("Generate Password"):
    password = generate_password(length)
    st.write("Generated Password:")
    st.text_area("Password", value=password, height=1, key="password", disabled=True)
