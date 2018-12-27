import logging

logger = logging.getLogger(__name__)


class Well:
    """
        Well Class that contains Well UUID, water surface area and height of the well
    """
    def __init__(self, well_id, area, height , offset):
        logger.info("Init Well")
        logger.debug("init well({},{},{})".format(well_id,area,height))
        self.__well_id = well_id
        self.__area = area
        self.__height = height
        self.__offset = offset

    def __repr__(self):
        # logger.info("printing a Well")
        wellstr = "\nWell {0}:".format(self.get_well_id())
        wellstr += "\n\t water area = {0},".format(self.get_area())
        wellstr += "\n\t Well Height = {0}".format(self.get_height())
        wellstr += "\n\t Well Offset = {0},".format(self.get_offset())
        # logger.debug("\n" + wellstr)
        return wellstr

    def __str__(self):
        # logger.info("printing a Well")
        wellstr = "\nWell {0}:".format(self.get_well_id())
        wellstr += "\n\t water area = {0},".format(self.get_area())
        wellstr += "\n\t Well Height = {0},".format(self.get_height())
        wellstr += "\n\t Well Offset = {0}".format(self.get_offset())
        # logger.debug("\n" + wellstr)
        return wellstr

    def to_dict(self):
        """
            Return the object as a Dictionary excluding the well_id variable
        :return: Class instance as Dict
        """
        return {
            'Area': self.__area,
            'Height': self.__height,
            'Offset': self.__offset
        }

    def get_well_id(self):
        """
            Get the Well's UUID
        :return: UUID of the well
        """
        return self.__well_id

    def set_well_id(self, well_id):
        """
            Set the value of the UUID of the well
        :param well_id: new UUID of the well class
        """
        if isinstance(well_id, int):
            self.__well_id = well_id

    def get_area(self):
        """
            Get the water surface area of the well
        :return: well's water surface area
        """
        return self.__area

    def set_area(self, area):
        """
            Set the water surface area for the well
        :param area: new water surface area
        """
        if isinstance(area, float):
            self.__area = area

    def get_height(self):
        """
            Get the well's height
        :return: height of the well
        """
        return self.__height

    def set_height(self, height):
        """
            Set the height of the well
        :param height: new well's height
        """
        if isinstance(height, float):
            self.__height = height

    def get_offset(self):
        """
            Get the well's water offset
        :return: max water level offset from well's led
        """
        return self.__offset

    def set_height(self, offset):
        """
            Set the well's water offset
        :param offset: max water level offset from well's led
        """
        if isinstance(offset, float):
            self.__offset= offset

