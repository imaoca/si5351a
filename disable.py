import board
import busio
import time

import adafruit_si5351

i2c = busio.I2C(board.SCL, board.SDA)
si5351 = adafruit_si5351.SI5351(i2c)

si5351.outputs_enabled = False
