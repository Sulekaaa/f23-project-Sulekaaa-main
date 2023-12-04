# DataSet1.py - script to extract data from its source and load into ADLS.

import json
from datetime import datetime
import pandas as pd
import requests

# Setting my BLS API parameters
headers = {'Content-type': 'application/json'}
series_id = ['LNS12000000']  # I'm using the single desired series ID
start_year = "2021"
end_year = "2023"
api_key = "a3224166286c4c84a6d152d08f251fc5"  # I'm using my BLS API key

# Constructing the data payload for my API request
data = {
    "seriesid": series_id,
    "startyear": start_year,
    "endyear": end_year,
    "registrationKey": api_key
}
data = json.dumps(data)

# Making the API request to BLS
response = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(response.text)

# Extracting the relevant data and formatting it into a DataFrame
data_list = []

for series in json_data['Results']['series']:
    for item in series['data']:
        year = item['year']
        period = item['period']
        periodName = item['periodName']

        # Converting the full month name to an abbreviated month name (first 3 letters)
        month_abbreviation = datetime.strptime(periodName, "%B").strftime("%b")

        label = f"{year} {month_abbreviation}"  # Create Label as a combination of Year and Month
        value = item['value']

        if 'M01' <= period <= 'M12':
            data_list.append([year, period, label, value])

# Creating a Pandas DataFrame to store the data
df = pd.DataFrame(data_list, columns=['Year', 'Period', 'Label', 'Value'])

# Sorting the data by the 'Year' column
df = df.sort_values(by='Year')

# Resetting the index and remove the index name
df = df.reset_index(drop=True)
df.index.name = None

# Saving the data to a CSV file
csv_filename = 'bls_data.csv'
df.to_csv(csv_filename, index=False)

print("bls_data has been saved into a csv file")