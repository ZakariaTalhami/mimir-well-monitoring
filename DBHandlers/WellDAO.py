import logging

from DBHandlers.DBDriver import DBDriver
from Models.Well import Well

logger = logging.getLogger(__name__)


# TODO  add a method to get  all the WELL IDS as a list
class WellDAO:
    """
        DAO for Well objects, handles all the data access (CRUD) of the well objects in the database
    """
    __tablename__ = Well.__name__

    def __init__(self):
        self.__db_driver = DBDriver()

    def save(self, well):
        """
            Persist the well instance to the database in the well table
        :param well: Well instance to be persisted
        :return:
        """
        logger.info("Saving Well to the database")
        logger.debug("saving: \n{}".format(well))
        success = True
        if isinstance(well, Well):
            try:
                self.well = well
                query = "INSERT INTO {}( id , area , height , offset)  VALUES(? , ? , ? , ?)".format(self.__tablename__)
                param = (self.well.get_well_id(), self.well.get_area(), self.well.get_height(), self.well.get_offset())
                self.__db_driver.insert(query, param)
            except:
                logger.error("Saving well to the database failed")
                success = False
        else:
            logging.error("Wrong value type for Well")
            success = False
        return success

    def read_all(self):
        """
            Read all the wells from the database
        :return: list of wells
        """
        logger.info("Reading all wells")
        try:
            query = "SELECT * FROM {}".format(self.__tablename__)
            result = self.__db_driver.query(query)
            logger.debug("Query result \n{}".format(result))
            well_list = []
            for entry in result:
                well_list.append(Well(entry[0], entry[1], entry[2], entry[3]))
            return well_list
        except:
            return False

    def read_by_id(self, select_id):
        """
            Reads from the database a well by its id
        :param select_id: UUID of the requested well
        :return: Well instance
        """
        try:
            logger.info("Selecting Well with id = {}".format(select_id))
            query = "SELECT * FROM {} WHERE id = {}".format(self.__tablename__, select_id)
            # TODO Check the size result before indexing
            entry = self.__db_driver.query(query)
            if len(entry) > 0:
                entry = entry[0]
            else:
                logger.info("Well not found in the database")
                return False
            logger.debug("Result: {}".format(entry))
            return Well(entry[0], entry[1], entry[2], entry[3])
        except:
            return False

    def get_well_id_list(self):
        """
            Read all the wells from the database, returning list of IDs only
        :return: list of well IDs
        """
        try:
            query = "SELECT id FROM {}".format(self.__tablename__)
            result = self.__db_driver.query(query)
            logger.debug("Query result \n{}".format(result))
            well_list = []
            for entry in result:
                well_list.append(entry[0])
            return well_list
        except:
            return False

    def update(self, well):
        """
            Update a well instance from the well table in the database
        :param well: New Well instance to be updated
        :return:
        """
        success = True
        if isinstance(well, Well):
            logger.info("Updating well with id = {}".format(well.get_well_id()))
            try:
                query = "UPDATE {} SET area = {} , height = {} , offset = {} WHERE id = {}".format(self.__tablename__,
                                                                                                   well.get_area(),
                                                                                                   well.get_height(),
                                                                                                   well.get_well_id(),
                                                                                                   well.get_offset())
                self.__db_driver.update(query)
            except:
                logger.error("Failed to update Well with id {}".format(well.get_well_id()))
                success = False
        else:
            success = False
        return success

    def delete(self, well_id):
        """
            Delete a Well specified by the passed well id
        :param well_id: UUID of the well to be deleted
        :return:
        """
        try:
            logger.info("Deleting Well with id = {}".format(well_id))
            query = "DELETE FROM {} WHERE id = {}".format(self.__tablename__, well_id)
            self.__db_driver.update(query)
        except:
            logger.error("Failed to delete well with id {}".format(well_id))
            return False
        return True
