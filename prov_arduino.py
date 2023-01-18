import time

import serial

text = "HELLO"


def com_ty():
    ser = serial.Serial("COM4", timeout=3)
    if ser.isOpen():
        ser.write(text.encode('utf-8'))
        print('write')
        print(ser.readline().decode('utf-8'))

def com_er():
    ser = serial.Serial("COM5", timeout=3)
    count = 1
    while True:
        if ser.isOpen():
            if ser.read().decode('utf-8') == 'U':
                ask = "U" + ser.read(size = 5).decode('utf-8')
                print (1,  ask)
                break
            else:
               pass
    while True:
        print(ser.read(size = 6).decode('utf-8'))



com_er()







