import requests
import json
import pandas as pd
from tqdm import tqdm

def call_url(year, month, variables):
    url_var = variables[0]
    for var in variables[1:]:
      url_var = str(url_var + ',' + var)
    base_url = 'https://api.census.gov/data/'
    year_month = f'{year}/cps/basic/{month}'
    census_var = f'get={url_var}'
    api_key = '9f3223244e7252dcbb1ed8348a071fc3673eb56e'

    url = f'{base_url}{year_month}?{census_var}&key={api_key}'

    return url

def get_data(url):
    response = requests.get(url)
    return response.json()

def get_data_from_census(years, months, variables):
    all_data = []
    urls = []
    for year in tqdm (years, desc="Loading..."):
        for month in months:
            url = call_url(year, month, variables)
            urls.append(url)
            data = get_data(url)
            yearcol = 'Year'
            monthcol = 'Month'
            data[0].append(yearcol)
            data[0].append(monthcol)
            for row in data[1:]:
                row.append(year)
                row.append(month)
            all_data.extend(data)
    columns = all_data[0]
    rows = all_data[1:]

    census_data = pd.DataFrame(rows, columns=columns)
    return census_data, urls

def main():
    years = [2010, 2011, 2012, 2013, 2014]
    months = ['jan']
    variables = ['GTCBSA', 'HEHOUSUT', 'HETENURE', 'HEFAMINC', 'PEEDUCA', 'PEMLR', 'PESEX', 'PEMARITL']
    data, urls = get_data_from_census(years, months, variables)

    data.to_csv('census_data.csv', index=False)


if __name__ == "__main__":
    main()
