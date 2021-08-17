from events.data_funcs import viirs_record_fetch
from help_scripts.global_funcs import get_home_dir
import logging
import os

# Path to directory
dir_path = get_home_dir()

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handling
file_handler = logging.FileHandler(os.path.join(dir_path, 'events.log'))
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)


# fetch new event data
def viirs_fetch_cron():
    # check data is received
    if viirs_record_fetch() and len(viirs_record_fetch()):
        logger.info("Data fetched successfully: ")
    else:
        logger.error('Could not process job')


if __name__ == "__main__":
    viirs_fetch_cron()
