import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email:")
    message = st.text_area("Write a message ...")
    button = st.form_submit_button()
    if button:
        pass
