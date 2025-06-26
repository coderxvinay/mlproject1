##logger is for purpose that any execution that happens we should be able to log all the information, execution everything.
##To track if there is some error,even the custom exception error, that basically comes, we try to log that into the text file.

import logging 
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  ##log file format 
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)  ##giving path to log file (ie foldername = logs)
os.makedirs(logs_path,exist_ok=True)  ##even though there is a file, keep on appending

LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE)

##overwriting the functionality of logging by setting with basic config 
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

"""Wherever we use logging.INFO import logging and logging.INFO and print out any message, 
it'll create this file path and keep the particular format wrt the message"""


# if __name__ == "__main__":
#     logging.info("Checking if logging has started")