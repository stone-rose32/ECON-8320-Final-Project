import streamlit as st

def show():
    st.title("About")
    st.write_stream("Learn more about our app, the author, and its purpose here.")

def main():
    show()


if __name__ == "__main__":
    main()
