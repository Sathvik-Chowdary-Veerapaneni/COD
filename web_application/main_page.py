import streamlit as st

# Title of the app
st.title('Country of Ideas')

# Adding text input box
user_input = st.text_input("Enter your idea:")
st.write("You entered:", user_input)
