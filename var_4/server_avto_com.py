import time
import sys
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from var_4 import connections
import threading






class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 900)
        MainWindow.setWindowTitle("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")

        self.label_server = QtWidgets.QLabel(self.centralwidget)
        self.label_server.setGeometry(QtCore.QRect(650, 20, 41, 21))
        self.label_server.setObjectName("label")
        self.label_server.setText("Server activaithion")

        self.bt_on_server = QtWidgets.QPushButton(self.centralwidget)
        self.bt_on_server.setGeometry(QtCore.QRect(620, 45, 61, 20))
        self.bt_on_server.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(0, 255, 127);")
        self.bt_on_server.setObjectName("bt_on_server")
        self.bt_on_server.setText("ON")

        self.bt_off_server = QtWidgets.QPushButton(self.centralwidget)
        self.bt_off_server.setGeometry(QtCore.QRect(700, 45, 61, 20))
        self.bt_off_server.setStyleSheet("background-color: rgb(255, 255, 127);\n"
                                      "")
        self.bt_off_server.setObjectName("bt_off_server")
        self.bt_off_server.setText("OFF")

        self.label_config = QtWidgets.QLabel(self.centralwidget)
        self.label_config.setGeometry(QtCore.QRect(650, 90, 80, 21))
        self.label_config.setObjectName("label_config")
        self.label_config.setText("Start config")

        self.bt_config = QtWidgets.QPushButton(self.centralwidget)
        self.bt_config.setGeometry(QtCore.QRect(650, 120, 61, 20))
        self.bt_config.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(0, 255, 127);")
        self.bt_config.setObjectName("bt_config")
        self.bt_config.setText("Start")

        self.botton_serv()

        self.Spisok_com = [] # список экземпляров класса Connection
        self.Spisok_com.append(self.Connection(self.centralwidget, 'arduino1', 0))
        self.Spisok_com.append(self.Connection(self.centralwidget, 'arduino2', 50))
        self.Spisok_com.append(self.Connection(self.centralwidget, 'power1', 100))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

    def botton_serv(self):
        self.bt_on_server.clicked.connect(lambda: self.server_power('onn'))
        self.bt_off_server.clicked.connect(lambda: self.server_power('off'))
        self.bt_config.clicked.connect(lambda: self.com_start())


    def com_start(self):
        if connections.com_config():
            for i in self.Spisok_com:
                try:
                    i.com_port(connections.COM_config[i.name_comport])
                    i.com_text.setText(connections.COM_config[i.name_comport])
                except:
                    pass


    def server_power(self, vvod = 'on'):
        if vvod != "off":
            serv = threading.Thread(target=connections.server_on)
            serv.start()
            self.bt_on_server.setText("RUNNING")
            self.bt_off_server.setText("OFF")

        else:
            connections.server_off()
            self.bt_on_server.setText("ON")
            self.bt_off_server.setText("CLOSE")


    class Connection():
        def __init__(self, centralwidget, name_comport, n):
            self.centralwidget = centralwidget
            self.name_comport = name_comport

            self.bt_on_com = QtWidgets.QPushButton(self.centralwidget)
            self.bt_on_com.setGeometry(QtCore.QRect(330, 45 + n, 61, 20))
            self.bt_on_com.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 255, 127);")
            self.bt_on_com.setObjectName("bt_on_com")
            self.bt_on_com.setText("ON")

            self.bt_off_com = QtWidgets.QPushButton(self.centralwidget)
            self.bt_off_com.setGeometry(QtCore.QRect(430, 45 + n, 61, 20))
            self.bt_off_com.setStyleSheet("background-color: rgb(255, 255, 127);\n"
                                          "")
            self.bt_off_com.setObjectName("bt_off_com")
            self.bt_off_com.setText("OFF")

            self.bt_loop = QtWidgets.QPushButton(self.centralwidget)
            self.bt_loop.setGeometry(QtCore.QRect(530, 45 + n, 61, 20))
            self.bt_loop.setStyleSheet("background-color: rgb(255, 255, 127);\n"
                                          "")
            self.bt_loop.setObjectName("bt_off_com")
            self.bt_loop.setText("LOOP")

            self.com_number = QtWidgets.QTextEdit(self.centralwidget)
            self.com_number.setGeometry(QtCore.QRect(60, 45 + n, 40, 20))
            font = QtGui.QFont()
            font.setPointSize(7)
            self.com_number.setFont(font)
            self.com_number.setObjectName("textEdit_2")

            self.text_com_name = QtWidgets.QLabel(self.centralwidget)
            self.text_com_name.setGeometry(QtCore.QRect(249, 45 + n, 81, 22))
            font = QtGui.QFont()
            font.setPointSize(7)
            self.text_com_name.setFont(font)
            self.text_com_name.setObjectName("textEdit_2")
            self.text_com_name.setText(self.name_comport)

            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(170, 20 + n, 41, 21))
            self.label.setObjectName("label")
            self.label.setText("SPEED")

            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(60, 20 + n, 51, 21))
            self.label_2.setObjectName("label_2")
            self.label_2.setText("№ COM")

            self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
            self.comboBox_2.setGeometry(QtCore.QRect(160, 45 + n, 60, 22))
            self.comboBox_2.setObjectName("comboBox_2")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(0, "9600")
            self.comboBox_2.setItemText(1, "19200")
            self.comboBox_2.setItemText(2, "115200")
            self.botton()
            self.ser = ''

        def botton(self):
            self.bt_on_com.clicked.connect(lambda: self.com_port(self.com_number.toPlainText()))
            self.bt_off_com.clicked.connect(lambda: self.com_port('close'))
            self.bt_loop.clicked.connect(lambda: self.Loop())


        def Loop(self):
            connections.loop(connections.COM_FlAG[self.name_comport][1], self.name_comport)
            self.bt_loop.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 255, 127);")


        def com_port(self, com):
            if com != "close":
                self.ser = serial.Serial("COM" + str(com), timeout=3) # полключается сом порт по номеру из ввода
                if self.ser.isOpen():
                    self.bt_on_com.setText("OPEN")
                    self.bt_off_com.setText("OFF")
                    connections.COM_FlAG[self.name_comport] = ['open', self.ser]

            else:
                connections.COM_FlAG[self.name_comport][0] = False
                time.sleep(2)
                self.ser.close()
                self.bt_on_com.setText("ON")
                self.bt_off_com.setText("CLOSE")
                self.bt_loop.setStyleSheet("background-color: rgb(255, 255, 127);\n"
                                          "")
                connections.COM_FlAG_loop[self.name_comport][0] = False

def app(): # графический интерфей
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()