import logging
import pprint
import sqlite3
from random import Random

import Linker
from DBHandlers.DBDriver import DBDriver
from DBHandlers.WellDAO import WellDAO
from DBHandlers.WellReadingDAO import WellReadingDAO
from Linker.Linker import Linker
from Models.Well import Well
from Models.Reading import Reading

import logging.config

from Models.WellReading import WellReading


def init_logging():
    logging.config.fileConfig('logs//logger.conf', disable_existing_loggers=False)
    logging.info("-------------------------------------------------------- |")
    logging.info("-------           New Logging session            ------- |")
    logging.info("-------------------------------------------------------- |")


init_logging()
# create random Generator
rand = Random()
randint = rand.randint(0, 1000)

# Testing Well And WellDAO
well5 = Well(randint, round(rand.uniform(1, 10), 3), round(rand.uniform(1, 10), 3))
well5DAo = WellDAO()
well5DAo.save(well5)
mylist = well5DAo.read_all()
pprint.pprint(mylist)
pprint.pprint(well5DAo.read_by_id(randint))
well5.set_height(round(rand.uniform(1, 10), 3))
well5.set_area(round(rand.uniform(1, 10), 3))
well5DAo.update(well5)
# well5DAo.delete(well5.get_well_id())

reading_id = rand.randint(0 , 1000)
reading = WellReading(well5, round(rand.uniform(1, 30), 3), reading_id=reading_id)
readingDAO = WellReadingDAO()
readingDAO.save(reading)
readingDAO.read_all()
readingDAO.read_by_id(reading_id)
reading.set_volume(25.0)
readingDAO.update(reading)
readingDAO.delete(reading_id)
# well5DAo.save(well5)
# reading5 = Reading(3, 25)
# print(reading5)
# wellReading = WellReading(well5 , 5)
# print(wellReading)

myLinker = Linker()
meReading = Reading(24 , 25.363)
myLinker.link_and_persist(meReading)

# # main="first" , comesafter = "second"
# db.create_table("hello", main="TEXT", comesafter="TEXT")
# # db.insert_data("hello", main="TEXT", comesafter="TEXT")
