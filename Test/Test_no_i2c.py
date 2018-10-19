# Set delay intervel 
# Open the CSV file
# Make a CSV reader
# Read row by row
# Convert Row to Reading Class
# Pass reading to the linker
# delay between rows. delay = [int(0.8*delay) , int(1.2*delay)]
import csv
import logging
from pathlib import Path

from Linker.Linker import Linker
from Models.Reading import Reading

logger = logging.getLogger(__name__)

# TODO document me NOW!
class TestNoI2C:
    __delay = 1

    def __init__(self, delay, file):
        logger.info("Init Test_no_i2c")
        self.__file = Path(__file__).parent / file
        if isinstance(delay, int):
            self.__minDelay = int(0.8 * delay)
            self.__maxDelay = int(1.2 * delay)
            self.__linker = Linker()
            logger.info("Test delay was set to = {}".format(str(delay)))

    def run(self):
        try:
            with open(self.__file, "r") as infile:
                fieldnames = ["UUID", "raw", "timestamp"]
                reader = csv.DictReader(infile, fieldnames)
                for row in reader:
                    reading = Reading(int(row["UUID"]), float(row["raw"]) , row["timestamp"])
                    ret = self.__linker.link_and_persist(reading)
                    # assert ret == True
        except FileNotFoundError:
            logger.error("CSV File not found")
            return


if __name__ == "__main__":
    logger.info(__name__)
