# import logging
# import logging.config
# import time
# from datetime import datetime
# import pigpio
# import struct
#
# # Setup the i2c module
# #     CallBack
# #             Read data from the i2c connection
# #             Create a Reading instance
# #             call linkers link_and_persist method
# # infinite loop
#
#
# # I2C address of the sink node.
# from Linker.Linker import Linker
# from Models.Reading import Reading
#
#
# def init_logging():
#     logging.config.fileConfig('logs//logger.conf', disable_existing_loggers=False)
#     logging.info("-------------------------------------------------------- |")
#     logging.info("-------           New Logging session            ------- |")
#     logging.info("-------------------------------------------------------- |")
#
#
# init_logging()
#
# I2C_ADDR = 9
#
# logger = logging.getLogger(__name__)
#
#
# def i2c(id, tick):
#     # print("Inside the Even Callback")
#     logger.info("Receiving I2C communications")
#     global pi
#     linker = Linker()
#     # Read the I2C communication
#     s, b, data = pi.bsc_i2c(I2C_ADDR)
#
#     if b == 8:
#         # Convert Bytes into numeric values for well_id and measurement
#
#         myHex = ":".join("{:02x}".format(x) for x in data)
#
#         logger.info("Convert Raw Bytes into well_id and measurement: {}".format(myHex))
#         well_id, measurement = struct.unpack("ff", data)
#         logger.debug("Bytes converted to :> id = {} , measurement = {}".format(well_id, measurement))
#
#         if measurement > 0:
#             logger.info("Creating a Reading instance from I2C data")
#             reading = Reading(int(well_id), measurement, datetime.now())
#             logger.debug("Received Reading :\n{}".format(reading))
#             linker.link_and_persist(reading)
#         else:
#             if measurement == -1:
#                 logger.error("Well {} failed to send measurement", well_id)
#             elif measurement == 0:
#                 logger.error("Invalid measurement of zero from well {} ", well_id)
#
#
#
#     else:
#         logger.info("I2C reading failed, expected 8 bytes received {}".format(b))
#
# pi = pigpio.pi()
#
# if not pi.connected:
#     exit()
#
# # Respond to BSC slave activity
# # print("Created the event Call Back")
# logger.info("I2C call back Created")
# e = pi.event_callback(pigpio.EVENT_BSC, i2c)
#
# logger.info("Gateway's I2C address is set to {}".format(I2C_ADDR))
# pi.bsc_i2c(I2C_ADDR)  # Configure BSC as I2C slave
#
# # time.sleep(1000)
#
# while True:
#     pass
#
# e.cancel()
#
# pi.bsc_i2c(0)  # Disable BSC peripheral
#
# pi.stop()


import smbus
import time
import logging
import logging.config
from DBHandlers.WellDAO import WellDAO
from DBHandlers.WellReadingDAO import WellReadingDAO
from FirebaseDriver.FirebaseDriver import CloudConnect
from Linker.Linker import Linker
from Models.Reading import Reading
from datetime import datetime

def init_logging():
    logging.config.fileConfig('logs//logger.conf', disable_existing_loggers=False)
    logging.info("-------------------------------------------------------- |")
    logging.info("-------           New Logging session            ------- |")
    logging.info("-------------------------------------------------------- |")


init_logging()
logger = logging.getLogger(__name__)
READ_CMD = 10


class i2cMaster:
    def __init__(self, slave):
        logger.info("Init the i2cMaster")
        self.__wellreadingdao = WellReadingDAO()
        self.__welldao = WellDAO()
        self.__firebase = CloudConnect()
        self.__slave_address = slave
        self.__bus = smbus.SMBus(1)

    def get_well_ids(self):
        logger.info("Getting the list of well ids")
        well_list = self.__firebase.read_all_wells()
        well_ids = [well.get_well_id() for well in well_list]
        logger.debug("Got ids of :> {}".format(",".join(well_ids)))
        return well_ids

    def get_reading_i2c(self, id: int):
        # send cmd and id
        logger.info("Sending to slave CMD {} and well id {}".format( READ_CMD , id))
        self.__bus.write_byte_data(self.__slave_address, READ_CMD, id)
        time.sleep(1)
        # receive float / 4 bytes
        logger.info("Reading from the slave with CMD {}".format(READ_CMD))
        raw = self.__bus.read_i2c_block_data(self.__slave_address, READ_CMD , 4)
        logger.info("Slave returned :> {}".format(" ".join(str(raw))))
        return raw

    def run(self):
        logger.info("I2C master has been run")
        while True:
            try:
                logger.info("Reading cycle has begun")
                linker = Linker()
                well_ids = self.get_well_ids()
                for id in well_ids:
                    raw = self.get_reading_i2c(int(id));
#                    reading = Reading(id, raw, datetime.now())
#                    linker.link_and_persist(reading)
                time.sleep(10)
            except KeyboardInterrupt:
                quit()

if __name__ == '__main__':
    i2c = i2cMaster(0x10)
    i2c.run()
