import csv
from events.models import Event
from help_scripts.global_funcs import get_home_dir
from events.data_funcs import pre_db_process_data

# Set filepath
file = get_home_dir() + '/hot_data/VIIRS_DATA_new.csv'


# Load in data to DB
def load_data():
    with open(file) as f:
        reader = csv.reader(f)
        next(reader, None)
        for event in reader:
            pre_db_process_data(event)

            inserted = Event.objects.get_or_create(
                lat=event[1],
                lon=event[2],
                bright_ti4=event[3],
                scan=event[4],
                track=event[5],
                acq_date=event[6],
                acq_time=event[7],
                satellite=event[8],
                confidence=event[9],
                version=event[10],
                bright_ti5=event[11],
                frp=event[12],
                daynight=event[13]
            )
            inserted.save()  # Save each record

# Initial Load
# Called from the Python Console

# load_data()
