import csv
from events.models import Event
from help_scripts.global_funcs import get_home_dir
from events.data_funcs import pre_db_process_data


# Load in data to DB from the local CSV file
def load_data(hard, mode):
    file = ""
    if mode == "modis":
        # Set filepath
        file = get_home_dir() + '/local_data/MODIS_C6_1_DATA_new.csv'
    elif mode == "viirs":
        # Set filepath
        file = get_home_dir() + '/local_data/VIIRS_C6_DATA_new.csv'
    count_inserts = 0
    with open(file) as f:
        reader = csv.reader(f)
        next(reader, None)
        for record in reader:
            event = Event.objects.get_or_create(
                lat=record[0],
                lon=record[1],
                bright_ti4=record[2],
                scan=record[3],
                track=record[4],
                acq_date=record[5],
                acq_time=record[6],
                satellite=record[7],
                confidence=record[8],
                version=record[9],
                bright_ti5=record[10],
                frp=record[11],
                daynight=record[12],
                resolution=mode
            )
            if not hard:
                chk_insert = pre_db_process_data(event)  # Check the record for duplication
                # Calls to a function which executes an SQL query via a cursor which
                # will determine if the record is redundant or should be inserted
                if chk_insert:
                    event[0].save()
                    count_inserts += 1  # Increment total records inserted
                else:
                    event[0].delete()
                    next(reader, None)  # Skip this record, need not be inserted to DB
            else:
                event[0].save()
                count_inserts += 1

    # Confirm function ran, records were/not inserted
    return f"Load data ran succesfully. {str(count_inserts)} records were inserted."

# Initial Load
# Called from the Python Console

