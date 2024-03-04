import streamlit as st
import secrets
import string

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
        st.write("Copy the password below:")
        st.text_area("Copied Password", value=password, height=1, key="password")
        st.write(
            """
            <button onclick="copyToClipboard()">Copy Password</button>
            <script>
                function copyToClipboard() {
                    const textarea = document.getElementById('password');
                    textarea.select();
                    document.execCommand('copy');
                    alert('Password copied to clipboard!');
                }
            </script>
            """,
            unsafe_allow_html=True
        )
