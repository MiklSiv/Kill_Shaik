from PyQt5 import QtWidgets, QtCore
import serial
import  sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 185)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_COM = QtWidgets.QPushButton(self.centralwidget)
        self.bt_COM.setGeometry(QtCore.QRect(40, 30, 151, 41))
        self.bt_COM.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.bt_COM.setObjectName("bt_COM")
        self.bt_read = QtWidgets.QPushButton(self.centralwidget)
        self.bt_read.setGeometry(QtCore.QRect(230, 30, 101, 41))
        self.bt_read.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_read.setObjectName("bt_read")
        self.bt_write = QtWidgets.QPushButton(self.centralwidget)
        self.bt_write.setGeometry(QtCore.QRect(230, 90, 101, 41))
        self.bt_write.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.bt_write.setObjectName("bt_write")
        self.vivod = QtWidgets.QLabel(self.centralwidget)
        self.vivod.setGeometry(QtCore.QRect(360, 30, 421, 41))
        self.vivod.setObjectName("vivod")
        self.vvod = QtWidgets.QTextEdit(self.centralwidget)
        self.vvod.setGeometry(QtCore.QRect(360, 90, 421, 41))
        self.vvod.setObjectName("vvod")
        MainWindow.setCentralWidget(self.centralwidget)
        self.infa = ''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fun()

    def fun(self):
        self.bt_COM.clicked.connect(lambda: self.serial_port())
        self.bt_read.clicked.connect(lambda: self.get())
        self.bt_write.clicked.connect(lambda: self.send())

    def serial_port(self):
        port = 'COM%d' %4
        try:
            self.infa = serial.Serial(port)
            print ('yes')

        except (OSError, serial.SerialException):
            pass

    def get(self):
        text = self.infa.readline()
        self.vivod.setText(text.decode('utf-8'))

    def send(self):
        text = self.infa.write()
        self.vivod.setText(text.decode('utf-8'))





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_COM.setText(_translate("MainWindow", "подключение COM порта"))
        #self.bt_COM2.setText(_translate("MainWindow", "отключение COM порта"))
        self.bt_read.setText(_translate("MainWindow", "READ"))
        self.bt_write.setText(_translate("MainWindow", "WRITE"))





def app():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()