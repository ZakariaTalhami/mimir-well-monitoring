import logging

from Models import Well

logger = logging.getLogger(__name__)


class WellReading():
    def __init__(self, well, raw_data, reading_id=0, valume=0):
        logger.info("Init Well Reading")
        logger.debug("Init WellReading({},{})".format(well, raw_data))
        if isinstance(well, Well.Well):
            self.__well = well
        else:
            logger.error("Invalid well reference")
            logger.debug("{} is an invalid Well Reference".format(well))
            raise ValueError
        self.__level = raw_data
        self.__id = reading_id
        if valume == 0:
            self.__volume = self.calculate_volume(raw_data)
        else:
            self.__volume = valume

    def __str__(self):
        # logger.info("WellReading toString")
        reading = self.__well.__str__()
        reading += "\n\t Volume = {}".format(self.__volume)
        # logger.debug("\n" + reading)
        return reading

    def __repr__(self):
        # logger.info("WellReading toString")
        reading = self.__well.__str__()
        reading += "\n\t Volume = {}".format(self.__volume)
        # logger.debug("\n" + reading)
        return reading

    def calculate_volume(self, raw_data):
        logger.info("Calculating Volume")
        if isinstance(raw_data, float) or isinstance(raw_data, int):
            if raw_data > 0:
                return round(self.__well.get_area() * raw_data, 3)
        logger.error("Invalid raw data")
        logger.debug("{} is an invalid raw data");
        raise ValueError

    def get_well(self):
        return self.__well

    def get_volume(self):
        return self.__volume

    def set_volume(self, val):
        if isinstance(val, float):
            self.__volume = val

    def get_level(self):
        return self.__level

    def get_id(self):
        return self.__id
