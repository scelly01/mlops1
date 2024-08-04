import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.mkdir(logs_path, exist_ok=True)

logging.basicConfig(
    filename = os.poth.join(logs_path, LOG_FILE)
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %()"
    level = logging.INFO
)