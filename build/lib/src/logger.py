import logging 
from datetime import datetime
import os

log_file = f"{datetime.now().strftime('%Y %m %d %H %M %S')}.log"

log_path = os.path.join(os.getcwd(), "logs", log_file)

os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, log_file)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s %(name)s %(message)s' 
)

