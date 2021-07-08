import csv
from events.models import Event
from help_scripts.global_funcs import get_home_dir
from events.data_funcs import pre_db_process_data

# Set filepath
file = get_home_dir() + '/data/MODIS_C6_DATA_new.csv'


# Load in data to DB from the local CSV file
def load_data(hard):
    count_inserts = 0
    with open(file) as f:
        reader = csv.reader(f)
        next(reader, None)
        for record in reader:
            event = Event.objects.get_or_create(
                lat=record[1],
                lon=record[2],
                bright_ti4=record[3],
                scan=record[4],
                track=record[5],
                acq_date=record[6],
                acq_time=record[7],
                satellite=record[8],
                confidence=record[9],
                version=record[10],
                bright_ti5=record[11],
                frp=record[12],
                daynight=record[13]
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

