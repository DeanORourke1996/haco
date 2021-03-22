import csv
from events.models import Event
from help_scripts.global_funcs import get_home_dir

# Set filepath
file = get_home_dir() + '/hot_data/VIIRS_DATA_new.csv'


# Load in data to DB
def load_data():
    with open(file) as f:
        reader = csv.reader(f)
        next(reader, None)
        for rec in reader:
            inserted = Event.objects.get_or_create(
                lat=rec[1],
                lon=rec[2],
                bright_ti4=rec[3],
                scan=rec[4],
                track=rec[5],
                acq_date=rec[6],
                acq_time=rec[7],
                satellite=rec[8],
                confidence=rec[9],
                version=rec[10],
                bright_ti5=rec[11],
                frp=rec[12],
                daynight=rec[13]
            )

# Initial Load
# Called from the Python Console

# load_data()
