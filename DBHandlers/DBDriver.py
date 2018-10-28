import sqlite3

import logging

from Models.Well import Well
from Models.WellReading import WellReading

logger = logging.getLogger(__name__)


# Might need to add some Try blocks for the execute

class DBDriver:
    """

    """
    def __init__(self):
        self.__conn = sqlite3.connect("gateway.db")
        self.__conn.row_factory = sqlite3.Row
        self.__conn.set_trace_callback(logger.info)
        self.__cursor = self.__conn.cursor()
        #self.maintain_well_table()
        #self.maintain_reading_table()

    def __del__(self):
        self.close_connection()

    def create_table(self, table_name, **kwargs):
        """
        Creates a table in the database if it doesnt exists, if it does exists then does notion.
        The Method takes desired name of the table and a dictionary of the columns.
        :param table_name: Name of the table
        :param kwargs: Dict of columns, with the key as the name of the column and the value as the type
        :return:
        """
        logger.info("Initializing {} Table in the database".format(table_name))
        fields = ""
        for key, value in kwargs.items():
            fields += " {} {} ,".format(key, value)
        fields = fields[:-1]
        logger.debug(fields)
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS {} ( {} )".format(table_name, fields))

    def insert(self, query, param):
        """
            Insert into the database, the query string is passed without the values, the values are passed as param
            in a tuple format
        :param query: insertion query string without values
        :param param: tuple of the table values
        """
        if isinstance(query, str):
            self.__cursor.execute(query, param)
            self.__conn.commit()

    def query(self, query):
        """

        :param query:
        :return:
        """
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def close_connection(self):
        self.__cursor.close()
        self.__conn.close()

    def delete(self, query):
        self.__cursor.execute(query)
        self.__conn.commit()

    def update(self, query):
        self.__cursor.execute(query)
        self.__conn.commit()

    def maintain_well_table(self):
        """
            Makes sure that the database has a well table by making a create table query if not exists
        """
        self.create_table(Well.__name__, id="INTEGER PRIMARY KEY", area="REAL", height="REAL")

    def maintain_reading_table(self):
        """
            Makes sure that the database has a Reading table by making a create table query if not exists
        """
        self.create_table(WellReading.__name__, id="INTEGER PRIMARY KEY",
                          well_id="INTEGER",
                          level="REAL",
                          volume="REAL",
                          time="TIMESTAMP",
                          FOREIGN="KEY(well_id) REFERENCES Well(id)")


#db_driver = DBDriver()
