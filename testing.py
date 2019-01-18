import logging
import math
import pprint
import sqlite3
import time
from datetime import datetime
from random import Random

from matplotlib.pyplot import plot, show

import Linker
from DBHandlers.DBDriver import DBDriver
from DBHandlers.WellDAO import WellDAO
from DBHandlers.WellReadingDAO import WellReadingDAO
from FirebaseDriver.FirebaseDriver import CloudConnect
from Linker.Linker import Linker
from Models.Well import Well
from Models.Reading import Reading

import logging.config

from Models.WellReading import WellReading
from Test.TestDataGenerator import DataGenerator
from Test.Test_no_i2c import TestNoI2C
from reading_synch import ReadingSynch


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
# well5 = Well(randint, round(rand.uniform(1, 10), 3), round(rand.uniform(1, 10), 3))
# well5DAo = WellDAO()
# well5DAo.save(well5)
# mylist = well5DAo.read_all()
# pprint.pprint(mylist)
# pprint.pprint(well5DAo.read_by_id(randint))
# well5.set_height(round(rand.uniform(1, 10), 3))
# well5.set_area(round(rand.uniform(1, 10), 3))
# well5DAo.update(well5)
# # well5DAo.delete(well5.get_well_id())
#
# well5 = well5DAo.read_by_id(916)
# reading_id = rand.randint(0 , 1000)
# reading = WellReading(well5, round(rand.uniform(1, 30), 3), datetime.now(), reading_id=reading_id)
# readingDAO = WellReadingDAO()
# readingDAO.save(reading)
# readingDAO.read_all()
# readingDAO.read_by_id(reading_id)
# reading.set_volume(25.0)
# readingDAO.update(reading)
# readingDAO.delete(reading_id)
# # well5DAo.save(well5)
# # reading5 = Reading(3, 25)
# # print(reading5)
# # wellReading = WellReading(well5 , 5)
# # print(wellReading)
#
# myLinker = Linker()
# meReading = Reading(24 , 25.363)
# myLinker.link_and_persist(meReading)

# # main="first" , comesafter = "second"
# db.create_table("hello", main="TEXT", comesafter="TEXT")
# # db.insert_data("hello", main="TEXT", comesafter=


# well_dao = WellDAO()
# well_list = well_dao.read_all()
# UUID_list = [x.get_well_id() for x in well_list]
# gen = DataGenerator()
# gen.set_count(5)
# gen.set_uuid_list(UUID_list)
# start = time.time()
# gen.generator()
# end = time.time()
# # #
# tester = TestNoI2C(5 , "test.csv")
# tester.run()

# con = CloudConnect()
# ret = con.read_all_wells()
# print(ret)
# wellDao = WellDAO()
# wells = wellDao.read_all()
# con = CloudConnect(u"waterlevelmonitoringsyst-3ca70")
# for well in wells:
# con.save_well(well)

# synch = ReadingSynch()
# synch.start()
# dao = WellDAO()
# fire = CloudConnect()
# wells = fire.read_all_wells()
# print(dao.get_well_id_list())

values = []
for x in range(0, 100):
    values.append(100 * math.log10(x + 1) + 100)

for x in range(100, 200):
    values.append(50 * math.sin((x - 100) / 10) + 100 * math.log10(x + 1) + 100)

for x in range(200, 500):
    values.append(10 * math.sin((x - 100) / 10) + 100 * math.log10(x + 1) + 40)

plot(range(0, 500), values)
show()

welldao = WellDAO()
wells = welldao.read_all()
fire = CloudConnect()

for well in wells:
    readings = []
    for value in values:
        # Reading(well.get_well_id(), value, datetime.now())
        # readings.append()
        well_reading = WellReading(well, value, datetime.now())
        fire.save_reading(well_reading)

# for well in wells:
#     try:
#         dao.save(
#             well
#         )
#     except:
#         print(" {} failed".format(well.get_well_id()))
# raw = 50
# Welldao = WellDAO()
# print(Welldao.read_by_id(1))
# for well in wells:
#     Welldao.save(well)
#     WellReading(well , raw , datetime.now())
# fire.faults_increment_failed_respond(3)
# fire.faults_increment_failed_transmit(3)
