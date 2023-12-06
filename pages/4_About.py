import streamlit as st
from PIL import Image

st.title("About Stock Trend Prediction")
image = Image.open('C:/Users/Pranav/project works/Project3( ml )/pages/stock-trend-prediction.jpg')
st.image(image, caption='Stock Trend Prediction')
st.write("Welcome to Stock Trend Prediction 📈, a powerful and intuitive web app that utilizes the latest in machine learning technology to provide accurate stock market predictions.")
st.write("Our team of experts has harnessed the power of advanced algorithms 🤖 to analyze vast amounts of market data and generate predictions in real-time. Whether you're a seasoned investor or just starting out, Stock Trend Prediction is the perfect tool to help you stay ahead of the curve and maximize your returns.")
st.write("At the heart of our app lies a state-of-the-art Long Short-Term Memory (LSTM) model 🧠, a type of deep learning neural network specifically designed to handle sequential data such as stock prices. The LSTM model has been trained on vast amounts of historical stock data, allowing it to make informed predictions about future trends.")
st.write("We are constantly updating and improving our app to ensure that you have access to the latest and most advanced technology in stock market analysis 💻. With Stock Trend Prediction, you can rest assured that you're getting the best possible advice for your investments.")
st.write("Developed by:")
st.write(": Pranav Raj")
st.write(": Jasleen Arora")
st.write(": Rishikesh Kumar")

