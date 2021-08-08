# Use requests for NASA archives
import requests
import datetime
from help_scripts.global_funcs import get_julian_date, get_home_dir, get_nasa_key, dpd_lon
from django.db import connection
import pandas as pd


def reverse_geo():
    df_m_data = pd.read_csv(get_home_dir() + "/local_data/MODIS_C6_1_DATA_new.csv")
    df_v_data = pd.read_csv(get_home_dir() + "/local_data/VIIRS_C6_DATA_new.csv")


def geometa_fetch():
    url = "https://nrt3.modaps.eosdis.nasa.gov/api/v2/content/archives/geoMeta/61/AQUA/2018/MYD03_2018-04-17.txt"
    key = get_nasa_key()
    headers = {
        "Authorization": f"Bearer {key}"
    }

    r = requests.get(url, headers=headers)

    return r.text


# This function is for fetching most recent
# fire events from NASA/SUOMI VIIRS Satellites
def viirs_record_fetch():
    # Parameters for Request
    key = get_nasa_key()
    headers = {
        "Authorization": f"Bearer {key}"
    }

    url = "https://nrt3.modaps.eosdis.nasa.gov/api/v2/content/archives/FIRMS/noaa-20-viirs-c2/Global" \
          "/J1_VIIRS_C2_Global_VJ114IMGTDL_NRT_"
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    # Get today's julian date
    today_julian = get_julian_date(date)
    url += str(today_julian)
    url += ".txt"
    r = requests.get(url, headers=headers)

    write_to_local(r.text, "viirs")
    # Return data fetched
    return r.text


# This function is for fetching most recent
# fire events from NASA MODIS Satellites
def modis_record_fetch():
    # Parameters for Request
    key = get_nasa_key()
    headers = {
        "Authorization": f"Bearer {key}"
    }

    # MODIS Data Retrieval Entry Point
    url = "https://nrt3.modaps.eosdis.nasa.gov/api/v2/content" \
          "/archives/FIRMS/modis-c6.1/Global/MODIS_C6_1_Global_MCD14DL_NRT_"
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    # Get a Julian date
    today_julian = get_julian_date(date)  # MODIS only has data for the previous day's events
    url += str(today_julian)
    # Append .txt to string as formatted in archive
    url += str(".txt")
    r = requests.get(url, headers=headers)

    write_to_local(r.text, "modis")
    # Return data fetched
    return r.text


# Overwrites data in a local text file
def write_to_local(data, satellite):
    # what is the source of the data
    if satellite == "modis":
        # Function call to fetch new data
        file = get_home_dir()  # Get directory
        file += '/local_data/MODIS_C6_1_DATA_new.csv'  # Append new String to directory
        with open(file, mode='w+', ) as f:
            f.write(data)  # Write data to new file using Write mode which overwrites whatever is there already
    elif satellite == "viirs":
        # Function call to fetch new data
        file = get_home_dir()  # Get directory
        file += '/local_data/VIIRS_C6_DATA_new.csv'  # Append new String to directory
        with open(file, mode='w+', ) as f:
            f.write(data)  # Write data to new file using Write mode which overwrites whatever is there already


# To define a Wildfire event and
# to avoid duplicating multiple records with the same coordinates
# this will first check the records coordinates exist within the DB within a defined threshold.
# A threshold exists and is passable as a parameter to the function to allow it to be changed dynamically.
# The treshold (t) defines how much variance is permissable in the lon and lat coordinates for it to be considred
# a seperate event. There are no standards which really define this but it is practical to include such limitations
# on data being imported to avoid data redundancy and overpopulation of the database. Further, it allows events to
# be seperated from each other. The variance between a degree length of distance for longitude varies
# greatly as the latitude changes. The length of a degree of latitude does not differ much as the
# longitude changes and will be taken as the value of the length of a degree at the equator (69.172 miles)
def pre_db_process_data(event, *t):
    # Cast to floats for referential integrity
    lat = float(event[0].lat)
    lon = float(event[0].lon)

    # Define default thresholds
    try:
        if not t:
            # Default thresholds
            t = 0.3

        # Calculate Distance per Degree
        v_lon_dpd = dpd_lon(lat)  # Expects a latitude and returns a distance per degree (dpd) float val
        c_lat_dpd = 69.172  # Constant... distance per degree at the equator for lat

        # Calculate Threshold Markers
        lon_variance = (v_lon_dpd * t) / 100
        lat_variance = (c_lat_dpd * t) / 100

        # Open connection cursor
        with connection.cursor() as c:
            c.execute(
                'SELECT * '
                'FROM events_event '
                'WHERE lat BETWEEN (%s-%s)::float8 '
                'AND (%s+%s)::float8 '
                'AND lon BETWEEN (%s-%s)::float8 '
                'AND (%s+%s)::float8 '

                # Query Parameters
                , [lat, lat_variance, lat, lat_variance, lon,
                   lon_variance, lon, lon_variance]
            )
            # Grab next row
            row = c.fetchone()
            if row is None:
                return 1  # Row can be inserted
            else:
                return 0  # Don't insert

    except ValueError as e:
        raise ValueError(f'Value passed to fuction (dpd_lon()) invalid {e}')
