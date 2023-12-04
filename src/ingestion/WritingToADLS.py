# - script to extract data from DataSet1.py and loading into ADLS.

# - script to extract data from DataSet1.py and loading into ADLS.

import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient

# This Method connects to a storage account with an account key.
def initialize_storage_account(storage_account_name, storage_account_key):
    global service_client
    try:
        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
    except Exception as e:
        print(e)

# My Azure Data Lake Storage account details
storage_account_name = "sulekastore"

# Storing key in a config file that is NOT checked in.
# Use .gitignore to avoid accidental submission.
with open("AccountKey.config") as f:
    storage_account_key=f.readline()

# Initializing the Azure Data Lake Storage account
initialize_storage_account(storage_account_name, storage_account_key)

# Creating a container and a directory
file_system_client = service_client.create_file_system(file_system="assign1-2")
directory_client = file_system_client.create_directory("bls_data")
directory_client2 = file_system_client.create_directory("census_data")

# Uploading the data files
data_file_name = "bls_data.csv"
data_file_name2 = "census_data.json"
directory_client = file_system_client.get_directory_client("bls_data")
directory_client2 = file_system_client.get_directory_client("census_data.json")
file_client = directory_client.create_file(data_file_name)
file_client2 = directory_client2.create_file(data_file_name2)
# Reading the data from the file
with open(data_file_name, 'r') as file:
    file_contents = file.read()

with open(data_file_name2, 'r') as file:
    file_contents2 = file.read()

# Uploading the data to Azure Data Lake Storage
file_client.upload_data(file_contents, overwrite=True)
file_client2.upload_data(file_contents2, overwrite=True)
print(f'Data has been uploaded to ADLS: {data_file_name, data_file_name2}')
