[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12502411&assignment_repo_type=AssignmentRepo)
# CSCI 422 Project: Impact of COVID-19 on Employment- Suleka Abdi


## Overview
In this project, we're studying how the COVID-19 pandemic affected employment focusing on unemployment rates and changes in household income. We'll use data from the BLS Labor Force Statistics dataset and the American Community Survey (ACS) DP03 table to answer some essential questions about the pandemic's impact on the job market. 

Our first goal is to track how the overall unemployment rate changed during the pandemic. We want to pinpoint when it increased or decreased significantly, helping us understand the pandemic's economic impact better. We'll also be looking at how different groups of people were affected. We want to know if specific age groups, genders, or racial backgrounds experienced more significant changes in their unemployment rates during the pandemic. Another part of our study will involve comparing unemployment rates across different states and regions. We want to identify which places had the highest and lowest unemployment rates when the pandemic hit its peak. This comparison could give us insights into regional differences. Lastly, we'll be paying special attention to how the pandemic affected women's unemployment rates. We'll see if women faced unique challenges in the job market during the pandemic.

The other goal is to analyze any significant shifts and trends in household income levels by comparing the median household income before and after the COVID-19 pandemic.

By answering these questions and analyzing the data, we hope to gain a deeper understanding of how the COVID-19 pandemic affected employment. This insight will help us see how different groups and regions fared during these challenging times.

#### Data sources
The two data sources used will be Bureau of Labor Statistics (BLS) Labor Force Statistics dataset and the American Community Survey (ACS) DP03 table: Selected Economic characteristics.

## Ingestion


#### Where does the data come from?
  1. Census Bureau API (https://api.census.gov/data/2022/acs/acs1/cprofile). This API provides data related to the American Community Survey.
  2. The Bureau of Labor Statistics (BLS) API (https://api.bls.gov/publicAPI/v2/timeseries/data/). The BLS API offers various economic and labor-related data.
     
#### How is it injested?
  1. Census data: data ingestion is done through an HTTP GET request to the Census Bureau API. The script specifies the parameters for the data query, and the response is processed as JSON.
  2. BLS data: data ingestion is performed through an HTTP POST request to the BLS API. The script constructs the data payload with specific parameters and makes the request. The response is processed as JSON.

#### Where is it Stored?
  1.  Census data is stored in a JSON file named "census_data.json" on the local file system.
  2.  BLS data is stored in a CSV file named "bls_data.csv" on the local file system.
     After the data is stored locally, it is uploaded to Azure Data Lake Storage (ADLS) and stored in the "assign1-2" file system within the "sulekastore"  storage account. 
