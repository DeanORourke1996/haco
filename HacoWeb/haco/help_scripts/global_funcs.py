# List of global functions which will be used across the project
# for various applications
from pathlib import Path
import datetime
import math


# Get a BASE_DIR
def get_home_dir():
    base_dir = Path(__file__).resolve().parent.parent

    # Return a BASE_DIR
    return str(base_dir)


# Julian Date Function
def get_julian_date(date, **dateany):
    # Set format of time string
    fmt = '%Y-%m-%d'
    date = str(date)
    # Try - Except
    try:
        dt = datetime.datetime.strptime(date, fmt)
        # Format a Datetime Tuple
        tt = dt.timetuple()
        julian = int('%d%03d' % (tt.tm_year, tt.tm_yday))

        # Return Julian Date
        return julian

    except ValueError as e:
        raise ValueError(f'Incorrect data value passed to function parameter, could not complete request. {e}')


# Calculates and returns a relative longitudal threshold based on the latitude passed to the function
def dpd_lon(latitude):
    rads = math.radians(latitude)  # Convert decimal to radians
    cos_lon = math.cos(rads)  # Cosine of longitudal radians
    equator_degree_miles = 69.172  # One degree at the equator
    longitude_v = cos_lon * equator_degree_miles

    # Return the variable longitude
    return round(longitude_v, 3)


