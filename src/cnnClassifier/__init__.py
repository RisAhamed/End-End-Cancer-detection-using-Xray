import os
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = 'logs'
log_filepath= os.path.join(log_dir,"running_logs")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath, mode='w', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)  # log to stdout as well
    ]
)

logger = logging.getLogger("cnnClassifier")
