
import logging
import os
from datetime import datetime



log_path = os.path.join(os.getcwd(), "logs")
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

os.makedirs(log_path, exist_ok=True)

os.path.join(log_path, LOG_FILE)
log_filepath = os.path.join(log_path, LOG_FILE)


logging.basicConfig(
    level=logging.INFO,
    filename=log_filepath, 
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",

)

