import streamlit as st
from pages import introduction, about, data_and_visuals

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Introduction", "About", "Data and Visuals"])

    if page == "Introduction":
        introduction.show()
    elif page == "About":
        about.show()
    elif page == "Data and Visuals":
        data_and_visuals.show()

if __name__ == "__main__":
    main()
