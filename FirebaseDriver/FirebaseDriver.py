import logging

logger = logging.getLogger(__name__)


class CloudConnect:
    def __init__(self):
        logger.info("Init Cloud Connect")

    def save_well(self, well):
        logger.info("Persisting well to cloud")

        return True

    def read_well(self, well_id):
        logger.info("check database for well with id = {}".format(well_id))

        return True

    def read_all_wells(self):
        logger.info("Reading all the well data from firebase")
        well_list = []
        return well_list

    def save_reading(self, reading):
        logger.info("Saving Reading to Database")
        return True
