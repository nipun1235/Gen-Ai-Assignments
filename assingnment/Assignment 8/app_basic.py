# Task 1: Basic Streamlit App
# Create a basic streamlit app that:
# 1. Displays a title : "Welcome to Streamlit"
# 2. Shows a text input box for entering your name.
# 3. When user clicks a button "Greet Me", display: "Hello, !"


import streamlit as st

st.title("Welcome to Streamlit !")

st.text_input("Enter your name: ")

if st.button("Greet Me"):
   st.write("Hello !")