import streamlit as st

#def support():
st.write("At Stock Trend Prediction, we believe that great customer support is the cornerstone of a successful product. We're here to help you get the most out of our app, and to make sure that you're able to make the most informed investment decisions.")
st.title("Support")
st.write("If you have any questions or need assistance, please don't hesitate to reach out. We're available 24/7 to help you with anything you need.")
st.write("Here are a few ways to get in touch with us:")
st.write("- Email: support@stocktrendprediction.com")
st.write("- Phone: (555) 555-5555")
st.write("- Live Chat: Click the chat icon in the bottom right corner of the page to start a live chat session with one of our support representatives.")
st.write("Or, if you prefer, you can write a description of your issue below:")
issue = st.text_area("Enter your issue here")
if st.button("Submit"):
    st.write("Thank you for submitting your issue. Our support team will review it and get back to you as soon as possible.")
