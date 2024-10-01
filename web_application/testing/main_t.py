import streamlit as st

# Set the page configuration to use a wide layout for better appearance
st.set_page_config(layout="wide")

# Title of the app
st.title('Country of Ideas')

# Main content area for input and submission
user_input = st.text_area("Enter your idea:", height=200, placeholder="Type here...")
submitted = st.button('Submit →')

#  HTML and CSS to display the submission text, within a styled box
if submitted:
    st.markdown(f"""
    <style>
    .border-box {{
        border: 2px solid black;
        padding: 10px;
        color: black;
        font-size: 16px;
        position: relative;
        margin-top: 20px;
    }}
    .submission-header {{
        position: absolute;
        left: -10px;
        top: -30px;
        font-size: 16px;
        color: black;
    }}
    </style>
    <div class="border-box">
        <div class="submission-header">You submitted:</div>
        <p>{user_input}</p>
    </div>
    """, unsafe_allow_html=True)

# Display constraints using Markdown for styling
st.markdown('<p style="color:gray;font-size:16px;"> Minimum 100 words, Maximum 1000 words </p>', unsafe_allow_html=True)
