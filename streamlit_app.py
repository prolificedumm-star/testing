import streamlit as st

st.title("Hello Streamlit Cloud!")

name = st.text_input("Your name:")
if st.button("Submit"):
    st.success(f"Hi {name}!")
