import streamlit as st
from pages import 2_project_details, 1_about, 3_data_and_visuals, 4_project_code

def show():
    st.title("Introduction")
    st.write_stream("Welcome to my ECON 8320 Final Project!")

def main():
    show()


if __name__ == "__main__":
    main()
