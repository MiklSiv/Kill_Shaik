import serial

text = '6'
def connecth(port):
    try:
        ser = serial.Serial(port)
        print(ser.readline().decode('utf-8'))
    except (OSError, serial.SerialException):
        pass



    while True:
        try:
        ser.write(text.encode('utf-8'))
        print(ser.readline().decode('utf-8'))







