import logging
from datetime import datetime

from Models import Well

logger = logging.getLogger(__name__)


class WellReading():
    """
        Well Reading class takes the dimension from the well class and the water level measurement from
        the Reading class and calculates the volume
    """

    def __init__(self, well, raw_data, timestamp, reading_id=0, volume=0):
        """
            Constructor of the Well Reading class, takes well class and water level measurement and calculates
            volume. Optionally, if a volume value is passed the volume calculation is passed.

            1. Make sure well parameter is of Well Class, if not raise ValueError
            2. Check if volume is provided
            3. If provided set volume to the provided value
            3. If not provided Calculate information using surface area of the well and the water level reading
        :param well: Well class containing the well information
        :param raw_data: Water level reading from a Reading class
        :param reading_id: optional Well reading id, used in reconstructing from the database
        :param volume: optional reading volume, used in reconstructing from the database
        :raises valueError if passed well is not of well class
        """
        logger.info("Init Well Reading")
        logger.debug("Init WellReading({},{} , {} )".format(well, raw_data, timestamp))
        if isinstance(well, Well.Well):
            self.__well = well
        else:
            logger.error("Invalid well reference")
            logger.debug("{} is an invalid Well Reference".format(well))
            raise ValueError
        self.__level = self.__well.get_height() - raw_data + self.__well.get_offset()
        if self.__level < 0:
            self.__level = 0
        self.__id = reading_id
        self.__timestamp = timestamp
        if volume == 0:
            self.__volume = self.calculate_volume(self.__level)
        else:
            self.__volume = volume

    def __str__(self):
        # logger.info("WellReading toString")
        reading = self.__well.__str__()
        reading += "\n\t Volume = {}".format(self.__volume)
        reading += "\n\t Timestamp = {}".format(self.__timestamp)
        # logger.debug("\n" + reading)
        return reading

    def __repr__(self):
        # logger.info("WellReading toString")
        reading = self.__well.__str__()
        reading += "\n\t Volume = {}".format(self.__volume)
        reading += "\n\t Timestamp = {}".format(self.__timestamp)
        # logger.debug("\n" + reading)
        return reading

    def to_dict(self):
        """
            Return the object as a Dictionary
        :return: Class instance as Dict
        """
        return {
            "Level": self.__level,
            "Volume": self.__volume,
            #"Timestamp": datetime.strptime(self.__timestamp , "%Y-%m-%d %H:%M:%S.%f")
            "Timestamp": self.__timestamp
        }

    def calculate_volume(self, level):
        """
            Calculate the volume of a well, using the water level passed and the well information stored in the class

            1. Check if the raw data is a float or int and a positive value, if not raise ValueError
            2. Extract Well surface area
            3. Calculate volume = surface area * measured water level
        :param level: water level
        :return: water volume in the well
        :raises ValueError if the passed value is not float or int
        """
        logger.info("Calculating Volume")
        if isinstance(level, float) or isinstance(level, int):
            if level > 0:
                return round(self.__well.get_area() * level, 3)
            else:
                return 0
        logger.error("Invalid raw data")
        logger.debug("{} is an invalid raw data");
        raise ValueError

    def get_well(self):
        """
            Get the class of the measured well
        :return: measured well
        """
        return self.__well

    def get_volume(self):
        """
            get the calculated volume of the Reading
        :return: volume in the well
        """
        return self.__volume

    def set_volume(self, val):
        """
            Set the Volume in the well
        :param val: new water volume in the well
        :raises ValueError if the passed volume isnt a float
        """
        if isinstance(val, float):
            self.__volume = val

    def get_level(self):
        """
            Get the measured water level
        :return: water level
        """
        return self.__level

    def get_id(self):
        """
            get the id of the well reading
        :return: WellReading id
        """
        return self.__id

    def get_timestamp(self):
        """
            get timestamp of the moment of reading
        :return: reading timestamp
        """
        return self.__timestamp

    def set_timestamp(self, timestanmp):
        """
            set the moment of reading from the well
        :param timestanmp: new timestmap value
        """
        if isinstance(timestanmp, datetime):
            self.__timestamp = timestanmp
        else:
            raise ValueError
