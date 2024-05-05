import streamlit as st
import pandas as pd

def show():
    st.title("Data and Visuals")
    
    census_data = pd.read_csv("https://raw.githubusercontent.com/stone-rose32/ECON-8320-Final-Project/main/census_data.csv")

    st.dataframe(census_data)

def main():
    show()


if __name__ == "__main__":
    main()
