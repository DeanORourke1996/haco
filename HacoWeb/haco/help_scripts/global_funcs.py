# List of global functions which can be used across the project
# for various applications

# Get a BASE_DIR
def get_home_dir():
    from pathlib import Path
    base_dir = Path(__file__).resolve().parent.parent

    # Return a BASE_DIR
    return str(base_dir)


# Julian Date Function
def get_julian_date(date, **dateany):
    # Datetime functions
    import datetime
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
