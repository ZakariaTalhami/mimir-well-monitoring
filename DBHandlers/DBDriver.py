import sqlite3

import logging

from Models.Well import Well

logger = logging.getLogger(__name__)


# Might need to add some Try blocks for the execute

class DBDriver:

    def __init__(self):
        self.__conn = sqlite3.connect("gateway.db")
        self.__conn.set_trace_callback(logger.info)
        self.__cursor = self.__conn.cursor()
        self.maintain_well_table()

    def __del__(self):
        self.close_connection()

    def create_table(self, table_name, **kwargs):
        logger.info("Creating {} Table in the database".format(table_name))
        fields = ""
        for key, value in kwargs.items():
            fields += " {} {} ,".format(key, value)
        fields = fields[:-1]
        logger.debug(fields)
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS {} ( {} )".format(table_name, fields))

    def insert(self, query, param):
        if isinstance(query, str):
            self.__cursor.execute(query, param)
            self.__conn.commit()

    def query(self, query):
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
        self.create_table(Well.__name__, id="INTEGER PRIMARY KEY", area="REAL", height="REAL")


db_driver = DBDriver()
