import streamlit as st
import pandas as pd
import plotly.express as px

# Create a function to load the data into streamlit. @st.cache_data is used to cache the data so that it is not reloaded every time the page is refreshed.
@st.cache_data
def load_data(filename):
    # Load the data in chunks to avoid memory issues
    chunk_size = 50_000
    chunks = []
    # Read the data in chunks
    for chunk in pd.read_csv(filename, chunksize=chunk_size):
        chunks.append(chunk)
    
    # Concatenate the chunks into a single dataframe
    data = pd.concat(chunks, axis=0)
    return data

# Create a function to show the data in the dashboard
def show(data):
    st.title("Exploration of Who Owns Home/Living Quarters in the US")
    st.write("The purpose of this dashboard is to allow users to explore the data from the Current Population Survey (CPS) to understand who owns home/living quarters in the US. The data is from the US Census Bureau and is publicly available.")
    st.write("Below are some visualizations that show the distribution of Home Ownership in the US by various demographics.")
    filtered_columns = data.filter(regex='^(?!.*Weight).*$', axis=1)
    
    # Create a sidebar to allow users to filter the data
    with st.sidebar:
        cities = ['Select All'] + data['Metropolitan Core Based Statistical Area FIPS Code'].unique().tolist()
        select_loc = st.selectbox('Select a location:', cities)

    # Filter the data based on the selected location
    filtered_data = data.copy()
    if select_loc != 'Select All':
        filtered_data = filtered_data[filtered_data['Metropolitan Core Based Statistical Area FIPS Code'] == select_loc]

    # Show the filtered data in various charts
    # Create a bar chart to show the distribution of home ownership by gender
    ownership_gender_counts = filtered_data.groupby(['Household-own/rent living quarters', 'Demographics-sex']).size().unstack()
    fig = px.bar(ownership_gender_counts, x=ownership_gender_counts.index, y=['Female', 'Male'], barmode='group', labels={'x': 'Ownership Status', 'y': 'Count'})
    fig.update_layout(title="Gender Distribution by Ownership Status")
    st.plotly_chart(fig)
    
    # Create a bar chart to show the distribution of home ownership by marital status
    ownership_marital_counts = filtered_data.groupby(['Household-own/rent living quarters', 'Demographics-marital status']).size().unstack()
    fig = px.bar(ownership_marital_counts, x=ownership_marital_counts.index, y=['Married - Spouse Present', 'Never Married'], barmode='group', labels={'x': 'Ownership Status', 'y': 'Count'})
    fig.update_layout(title="Marital Status Distribution by Ownership Status")
    st.plotly_chart(fig)
    
    # Create a bar chart to show the distribution of home ownership by employment status
    ownership_employment_counts = filtered_data.groupby(['Household-own/rent living quarters', 'Labor Force-employment status']).size().unstack()
    fig = px.bar(ownership_employment_counts, x=ownership_employment_counts.index, y=['Employed-At Work', 'Retired-Not In Labor Force'], barmode='group', labels={'x': 'Ownership Status', 'y': 'Count'})
    fig.update_layout(title="Employment Status Distribution by Ownership Status")
    st.plotly_chart(fig)
    
    # Create a histogram to show the distribution of family size by home ownership
    fig = px.histogram(filtered_data, x='Household-total # of members', color='Household-own/rent living quarters')
    fig.update_layout(title="Distribution of Family Size by Home Ownership")
    st.plotly_chart(fig)

    # Create a line chart to show the change in homeownership over the years
    ownership_year_counts = filtered_data.groupby(['Year', 'Household-own/rent living quarters']).size().reset_index(name='Count')
    fig = px.line(ownership_year_counts, x='Year', y='Count', color='Household-own/rent living quarters', labels={'Count': 'Count', 'Year': 'Year'})
    fig.update_layout(title="Change in Homeownership Over the Years")
    st.plotly_chart(fig)

# Create a main function to run the dashboard
def main():
    sample_data = load_data("https://github.com/stone-rose32/ECON-8320-Final-Project/releases/download/v1.0.0/census_data.csv")
    show(sample_data)

# Run the main function
if __name__ == "__main__":
    main()

#Website Sources: https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/
#https://towardsdatascience.com/building-a-dashboard-in-under-5-minutes-with-streamlit-fd0c906ff886
#https://discuss.streamlit.io/t/streamlit-with-datasets-up-to-1-mil-of-rows/51415
#https://stackoverflow.com/questions/58830858/plotly-how-to-create-a-barchart-using-group-by
