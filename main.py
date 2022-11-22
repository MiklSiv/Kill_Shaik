import serial
import time

ser = serial.Serial('COM4', 19200, timeout=1)
for i in range(10):
    if not ser.is_open:
        ser.open()
    #time.sleep(1)
    da = ser.readline()
    #ser.close()
    print('Вот так:', i, da)