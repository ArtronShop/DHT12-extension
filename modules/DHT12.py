from machine import Pin, I2C
import os

def read():
    machine = os.uname().machine
    if "KidBright32" in machine:
        i2c1 = I2C(1, scl=Pin(5), sda=Pin(4), freq=100000)
    else:
        i2c1 = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
    d = i2c1.readfrom_mem(0x5C, 0x00, 4)
    h = d[0] + (d[1] * 0.1)
    t = d[2] + ((d[3] & 0x7F) * 0.1)
    if d[3] & 0x80:
        t = -t
    return (t, h)
