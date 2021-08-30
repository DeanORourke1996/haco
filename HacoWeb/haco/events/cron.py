from events.load import load_data
from events.data_funcs import viirs_record_fetch
from help_scripts.global_funcs import get_home_dir
import kronos
import logging
import os

# Path to directory
dir_path = get_home_dir()

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handling
file_handler = logging.FileHandler(os.path.join(dir_path, '../events.log'))
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)


# Loader script for database updates
@kronos.register('*/10 */3 * * *')
def viirs_load_data():
    data = load_data(False, "viirs")
    if len(data):
        logger.info(f"Loaded data to database with return message: {data}")
    else:
        logger.error("Could not process job")


# fetch new event data
@kronos.register('0 */3 * * *')
def viirs_fetch_cron():
    # check data is received
    if viirs_record_fetch() and len(viirs_record_fetch()):
        logger.info("Data fetched successfully: ")
    else:
        logger.error('Could not process job')
