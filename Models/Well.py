import logging

logger = logging.getLogger(__name__)


class Well:
    def __init__(self, well_id, area, height):
        logger.info("Init Well")
        logger.debug("init well({},{},{})".format(well_id,area,height))
        self.__well_id = well_id
        self.__area = area
        self.__height = height

    def __repr__(self):
        # logger.info("printing a Well")
        wellstr = "Well {0}:".format(self.get_well_id())
        wellstr += "\n\t water area = {0},".format(self.get_area())
        wellstr += "\n\t Well Height = {0}.".format(self.get_height())
        # logger.debug("\n" + wellstr)
        return wellstr

    def __str__(self):
        logger.info("printing a Well")
        wellstr = "Well {0}:".format(self.get_well_id())
        wellstr += "\n\t water area = {0},".format(self.get_area())
        wellstr += "\n\t Well Height = {0}.".format(self.get_height())
        logger.debug("\n" + wellstr)
        return wellstr

    def get_well_id(self):
        return self.__well_id

    def set_well_id(self, well_id):
        if isinstance(well_id, int):
            self.__well_id = well_id

    def get_area(self):
        return self.__area

    def set_area(self, area):
        if isinstance(area, float):
            self.__area = area

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if isinstance(height, float):
            self.__height = height
