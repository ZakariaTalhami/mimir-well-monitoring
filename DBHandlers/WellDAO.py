import logging

from DBHandlers.DBDriver import db_driver
from Models.Well import Well

logger = logging.getLogger(__name__)


class WellDAO:
    __tablename__ = Well.__name__

    def save(self, well):
        logger.info("Saving Well to the database")
        logger.debug("saving: \n{}".format(well))
        if isinstance(well, Well):
            self.well = well
            query = "INSERT INTO {}( id , area , height)  VALUES(? , ? , ?)".format(self.__tablename__)
            param = (self.well.get_well_id(), self.well.get_area(), self.well.get_height())
            db_driver.insert(query, param)
        else:
            raise ValueError

    def read_all(self):
        logger.info("Reading all wells")
        query = "SELECT * FROM {}".format(self.__tablename__)
        result = db_driver.query(query)
        logger.debug("Query result \n{}".format(result))
        well_list = []
        for entry in result:
            well_list.append(Well(entry[0], entry[1], entry[2]))
        return well_list

    def read_by_id(self, select_id):
        logger.info("Selecting Well with id = {}".format(select_id))
        query = "SELECT * FROM {} WHERE id = {}".format(self.__tablename__, select_id)
        entry = db_driver.query(query)[0]
        logger.debug("Result: {}".format(entry))
        return Well(entry[0], entry[1], entry[2])

    def update(self, well):
        if isinstance(well, Well):
            logger.info("Updating well with id = {}".format(well.get_well_id()))
            query = "UPDATE {} SET area = {} , height = {} WHERE id = {}".format(self.__tablename__, well.get_area(),
                                                                                 well.get_height(), well.get_well_id())
            db_driver.update(query)
        else:
            raise ValueError

    def delete(self, well_id):
        logger.info("Deleting Well with id = {}".format(well_id))
        query = "DELETE FROM {} WHERE id = {}".format(self.__tablename__, well_id)
        db_driver.update(query)
