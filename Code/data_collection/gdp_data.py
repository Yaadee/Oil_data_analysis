import wbdata
import pandas as pd
from datetime import datetime

# Function to get GDP data from World Bank for a specific country
def get_gdp_data(country_code):
    indicators = {'NY.GDP.MKTP.CD': 'GDP'}
    gdp_data = wbdata.get_dataframe(indicators, country=country_code, date=(datetime(1987, 5, 20), datetime.now()))
    gdp_data.reset_index(inplace=True)
    return gdp_data

# Get list of country codes
countries = wbdata.get_countries()

# Loop through each country code and collect GDP data
all_gdp_data = pd.DataFrame()  # Initialize an empty DataFrame to store all data

for country in countries:
    country_code = country['id']
    country_name = country['name']
    
    try:
        gdp_data_country = get_gdp_data(country_code)
        gdp_data_country['Country Name'] = country_name  # Add country name column
        all_gdp_data = pd.concat([all_gdp_data, gdp_data_country], ignore_index=True)
        print(f"Collected GDP data for {country_name} ({country_code})")
    except Exception as e:
        print(f"Failed to collect GDP data for {country_name} ({country_code}): {str(e)}")

# Save all GDP data to CSV
all_gdp_data.to_csv('Inputs/data/all_countries_gdp.csv', index=False)