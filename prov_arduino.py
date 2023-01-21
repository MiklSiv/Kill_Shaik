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
    Flag = True
    while Flag:
        if ser.isOpen():
            if ser.read().decode('utf-8') == 'U':
                ask = "U" + ser.read(size = 31).decode('utf-8')
                print (count,  ask)
                count +=1
                if count == 5:
                    Flag = False
            else:
               pass






com_er()







