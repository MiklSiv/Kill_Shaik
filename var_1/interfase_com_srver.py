#создается интерфейс для подключения ком-портов и серверов к портам
# используется файл server для создания класа Server по номеру порта из интерфейса
#




import sys
import serial
from PyQt5 import QtCore, QtWidgets
import server

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 300)
        MainWindow.setWindowTitle("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.com1 = self.Connecthion(self.centralwidget, 0)
        self.com2 = self.Connecthion(self.centralwidget, 50)
        self.com3 = self.Connecthion(self.centralwidget, 100)



        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)


    class Connecthion():
        def __init__(self, centralwidget, n):
            self.centralwidget = centralwidget
            self.bt_on_com = QtWidgets.QPushButton(self.centralwidget)
            self.bt_on_com.setGeometry(QtCore.QRect(260, 45 + n, 61, 20))
            self.bt_on_com.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 255, 127);")
            self.bt_on_com.setObjectName("bt_on_com")
            self.bt_off_com = QtWidgets.QPushButton(self.centralwidget)
            self.bt_off_com.setGeometry(QtCore.QRect(350, 45 + n, 61, 20))
            self.bt_off_com.setStyleSheet("background-color: rgb(255, 255, 127);\n"
                                          "")
            self.bt_off_com.setObjectName("bt_off_com")
            self.bt_server = QtWidgets.QPushButton(self.centralwidget)
            self.bt_server.setGeometry(QtCore.QRect(640, 45 + n, 61, 20))
            self.bt_server.setStyleSheet("background-color: rgb(85, 255, 0);")
            self.bt_server.setObjectName("bt_server")
            self.speed_text = QtWidgets.QTextEdit(self.centralwidget)
            self.speed_text.setGeometry(QtCore.QRect(140, 45 + n, 91, 20))
            self.speed_text.setObjectName("textEdit")
            self.com_text = QtWidgets.QTextEdit(self.centralwidget)
            self.com_text.setGeometry(QtCore.QRect(30, 45 + n, 91, 20))
            self.com_text.setObjectName("textEdit_2")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(170, 20 + n, 41, 21))
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(60, 20 + n, 51, 21))
            self.label_2.setObjectName("label_2")
            self.port_text = QtWidgets.QTextEdit(self.centralwidget)
            self.port_text.setGeometry(QtCore.QRect(530, 45 + n, 91, 20))
            self.port_text.setObjectName("textEdit_3")
            self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox.setGeometry(QtCore.QRect(440, 45 + n, 61, 31))
            self.checkBox.setObjectName("checkBox")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(540, 20 + n, 71, 22))
            self.label_3.setObjectName("label_3")
            self.bt_on_com.setText("ON")
            self.bt_off_com.setText("OFF")
            self.bt_server.setText("ON")
            self.label.setText("SPEED")
            self.label_2.setText("№ COM")
            self.checkBox.setText("LOOP")
            self.label_3.setText("PORT SERVER")
            self.botton()
            self.ser = ''
            self.server = ''



        def botton(self):
            self.bt_on_com.clicked.connect(lambda: self.com_port(self.com_text.toPlainText()))
            self.bt_off_com.clicked.connect(lambda: self.com_port('close'))
            self.bt_server.clicked.connect(lambda: self.serv(self.port_text.toPlainText()))

        def com_port(self, com):

            if com != "close":
                self.ser = serial.Serial("COM" + str(com))
                if self.ser.isOpen():
                    self.bt_on_com.setText("OPEN")
                    print(self.ser.readline().decode('utf-8'))
                    self.bt_off_com.setText("OFF")
            else:
                self.ser.close()
                self.bt_on_com.setText("ON")
                self.bt_off_com.setText("CLOSE")

        def serv(self, port):
            self.server = server.Server(int(port))


def app():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()