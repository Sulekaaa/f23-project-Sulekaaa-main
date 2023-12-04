from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

print("Imports complete")

# %%
# Authentication defaults to use the config file in the predefined location.
api = KaggleApi()
api.authenticate()

# Get the competitions list to test out the API.
competitions = api.competitions_list()
print(competitions)

# %%
dataset = 'adityaramachandran27/world-air-quality-index-by-city-and-coordinates'
out_path = 'datasets/AirQuality'

api.dataset_download_file(dataset, 'AQI and Lat Long of Countries.csv', out_path)
# %%

