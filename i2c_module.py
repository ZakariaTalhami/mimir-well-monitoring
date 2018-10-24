import logging
import time
from datetime import datetime

import pigpio
import struct

# Setup the i2c module
#     CallBack
#             Read data from the i2c connection
#             Create a Reading instance
#             call linkers link_and_persist method
# infinite loop


# I2C address of the sink node.
from Linker.Linker import Linker
from Models.Reading import Reading

I2C_ADDR = 9

logger = logging.getLogger(__name__)
linker = Linker()

def i2c(id, tick):
    # print("Inside the Even Callback")
    logger.info("Receiving I2C communications")
    global pi

    # Read the I2C communication
    s, b, data = pi.bsc_i2c(I2C_ADDR)

    if b:
        # Convert Bytes into numeric values for well_id and measurement

        myHex = ":".join("{:02x}".format(x) for x in data)

        logger.info("Convert Raw Bytes into well_id and measurement: {}".format(myHex))
        well_id, measurement = struct.unpack("ff", data)
        logger.debug("Bytes converted to :> id = {} , measurement = {}".format(well_id , measurement))

        logger.info("Creadting a Reading instance from I2C data")
        reading = Reading(int(id) , measurement , datetime.now())
        logger.debug("Received Reading :\n{}".format(reading))

        linker.link_and_persist(reading)




pi = pigpio.pi()

if not pi.connected:
    exit()

# Respond to BSC slave activity
# print("Created the event Call Back")
logger.info("I2C call back Created")
e = pi.event_callback(pigpio.EVENT_BSC, i2c)

logger.info("Gateway's I2C address is set to {}".format(I2C_ADDR))
pi.bsc_i2c(I2C_ADDR)  # Configure BSC as I2C slave

# time.sleep(1000)

while True:
    pass

e.cancel()

pi.bsc_i2c(0)  # Disable BSC peripheral

pi.stop()
