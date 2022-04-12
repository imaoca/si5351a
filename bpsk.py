import time
import smbus

I2C = smbus.SMBus(1)
while True:
        i = I2C.read_byte_data(0x60, 16)
        I2C.write_byte_data(0x60, 16, i | 0x10) # CLK0_INV=1
        time.sleep(0.02)
        i = I2C.read_byte_data(0x60, 16)
        I2C.write_byte_data(0x60, 16, i & 0xEF) # CLK0_INV=0
        time.sleep(0.02)
