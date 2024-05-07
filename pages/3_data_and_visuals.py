import streamlit as st
import pandas as pd
import plotly.express as px

def show(data):
    st.title("Data and Visuals")
    
    tab1, tab2 = st.tabs(["Visualiztions", "Data Table"])
    with tab1:
        st.title('CPS Data Analysis')
    
        selected_variable = st.selectbox('Select a variable', data.columns)
        fig = None

        if selected_variable == 'Household-total family income in past 12 months':
            fig = px.histogram(data, x=selected_variable, title='Distribution of Household Total Family Income')
        elif selected_variable == 'Household-type of living quarters':
            fig = px.pie(data, names=selected_variable, title='Percentage of Household Types of Living Quarters')
        elif selected_variable == 'Demographics-sex':
            fig = px.bar(data['Demographics-sex'].value_counts().reset_index(), x='index', y='Demographics-sex', title='Count of Males and Females')
        elif selected_variable == 'Household-total # of members':
            fig = px.box(data, y=selected_variable, title='Distribution of Household Total Number of Members')
        elif selected_variable == 'Month':
            fig = px.line(data.groupby(selected_variable).size().reset_index(), x=selected_variable, y=0, title='Trends Over Time')
    
        if fig:
            st.plotly_chart(fig)
        else:
            st.write("No plot available for the selected variable.")
    with tab2:    
        st.dataframe(data)

def main():
    census_data = pd.read_csv("https://raw.githubusercontent.com/stone-rose32/ECON-8320-Final-Project/main/census_data.csv")
    show(census_data)


if __name__ == "__main__":
    main()
