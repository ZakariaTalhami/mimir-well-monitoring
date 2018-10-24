import time
import pigpio
import struct

I2C_ADDR=9

def i2c(id, tick):
    print("Inside the Even Callback")
    global pi

    s, b, d = pi.bsc_i2c(I2C_ADDR)

    if b:
        print(len(d))
        # print(d[:-1])
        myHex = ":".join("{:02x}".format(x) for x in d)
        id , measurement = struct.unpack("ff", d)
        print(myHex)
        print(int(id), float(measurement))

pi = pigpio.pi()

if not pi.connected:
    exit()

# Respond to BSC slave activity
print("Created the event Call Back")
e = pi.event_callback(pigpio.EVENT_BSC, i2c)

pi.bsc_i2c(I2C_ADDR) # Configure BSC as I2C slave
time.sleep(1000)

e.cancel()

pi.bsc_i2c(0) # Disable BSC peripheral

pi.stop()
