import streamlit as st
import pandas as pd

def show(data):
    st.title("Data and Visuals")
    
    tab1, tab2 = st.tabs(["Visualiztions", "Data Table"])
    with tab1:
        st.line_chart(data, x = "Year", y = ["HEHOUSUT", "HETENURE", "HEFAMINC"])
    with tab2:    
        st.dataframe(data)

def main():
    census_data = pd.read_csv("https://raw.githubusercontent.com/stone-rose32/ECON-8320-Final-Project/main/census_data.csv")
    show(census_data)


if __name__ == "__main__":
    main()
