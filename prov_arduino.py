import serial

port = 'COM%d' %4
try:
    ser = serial.Serial(port)
    print('yes')

except (OSError, serial.SerialException):
    pass

def get():
    text = ser.readline().decode('utf-8')
    return text

def send(text):
    ser.write(text)

send(b'{CMD503ABC}')

print (6)
try:

    r = get()

    print (r)
except:
    print('no')

