# import streamlit as st

# # Title of the app
# st.title('Country of Ideas')

# # Function to count words
# def count_words(text):
#     return len(text.split())

# # Text input box that directly binds to user input
# user_input = st.text_area("Enter your idea:", height=200)

# # Display the word count live
# word_count = count_words(user_input)
# st.write(f'Word count: {word_count}')

# # Display constraints using Markdown for styling
# st.markdown('<p style="color:gray;font-size:16px;"> Minimum 100 words, Maximum 1000 words </p>', unsafe_allow_html=True)

import streamlit as st

# Title of the app
st.title('Country of Ideas')

# Text input box that directly binds to user input with a placeholder
user_input = st.text_area("Enter your idea:", height=200, placeholder="Enter to Submit")

# Submit button
if st.button('Submit →'):
    st.write("You submitted:", user_input)

# Display constraints using Markdown for styling
st.markdown('<p style="color:gray;font-size:16px;"> Minimum 100 words, Maximum 1000 words </p>', unsafe_allow_html=True)
