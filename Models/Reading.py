import logging

logger = logging.getLogger(__name__)


class Reading:
    """
        This is a Raw Reading class that is produced from the I2C module, it contains
        the ID of the well and the measured water level
    """
    def __init__(self, well_id, raw_data):
        """
            Constructor for Reading Class, where it takes the Well id and water level as the raw_data
        :param well_id:  UUID of the measured well
        :param raw_data: The measured water level
        """
        logger.info("Init Reading")
        logger.debug("Init Reading( {} ,{} )".format(well_id, raw_data))
        self.__well_id = well_id
        self.__raw_data = raw_data

    def __str__(self):
        # logger.info("Reading toString")
        reading = "Reading:> \n"
        reading += "\t Well ID  = {}\n".format(self.get_well_id())
        reading += "\t Raw data = {}\n".format(self.get_raw_data())
        # logger.debug("\n"+reading)
        return reading

    def __repr__(self):
        return self.__str__()

    def get_well_id(self):
        """
            Get the UUID of the measured well
        :return: well UUID of the Reading
        """
        return self.__well_id

    def get_raw_data(self):
        """
            Get the water level reading
        :return: water level measured
        """
        return self.__raw_data

    def set_well_id(self, well_id):
        """
            Set the UUID of the reading
        :param well_id: UUID of a well
        :raise: ValueError if the well_id is not Int
        """
        if isinstance(well_id, int):
            self.__well_id = well_id
        else:
            logger.error("Invalid Well_id")
            logger.debug("{} is an invalid Well id ".format(well_id))
            raise ValueError

    def set_raw_data(self, raw_data):
        """
            Set the water level reading
        :param raw_data: Water level
        :raise: ValueError if the water level passed is not float
        """
        if isinstance(raw_data, float):
            self.__raw_data = raw_data
        else:
            logger.error("Invalid raw_data")
            logger.debug("{} is an invalid raw data ".format(raw_data))
            raise ValueError

