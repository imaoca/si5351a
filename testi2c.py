import smbus
import time

i2c = smbus.SMBus(1)
addr = 0x60

data = i2c.read_byte_data(addr, 0x01)
print(data)
