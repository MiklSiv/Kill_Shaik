import serial

def cikl(port="COM4"):
    text = "0"
    count = 0
    with serial.Serial(port) as ser:
        print(ser.readline().decode('utf-8'))
        while True:
            try:
                ser.write(text.encode('utf-8'))
                print(ser.readline().decode('utf-8'))
            except:
                pass
            count += 1
            text = str(count)

cikl()
