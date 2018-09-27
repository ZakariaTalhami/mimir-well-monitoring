import logging

from Models.Well import Well
from Models.Reading import Reading

import logging.config

from Models.WellReading import WellReading

def init_logging():
    logging.config.fileConfig('logs//logger.conf', disable_existing_loggers=False)
    logging.info("-------------------------------------------------------- |")
    logging.info("-------           New Logging session            ------- |")
    logging.info("-------------------------------------------------------- |")

init_logging()
logging.getLogger(__name__).info("Hello")
well5 = Well(1, 2, 4)
print(well5)
reading5 = Reading(3, 25)
print(reading5)
wellReading = WellReading(well5 , 5)
print(wellReading)
