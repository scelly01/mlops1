import logging
import os
from datetime import datetime

logs_path = os.path.join(os.getcwd(), 'logs', f{"datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logging.basicConfig(
    filename = os.poth.join(logs_path, LOG_FILE)
    format = 
    level = 
)