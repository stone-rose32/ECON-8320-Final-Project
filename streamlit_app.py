import streamlit as st
from pages import project_details, about, data_and_visuals

def show():
    st.title("Introduction")
    st.write_stream("Welcome to my ECON 8320 Final Project!")

def main():
    show()


if __name__ == "__main__":
    main()