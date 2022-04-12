import board
import busio
import time

import adafruit_si5351

i2c = busio.I2C(board.SCL, board.SDA)
si5351 = adafruit_si5351.SI5351(i2c)

si5351.pll_a.configure_integer(36)
si5351.pll_b.configure_fractional(24, 2, 3)

si5351.outputs_enabled = True

while True:
        c = input()
        if c=='q':
                break
        if c=='0':
                si5351.clock_0.configure_integer(si5351.pll_a, 30)
                time.sleep(0.02)

        if c=='1':
                si5351.clock_0.configure_fractional(si5351.pll_a, 30, 1, 1000)
                time.sleep(0.02)
