import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Input form
st.header("Enter your name")
name = st.text_input("What's your name?")

# Display greeting
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit!")
else:
    st.write("Please enter your name to get a personalized greeting.")
