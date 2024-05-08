import GetCensusData as gcd

def main():
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    months = ['jan']
    variables = ['CBSA', 'HEHOUSUT', 'HETENURE', 'HEFAMINC', 'PEEDUCA', 'PEMLR', 'PESEX', 'PEMARITL', 'PWCMPWGT', 'HRNUMHOU', 'PWFMWGT', 'PWLGWGT', 'PWORWGT', 'PWSSWGT']

    var_dict = gcd.get_variable_dict(years, months)
    census_data = gcd.get_data_from_census(years, months, variables)
    census_rdata= gcd.data_refine_job(census_data, var_dict)

    census_rdata.to_csv('census_data.csv', index=False)


if __name__ == "__main__":
    main()
