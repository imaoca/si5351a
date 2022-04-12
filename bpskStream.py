import time
import smbus

I2C = smbus.SMBus(1)

while True:
        c = input()
        if c=='q':
                break
        if c=='0':
                i = I2C.read_byte_data(0x60, 16)
                I2C.write_byte_data(0x60, 16, i | 0x10)
                time.sleep(0.02)
        if c=='1':
                i = I2C.read_byte_data(0x60, 16)
                I2C.write_byte_data(0x60, 16, i & 0xEF)
        time.sleep(0.02)
