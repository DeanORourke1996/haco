from events.load import load_data
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


# Loader script for database updates
def viirs_load_data():
    data = load_data(False, "viirs")
    if len(data):
        logger.info(f"Fetched data with return message: {data}")
    else:
        logger.error("Could not process job")


