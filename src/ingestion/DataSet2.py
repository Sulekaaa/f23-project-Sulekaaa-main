import json
import requests

# Defining the Census Bureau API endpoint
url = "https://api.census.gov/data/2022/acs/acs1/cprofile"

# Defining the parameters for your data query
params = {
    "get": "group(CP03)",
    "for": "metropolitan statistical area/micropolitan statistical area:*",
}

# Making the API request
response = requests.get(url, params=params)

# Checking if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extracting column names and data
    columns = data[0]
    rows = data[1:]

    # Creating a list of dictionaries with column names as keys and data as values
    dataset = [dict(zip(columns, row)) for row in rows]

    # Replacing '*' and empty spaces with 'null' in the dataset
    for row in dataset:
        for key, value in row.items():
            if value == '*':
                row[key] = 'null'
            elif value is not None and value.strip() == ' ':
                row[key] = 'null'
            elif value is None:
                row[key] = 'null'

    # Defining the JSON file name
    json_file = "census_data.json"

    # Writ the dataset to a JSON file
    with open(json_file, "w") as jsonfile:
        json.dump(dataset, jsonfile)

    print(f"Census data saved to {json_file}")
else:
    print(f"API request failed with status code: {response.status_code}")
