import serial
text = '6'
port = "COM4"
def cikl(port):
    with serial.Serial(port) as ser:
        print(ser.readline().decode('utf-8'))
        while True:
            try:
                ser.write(text.encode('utf-8'))
                print(ser.readline().decode('utf-8'))
            except:
                pass


