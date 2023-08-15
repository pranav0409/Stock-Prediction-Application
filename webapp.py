import streamlit as st
from streamlit_option_menu import option_menu


def home():
    st.write("Welcome to the home page")

def app():
    st.write("This is the project page")

def about():
    st.write("Learn more about us")


# horizontal menu
selected = option_menu(None, ["Home", "App", 'About'], 
    icons=['house', 'cloud-upload', "list-task"], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected

if selected == "Home":
    import home
elif selected == "app":
    import app
elif selected == "About":
    import about
