from machine import Pin, I2C

def read():
    i2c1 = I2C(1, scl=Pin(5), sda=Pin(4), freq=100000)
    d = i2c1.readfrom_mem(0x5C, 0x00, 4)
    h = d[0] + (d[1] * 0.1)
    t = d[2] + ((d[3] & 0x7F) * 0.1)
    if d[3] & 0x80:
        t = -t
    return (t, h)
