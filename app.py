import streamlit as st
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

st.title("Password Generator")
length = st.slider("Select Password Length", 8, 128, 12)
password = generate_password(length)
st.write("Your generated password is:", password)
