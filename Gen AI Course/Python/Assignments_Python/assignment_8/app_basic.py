''' Task 1: Basic Streamlit App (app_basic.py)
Create a basic Streamlit app that:
1. Displays a title: "Welcome to Streamlit!"
2. Shows a text input box for entering your name.
3. When user clicks a button "Greet Me", display:
"Hello, !"
Use:
st.title()
st.text_input()
st.button()
st.write() '''


import streamlit as st

st.title("Welcome to Streamlit!!!")
st.text_input("Enter your Name")
if st.button("Greet Me"):
    st.write("Hello, !")