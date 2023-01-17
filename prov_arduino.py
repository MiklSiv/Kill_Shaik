import time

import serial

text = "HELLO"

ser = serial.Serial("COM4", timeout=3)
if ser.isOpen():
    ser.write(text.encode('utf-8'))
    print('write')
    print(ser.readline().decode('utf-8'))









