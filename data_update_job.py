import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])


import GetCensusData as gcd
import pandas as pd
import datetime

def get_update_year():
  current_year = []
  today = datetime.date.today().year
  current_year.append(today)

  return current_year

def update_data_job(current_year, current_month, variables, csv_file):
  new_data = gcd.get_data_from_census(current_year, current_month, variables)
  var_dict = gcd.get_variable_dict(current_year, current_month)
  new_rdata = gcd.data_refine_job(new_data, var_dict)
  current_data = pd.read_csv(csv_file)
  updated_data = pd.concat([current_data, new_rdata], ignore_index=True)
  updated_data.to_csv(csv_file, index=False)

def main():
    current_year = get_update_year()
    current_month = 'jan'
    variables = ['CBSA', 'HEHOUSUT', 'HETENURE', 'HEFAMINC', 'PEEDUCA', 'PEMLR', 'PESEX', 'PEMARITL', 'PWCMPWGT', 'HRNUMHOU', 'PWFMWGT', 'PWLGWGT', 'PWORWGT', 'PWSSWGT']
    csv_file = 'census_data.csv'
    
    update_data_job(current_year, current_month, variables, csv_file)


if __name__ == "__main__":
    main()
