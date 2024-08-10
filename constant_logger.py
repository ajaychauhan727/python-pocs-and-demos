import time
import datetime
import logging

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a console handler and set its level to INFO
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Create a formatter and set it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)


while True:
    logger.info(f"time ==========> {datetime.datetime.now()}")
    time.sleep(3)
