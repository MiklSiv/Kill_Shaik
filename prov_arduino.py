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
            if count == 10:
                break
            elif ser.read().decode('utf-8') == 'U':
               count += 1
               print(f' {count}   {ser.read(size=5).decode()}' )
            else:
               pass



com_er()







