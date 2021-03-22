# Use requests for NASA archives
import requests
import datetime
import csv
import pandas as pd
from help_scripts.global_funcs import get_julian_date, get_home_dir


# This function is for fetching most recent
# fire events from NASA MODIS Satellite
def modis_record_fetch():
    # Get the path
    file = get_home_dir()  # BASE DIR
    file += '/nasa_app_bearer.txt'  # Append key

    # Parameters for Request
    key = open(file, "r").read()  # Key Excluded from GIT
    headers = {
        "Authorization": f"Bearer {key}"
    }

    # MODIS Data Retrieval Entry Point
    url = "https://nrt3.modaps.eosdis.nasa.gov/api/v2/content" \
          "/archives/FIRMS/c6/Global/MODIS_C6_Global_MCD14DL_NRT_"
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    # Get a Julian date
    today_julian = get_julian_date(date)
    url += str(today_julian)
    # Append .txt to string as formatted in archive
    url += str(".txt")
    r = requests.get(url, headers=headers)

    # Return data fetched
    return r.text


# Overwrites data in a local text file
def write_data(data):
    # Function call to fetch new data
    file = get_home_dir()  # Get directory
    file += '/hot_data/VIIRS_DATA_new.txt'  # Append new String to directory
    with open(file, mode='w',) as f:
        f.write(data)  # Write data to new file using Write mode which overwrites whatever there already
    data_to_csv()


# Simple Conversion Function to_csv using Pandas
def data_to_csv():
    file = get_home_dir()
    file += '/hot_data/VIIRS_DATA_new.txt'
    data = pd.read_csv(file)
    file = get_home_dir() + "/hot_data/VIIRS_DATA_new.csv"
    data.to_csv(file, mode='w')


