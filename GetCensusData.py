import requests
import json
import pandas as pd
from tqdm import tqdm

# Create a class to get the data from the Census API
class GetCensusData:
  # Initialize the class with the API key
  def __init__(self):
    self.api_key = '9f3223244e7252dcbb1ed8348a071fc3673eb56e'
  
  # Create a function to call the URL
  def call_url(self, year, month, variables):
    # Check if the year is less than 2024. The variable name changed in 2024 from GTBSA to CBSA so we need to adjust the URL accordingly
    if year < 2024:
      if 'CBSA' in variables:
        variables[variables.index('CBSA')] = 'GTCBSA'
    else:
      if 'GTCBSA' in variables:
        variables[variables.index('GTCBSA')] = 'CBSA'
    # Join the variables into a string
    url_var = ','.join(variables)
    base_url = 'https://api.census.gov/data/'
    year_month = f'{year}/cps/basic/{month}'
    census_var = f'get={url_var}'
    # Create the URL
    url = f'{base_url}{year_month}?{census_var}&key={self.api_key}'
    return url

  # Create a function to get the data from the URL
  def get_data(self, url):
    response = requests.get(url)
    return response.json()

  # Create a function to get the variable dictionary
  def get_variable_dict(self, years, months):
    # Get the most recent year and month to use are the variable key
    year = max(years)
    month = months[-1]
    base_url = 'https://api.census.gov/data/'
    year_month = f'{year}/cps/basic/{month}/variables.json'
    url = f'{base_url}{year_month}'
    response = requests.get(url)
    data = response.json()
    # Create a dictionary to store the variable information
    variable_info = {}
    # Loop through the variables and get the label and values
    for variable, info in data["variables"].items():
      variable_info[variable] = {
        "label": info.get("label", ""),
        "suggested_weight": info.get("suggested-weight", ""),
        "values": {}
      }
      # Check if there are values for the variable
      if "values" in info:
        # Check if the values are nested
        if "item" in info["values"]:
          # Loop through the values and get the label
          for value, label in info["values"]["item"].items():
            variable_info[variable]["values"][value] = label
        else:
          variable_info[variable]["values"] = info["values"]
    return variable_info

  # Create a function to get the data from the Census API
  def get_data_from_census(self, years, months, variables):
    all_data = []
    # Loop through the years and months to get the data
    for year in tqdm(years, desc="Loading..."):
      for month in months:
          url = self.call_url(year, month, variables)
          data = self.get_data(url)
          yearcol = 'Year'
          monthcol = 'Month'
          # Add the year and month to the data
          data[0].append(yearcol)
          data[0].append(monthcol)
          # Loop through the data and add the year and month to each row
          for row in data[1:]:
            row.append(year)
            row.append(month)
          # Add the data to the list
          all_data.extend(data)
    # Create a dataframe from the data
    # Make first row as columns
    columns = all_data[0]
    rows = all_data[1:]
    # Create a dataframe from the rows and columns
    census_data = pd.DataFrame(rows, columns=columns)
    return census_data

  # Create a function to refine the data
  def data_refine_job(self, data_frame, variable_dict):
    # Check if the column name is GTCBSA or CBSA and rename it to CBSA to match 2024 update to variable name
    if 'GTCBSA' in data_frame.columns:
      data_frame = data_frame.rename(columns={'GTCBSA': 'CBSA'})
    # Loop through the columns and map the values to the labels
    for column in data_frame.columns:
      if column in variable_dict:
        label_dict = variable_dict[column]['values']
        # Map the values to the labels
        data_frame[column] = data_frame[column].astype(str).map(label_dict).fillna(data_frame[column])
    new_column_headers = []
    # Loop through the columns and rename them to the labels
    for header in data_frame.columns:
      if header in variable_dict:
        new_column_headers.append(variable_dict[header]['label'])
      else:
        new_column_headers.append(header)
    # Rename the columns
    data_frame.columns = new_column_headers
    return data_frame
  
#Website Sources: https://stackoverflow.com/questions/40325496/map-pandas-values-to-a-categorical-level
