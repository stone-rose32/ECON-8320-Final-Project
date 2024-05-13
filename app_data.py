import GetCensusData as gcd

def main():
    # Create a list of years, months, and variables to get the data from the Census API
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    months = ['jan']
    variables = ['CBSA', 'HEHOUSUT', 'HETENURE', 'HEFAMINC', 'HRNUMHOU', 'PEEDUCA', 'PESEX', 'PEMARITL', 'PEMLR', 'PWCMPWGT', 'HWHHWGT', 'PWFMWGT', 'PWLGWGT', 'PWORWGT', 'PWSSWGT']

    # Get the data from the Census API using the GetCensusData class
    var_dict = gcd.GetCensusData().get_variable_dict(years, months)
    census_data = gcd.GetCensusData().get_data_from_census(years, months, variables)
    census_rdata= gcd.GetCensusData().data_refine_job(census_data, var_dict)

    # Save the data to a CSV file
    census_rdata.to_csv('census_data.csv', index=False)


if __name__ == "__main__":
    main()
