import requests
import json
import pandas as pd

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
months = ['jan']

def call_url(year, month):
    base_url = 'https://api.census.gov/data/'
    year_month = f'{year}/cps/basic/{month}'
    census_var = 'get=GTCBSA,HEHOUSUT,HETENURE,HEFAMINC,PEEDUCA,PEMLR,PESEX,PEMARITL'
    api_key = '9f3223244e7252dcbb1ed8348a071fc3673eb56e'
    
    url = f'{base_url}{year_month}?{census_var}&key={api_key}'
    
    return url

def get_data(url):
    response = requests.get(url)
    return response.json()

def get_data_from_census(years, months):
    all_data = []
    for year in years:
        for month in months:
            url = call_url(year, month)
            data = get_data(url)
            yearcol = 'Year'
            monthcol = 'Month'
            data[0].append(yearcol)
            data[0].append(monthcol)
            for row in data[1:]:
                row.append(year)  # Add year to each row
                row.append(month)  # Add month to each row
            all_data.extend(data)
            print(year+'-'+month)
    return all_data

data = get_data_from_census(years, months)
columns = data[0]
rows = data[1:]

df = pd.DataFrame(rows, columns=columns)

df.to_csv('census_data.csv', index=False)
