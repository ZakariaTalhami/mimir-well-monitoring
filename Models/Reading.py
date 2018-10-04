import logging

logger = logging.getLogger(__name__)


class Reading:
    def __init__(self, well_id, raw_data):
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
        return self.__well_id

    def get_raw_data(self):
        return self.__raw_data

    def set_well_id(self, well_id):
        if isinstance(well_id, int):
            self.__well_id = well_id
        else:
            logger.error("Invalid Well_id")
            logger.debug("{} is an invalid Well id ".format(well_id))
            raise ValueError

    def set_raw_data(self, raw_data):
        if isinstance(raw_data, float):
            self.__raw_data = raw_data
        else:
            logger.error("Invalid raw_data")
            logger.debug("{} is an invalid raw data ".format(raw_data))
            raise ValueError

