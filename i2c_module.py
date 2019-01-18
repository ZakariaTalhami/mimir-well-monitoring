import math
import smbus
import time
import struct
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
        """
            Retrieve the IDs of the wells to be measured
        :return: list of well IDs
        """
        logger.info("Getting the list of well ids")
        well_list = self.__firebase.read_all_wells()
        # If connection with the cloud fails,
        # read from the local database
        if not well_list:
            well_list = self.__welldao.read_all()
        # Filter out only the Well IDs
        well_ids = [well.get_well_id() for well in well_list]
        logger.debug("Got ids of :> {}".format(",".join(well_ids)))
        return well_ids

    def get_reading_i2c(self, well_id: int):
        """
            Send reading request to the sink, by passing the well ID and the read command
        :param well_id: ID of well to be measured
        :return: reading measurement as float
        """
        # send command and id
        logger.info("Sending to slave CMD {} and well id {}".format(READ_CMD, well_id))
        self.__bus.write_byte_data(self.__slave_address, READ_CMD, well_id)
        time.sleep(1)
        # receive float / 4 bytes
        logger.info("Reading from the slave with CMD {}".format(READ_CMD))
        raw = self.__bus.read_i2c_block_data(self.__slave_address, READ_CMD, 4)
        logger.info("Slave returned :> {}".format(" ".join(str(raw))))
        # convert received 4 bytes to float
        raw = self.convert_to_float(self.convert_list_to_byte_array(raw))
        return raw

    def convert_list_to_byte_array(self, byte_list):
        """
            Convert byte values list to a bytearray
        :param byte_list: List of byte values
        :return: bytearray
        """
        data = bytearray()
        for i in byte_list:
            data.append(i)
        return data

    def convert_to_float(self, data):
        """
            Convert bytearray to float variable
        :param data:
        :return:
        """
        my_hex = ":".join("{:02x}".format(x) for x in data)
        logger.info("Convert Raw Bytes into well_id and measurement: {}".format(my_hex))
        # Convert as float
        measurement = struct.unpack("f", data)
        logger.debug("Bytes converted to :> measurement = {}".format(measurement[0]))
        return measurement[0]

    def run(self):
        """
            Loop of the I2C process
        :return:
        """
        logger.info("I2C master has been run")
        while True:
            try:
                logger.info("Reading cycle has begun")
                linker = Linker()
                well_ids = self.get_well_ids()
                for id in well_ids:
                    raw = self.get_reading_i2c(int(id))
                    if math.isclose(raw, 0):
                        logger.error("Received reading of 0, node {} has ack but failed to transmit data.".format(id))
                        self.__firebase.faults_increment_failed_transmit(id)
                    elif math.isclose(raw, -1):
                        logger.error("Received reading of -1, node {} has failed to respond.".format(id))
                        self.__firebase.faults_increment_failed_respond(id)
                    elif raw > 0:
                        reading = Reading(id, raw, datetime.now())
                        linker.link_and_persist(reading)
                time.sleep(10)
            except KeyboardInterrupt:
                quit()


if __name__ == '__main__':
    # Set the master slave sink address and run the process
    i2c = i2cMaster(0x10)
    i2c.run()
