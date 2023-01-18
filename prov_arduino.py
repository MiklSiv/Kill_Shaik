import time

import serial

text = "DFGH"

ser = serial.Serial("COM3", timeout = 5)
if ser.isOpen():
    ser.write(text.encode())
    print('write')
    print(ser.readline().decode('utf-8'))









