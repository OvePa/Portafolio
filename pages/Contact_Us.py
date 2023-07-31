import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email:")
    subject = st.text_input("Subject:")
    message = st.text_area("Write a message ...")
    message = f"""\
Subject: {subject}

From: {user_email}
{message}
"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")
