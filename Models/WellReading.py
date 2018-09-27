import logging

from Models import Well

logger = logging.getLogger(__name__)


class WellReading():
    def __init__(self, well, raw_data):
        logger.info("Init Well Reading")
        logger.debug("Init WellReading({},{})".format(well,raw_data))
        if isinstance(well, Well.Well):
            self.__well = well
        else:
            logger.error("Invalid well reference")
            logger.debug("{} is an invalid Well Reference".format(well))
            raise ValueError
        self.__volume = self.calculate_volume(raw_data)

    def calculate_volume(self, raw_data):
        logger.info("Calculating Volume")
        if isinstance(raw_data, float) or isinstance(raw_data,int):
            if raw_data > 0:
                return self.__well.get_area() * raw_data
        logger.error("Invalid raw data")
        logger.debug("{} is an invalid raw data");
        raise ValueError

    def get_well(self):
        return self.__well

    def __str__(self):
        logger.info("WellReading toString")
        reading = self.__well.__str__()
        reading += "\n\t Volume = {}".format(self.__volume)
        logger.debug("\n"+reading)
        return reading

    def get_volume(self):
        return self.__volume
