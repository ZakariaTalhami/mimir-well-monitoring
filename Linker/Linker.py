import logging
from pprint import pformat

from DBHandlers.WellDAO import WellDAO
from DBHandlers.WellReadingDAO import WellReadingDAO
from FirebaseDriver.FirebaseDriver import CloudConnect
from Models.Reading import Reading
from Models.WellReading import WellReading

logger = logging.getLogger(__name__)


class Linker:
    """
        The linker class, links between Readings coming from the I2C module and the Well information stored in
        the database.
    """
    def __init__(self):
        """
            Construct the linker class, initiates the WellReadingDAO, WellDAO and the firebase cloud connection
        """
        logger.info("Init Linker")
        self.__wellreadingdao = WellReadingDAO()
        self.__welldao = WellDAO()
        self.__firebase = CloudConnect()

    def link_and_persist(self, readings):
        """
            Links the readings with the well classes stored in the database, creating a WellReading object.
            This object is then persisted to the forebase database in the cloud, if cloud persistence fails, the readings
            are then persisted to the local database temporarily.

            1. Check if passed reading is instance of Reading or a list of readings, raise ValueError if not.
            2. Convert the Readings into WellReadings by linking them to well instances
            3. Attempt to persist to the firebase database
            4. if fails persist to the local database
        :param readings: individual reading or a list of readings
        :return:
        """
        logger.info("preparing to link and persist")
        logger.debug("linking and persisting:> \n {}".format(pformat(readings)))
        target_list = []

        # Convert Stage
        if isinstance(readings, Reading):
            target_list.append(self.convert_reading_to_well_reading(readings))

        elif isinstance(readings, list) and all([isinstance(x, Reading) for x in readings]):
            for entry in readings:
                target_list.append(self.convert_reading_to_well_reading(entry))
        else:
            raise ValueError

        logger.debug("Converted Well Readings:>")
        logger.debug("\n{}".format(pformat(target_list)))

        # Persist Readings
        for entry in target_list:
            if not self.__firebase.save_reading(entry):
                logger.info("failed to persist to firebase database")
                self.__wellreadingdao.save(entry)

    def convert_reading_to_well_reading(self, reading):
        """
            Convert a reading instance to a WellReading instance

            1. Read from database a well depending on the well_id in the reading instance
            2. Construct WellReading by passing the well and water level from the reading instance
        :param reading: a reading instance
        :return: WellReading instance
        :raises ValueError if the reading is not instance Reading class
        """
        if not isinstance(reading, Reading):
            raise ValueError

        logger.debug("Converting {}".format(reading))
        # have to change Reading class to include UID
        well_uuid = reading.get_well_id()  # What happens if the UUID is not found in the DB
        source_well = self.__welldao.read_by_id(well_uuid)
        logger.debug("Retrieved Well information")
        target = WellReading(source_well, reading.get_raw_data())
        logger.debug("\n{}".format(target))

        return target


if __name__ == "__main__":
    myLinker = Linker()
    meReading = Reading(24 , 25.363)
    myLinker.link_and_persist(meReading)