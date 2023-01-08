from PyQt5 import QtWidgets
import serial
import  sys

def serial_ports():
    ports = ['COM%s' % (i + 1) for i in range(256)]
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']


class LedApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup(self)
        self.Port.addItems(serial_ports())
        self.Speed.addItems(speeds)
        self.realport = None
        self.ConnectButton.clicked.connect(self.connect)
        self.EnableBtn.clicked.connect(self.send)

    def connect(self):
        try:
            self.realport = serial.Serial(self.Port.currentText(),int(self.Speed.currentText()))
            self.ConnectButton.setStyleSheet("background-color: green")
            self.ConnectButton.setText('Подключено')
        except Exception as e:
            print(e)

    def send(self):
        if self.realport:
            self.realport.write(b'b')
        self.EnableBtn.clicked.connect(self.send)

    def connect(self):
        try:
            self.realport = serial.Serial(self.Port.currentText(),int(self.Speed.currentText()))
            self.ConnectButton.setStyleSheet("background-color: green")
            self.ConnectButton.setText('Подключено')
        except Exception as e:
            print(e)

    def send(self):
        if self.realport:
            self.realport.write(b'b')


def app():
    app = QtWidgets.QApplication(sys.argv)
    window = LedApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()