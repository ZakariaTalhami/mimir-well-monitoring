import logging
import threading
import time

from DBHandlers.WellReadingDAO import WellReadingDAO
from FirebaseDriver.FirebaseDriver import CloudConnect

logger = logging.getLogger(__name__);


class ReadingSynch(threading.Thread):
    def __init__(self):
        logger.info("Initiating ReadingSynch")
        threading.Thread.__init__(self)
        self.__SHORT_SLEEP = 60
        self.__LONG_SLEEP = 300

    def run(self):
        logger.info("Starting ReadingSynch")
        self.__wellReadingDao = WellReadingDAO()
        self.__conn = CloudConnect()
        time.sleep(10)
        while True:
            # Read from the local Database
            buffer = []
            toDelete = []
            readings = self.__wellReadingDao.read_all()
            if len(readings) > 0:
                for reading in readings:
                    if self.__conn.save_reading(reading):
                        toDelete.append(reading)
                    else:
                        buffer.append(reading)

                if len(toDelete) > 0:
                    id_list = [reading.get_id() for reading in toDelete]
                    self.__wellReadingDao.delete_list(id_list)

            if len(buffer) > 0:
                logger.debug("ReadingSynch taking a SHORT SLEEP")
                time.sleep(self.__SHORT_SLEEP)
            else:
                logger.debug("ReadingSynch taking a LONG SLEEP")
                time.sleep(self.__LONG_SLEEP)
