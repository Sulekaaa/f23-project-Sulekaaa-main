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
dataset = 'nelgiriyewithana/global-weather-repository'
out_path = 'datasets/GlobalWeatherRepository'

api.dataset_download_file(dataset, 'GlobalWeatherRepository.csv', out_path)
# %%



