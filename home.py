import streamlit as st
from pages import about, project_details, data_and_visuals, project_code
#https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/
def show():
    st.title("Introduction")
    col = st.columns((1.5, 4.5, 2), gap='medium')
    with col[0]:
        st.text("Columns 1 text")
    with col[1]:
        st.text("Columns 2 text")
    with col[2]:
        st.text("Columns 3 text")

def main():
    show()


if __name__ == "__main__":
    main()
