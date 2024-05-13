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
    for chunk in pd.read_csv(filename, chunksize=chunk_size, low_memory=False):
        chunks.append(chunk)
    
    # Concatenate the chunks into a single dataframe
    data = pd.concat(chunks, axis=0)
    return data

def remove_text_rows(data, columns):
    # Filter out rows where the specified columns contain non-numeric values
    for col in columns:
        data = data[pd.to_numeric(data[col], errors='coerce').notnull()]
    return data

def convert_columns_to_int(data):
    # List of columns to convert to integers
    columns_to_convert = [col for col in data.columns if 'weight' in col.lower() or 'year' in col.lower() or 'household total #' in col.lower()]
    
    # Remove rows with text in the specified columns
    data = remove_text_rows(data, columns_to_convert)
    
    # Convert selected columns to integers
    for col in columns_to_convert:
        data[col] = pd.to_numeric(data[col], errors='coerce')
        data[col] = data[col].fillna(0).astype(int)
    return data

def show():
    st.title("Data and Visuals")

    # Load the data
    data = load_data("https://github.com/stone-rose32/ECON-8320-Final-Project/releases/download/v1.0.0/census_data.csv")
    data = convert_columns_to_int(data)
    
    # Create tabs for the different sections of the data and visuals
    tab1, tab2 = st.tabs(["Visualizations", "Data Table"])
    with tab1:
        st.write('CPS Data Analysis')
        # Create a sidebar to allow users to filter the data. Removed Weight fields from dropbox
        filtered_columns = data.filter(regex='^(?!.*Weight).*$', axis=1)
        # Create a sidebar to allow users to filter the data
        with st.sidebar:
            cities = ['Select All'] + data['Metropolitan Core Based Statistical Area FIPS Code'].unique().tolist()
            select_loc = st.selectbox('Select a location:', cities)
            year_range = st.slider('Select a year range:', 2010, int(data['Year'].max()), (2019, 2024))
            own_rent_options = ['Select All', 'Owned Or Being Bought By A Hh Member', 'Rented For Cash Rent', 'Occupied Without Payment Of Cash Rent']
            own_rent_selected = st.selectbox('Filter by own/rent:', own_rent_options)
            selected_variable = st.selectbox('Select a variable', filtered_columns.columns.tolist())
            var_values = ['Select All'] + data[selected_variable].unique().tolist()
            selected_var_value = st.selectbox('Filter by variable values:', var_values)
        
        # Filter the data based on the selected location and year range
        if select_loc == 'Select All':
            filtered_data = data[(data['Year'].between(year_range[0], year_range[1]))]
        else:
            filtered_data = data[(data['Year'].between(year_range[0], year_range[1])) & (data['Metropolitan Core Based Statistical Area FIPS Code'] == select_loc)]
        
        # Filter the data based on the selected own/rent and variable values
        if own_rent_selected != 'Select All':
            filtered_data = filtered_data[filtered_data['Household-own/rent living quarters'] == own_rent_selected]
        
        if selected_var_value != 'Select All':
            filtered_data = filtered_data[filtered_data[selected_variable] == selected_var_value]
        
        fig = None

        # Show the filtered data in various charts
        if selected_variable == 'Metropolitan Core Based Statistical Area FIPS Code':        
            own_living_quarters = filtered_data[filtered_data['Household-own/rent living quarters'] == 'Owned Or Being Bought By A Hh Member']
            own_quarters_by_area = own_living_quarters.groupby('Metropolitan Core Based Statistical Area FIPS Code')['Weight-composited final weight'].sum().reset_index()
            own_quarters_by_area.columns = ['Metropolitan Area', 'Weighted Number of Participants Owning Living Quarters']
            own_quarters_by_area['Weighted Number of Participants Owning Living Quarters'] = own_quarters_by_area['Weighted Number of Participants Owning Living Quarters'].round()
            own_quarters_by_area = own_quarters_by_area[own_quarters_by_area['Weighted Number of Participants Owning Living Quarters'] != 0]
            st.write(own_quarters_by_area)

        elif selected_variable == 'Household-type of living quarters':
            fig = px.pie(filtered_data, names=selected_variable, values='Weight-household', title='Weighted Percentage of Household Types of Living Quarters', hole=0.5)

        elif selected_variable == 'Household-own/rent living quarters':
            fig = px.pie(filtered_data, names=selected_variable, values='Weight-household', title='Weighted Percentage of Household Ownership of Living Quarters', hole=0.5)

        elif selected_variable == 'Household-total family income in past 12 months':
            fig = px.histogram(filtered_data, x=selected_variable, title='Distribution of Household Total Family Income- Unweighted', category_orders={selected_variable: ['Less Than $5,000', '5,000 To 7,499', '7,500 To 9,999', '10,000 To 12,499', '12,500 To 14,999', '15,000 To 19,999', '20,000 To 24,999', '25,000 To 29,999', '30,000 To 34,999', '35,000 To 39,999', '40,000 To 49,999', '50,000 To 59,999', '60,000 To 74,999', '75,000 To 99,999', '100,000 To 149,999', '150,000 or More',]})

        elif selected_variable == 'Demographics-highest level of school completed':
            edu_counts = filtered_data.groupby(['Year', 'Demographics-highest level of school completed', 'Household-own/rent living quarters'])['Weight-second stage weight (rake 6 final step weight)'].sum().reset_index()
            fig = px.bar(edu_counts, x='Year', y='Weight-second stage weight (rake 6 final step weight)', color='Demographics-highest level of school completed', title='Weighted Count of Highes
