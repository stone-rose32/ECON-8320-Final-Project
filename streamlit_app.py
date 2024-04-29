import streamlit as st
from pages import introduction, about, data_and_visuals

def main():
    st.sidebar.title("Navigation")

    # Buttons for each page
    if st.sidebar.button("Introduction"):
        introduction.show()
    if st.sidebar.button("About"):
        about.show()
    if st.sidebar.button("Data and Visuals"):
        data_and_visuals.show()

if __name__ == "__main__":
    main()
