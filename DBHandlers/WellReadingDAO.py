import logging
from DBHandlers.DBDriver import db_driver
from DBHandlers.WellDAO import WellDAO
from Models.Well import Well
from Models.WellReading import WellReading

logger = logging.getLogger(__name__)


class WellReadingDAO:
    """
        DAO for WellReading objects, handles all the data access (CRUD) of the wellReading objects in the database
    """
    __tablename__ = WellReading.__name__

    def save(self, reading):
        """
            Persist the wellReading instance to the database in the reading table
        :param well: WellReading instance to be persisted
        :return:
        """
        logger.info("Saving Well Reading to the database")
        logger.debug("saving: \n{}".format(reading))
        if isinstance(reading, WellReading):
            self.reading = reading
            if reading.get_id():
                query = "INSERT INTO {}( id, well_id , level , volume, time)  VALUES(? , ? , ? , ? , ?)".format(
                    self.__tablename__)
                param = (self.reading.get_id(), self.reading.get_well().get_well_id(), self.reading.get_level(),
                         self.reading.get_volume(),
                         self.reading.get_timestamp())
            else:
                query = "INSERT INTO {}( well_id , level , volume , time)  VALUES( ? , ? , ? , ?)".format(
                    self.__tablename__)
                param = (self.reading.get_well().get_well_id(), self.reading.get_level(), self.reading.get_volume(),
                         self.reading.get_timestamp())

            db_driver.insert(query, param)
        else:
            raise ValueError

    def read_all(self):
        """
            Read all the wellReadings from the database
        :return: list of wellReadings
        """
        logger.info("Reading all Well Readings")
        query = "SELECT * FROM {0} " \
                "INNER JOIN {1} ON {0}.well_id = {1}.id".format(self.__tablename__, WellDAO.__tablename__)
        result = db_driver.query(query)
        logger.debug("Query result \n{}".format(result))
        reading_list = []
        for entry in result:
            well = Well(entry["well_id"], entry["area"], entry["height"])
            reading_list.append(WellReading(well, entry["level"], entry["time"], entry["id"], entry["volume"]))
        return reading_list

    def read_by_id(self, select_id):
        """
            Reads from the database a wellReading by its id
        :param select_id: UUID of the requested reading
        :return: WellReadings instance
        """
        logger.info("Selecting Well Reading with id = {}".format(select_id))
        query = "SELECT * FROM {0} " \
                "INNER JOIN {1} ON {0}.well_id = {1}.id " \
                "where {0}.id = {2}".format(self.__tablename__, WellDAO.__tablename__, select_id)
        entry = db_driver.query(query)[0]
        logger.debug("Result: {}".format(entry))
        well = Well(entry["well_id"], entry["area"], entry["height"])
        return WellReading(well, entry["level"], entry["time"], entry["id"], entry["volume"])

    def update(self, reading):
        """
            Update a wellReading instance from the reading table in the database
        :param well: New WellReading instance to be updated
        :return:
        """
        if isinstance(reading, WellReading):
            logger.info("Updating reading with id = {}".format(reading.get_id()))
            query = "UPDATE {} SET well_id = {} ," \
                    " level = {}," \
                    " volume = {} " \
                    " WHERE id = {}".format(self.__tablename__,
                                            reading.get_well().get_well_id(),
                                            reading.get_level(),
                                            reading.get_volume(),
                                            reading.get_id())
            db_driver.update(query)
        else:
            raise ValueError

    def delete(self, reading_id):
        """
            Delete a WellReading specified by the passed wellReading id
        :param well_id: ID of the wellReading to be deleted
        :return:
        """
        logger.info("Deleting Reading with id = {}".format(reading_id))
        query = "DELETE FROM {} WHERE id = {}".format(self.__tablename__, reading_id)
        db_driver.update(query)
