import time
import sys
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
import connections # модуль с классами клиентов, с классами сом портов
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

        self.com1 = self.Connecthion(self.centralwidget, 0)
        self.com2 = self.Connecthion(self.centralwidget, 50)
        self.com3 = self.Connecthion(self.centralwidget, 100)
        self.com4 = self.Connecthion(self.centralwidget, 150)
        self.com5 = self.Connecthion(self.centralwidget, 200)
        self.com6 = self.Connecthion(self.centralwidget, 250)
        self.com7 = self.Connecthion(self.centralwidget, 300)
        self.com8 = self.Connecthion(self.centralwidget, 350)
        self.com9 = self.Connecthion(self.centralwidget, 400)
        self.com10 = self.Connecthion(self.centralwidget, 450)
        self.com11 = self.Connecthion(self.centralwidget, 500)
        self.com12 = self.Connecthion(self.centralwidget, 550)
        self.com13 = self.Connecthion(self.centralwidget, 600)
        self.com14 = self.Connecthion(self.centralwidget, 650)
        self.com15 = self.Connecthion(self.centralwidget, 700)
        self.com16 = self.Connecthion(self.centralwidget, 750)
        self.botton_serv()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

    def botton_serv(self):
        self.bt_on_server.clicked.connect(lambda: self.server_power('onn'))
        self.bt_off_server.clicked.connect(lambda: self.server_power('off'))

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


    class Connecthion():
        def __init__(self, centralwidget, n):
            self.centralwidget = centralwidget

            self.bt_on_com = QtWidgets.QPushButton(self.centralwidget)
            self.bt_on_com.setGeometry(QtCore.QRect(360, 45 + n, 61, 20))
            self.bt_on_com.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 255, 127);")
            self.bt_on_com.setObjectName("bt_on_com")
            self.bt_on_com.setText("ON")

            self.bt_off_com = QtWidgets.QPushButton(self.centralwidget)
            self.bt_off_com.setGeometry(QtCore.QRect(450, 45 + n, 61, 20))
            self.bt_off_com.setStyleSheet("background-color: rgb(255, 255, 127);\n"
                                          "")
            self.bt_off_com.setObjectName("bt_off_com")
            self.bt_off_com.setText("OFF")

            self.com_text = QtWidgets.QTextEdit(self.centralwidget)
            self.com_text.setGeometry(QtCore.QRect(60, 45 + n, 40, 20))
            font = QtGui.QFont()
            font.setPointSize(7)
            self.com_text.setFont(font)
            self.com_text.setObjectName("textEdit_2")

            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(170, 20 + n, 41, 21))
            self.label.setObjectName("label")
            self.label.setText("SPEED")

            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(60, 20 + n, 51, 21))
            self.label_2.setObjectName("label_2")
            self.label_2.setText("№ COM")

            self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox.setGeometry(QtCore.QRect(550, 45 + n, 61, 31))
            self.checkBox.setObjectName("checkBox")
            self.checkBox.setText("LOOP")


            self.comboBox = QtWidgets.QComboBox(self.centralwidget)
            self.comboBox.setGeometry(QtCore.QRect(249, 45 + n, 81, 22))
            self.comboBox.setObjectName("comboBox")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
            self.comboBox_2.setGeometry(QtCore.QRect(160, 45 + n, 60, 22))
            self.comboBox_2.setObjectName("comboBox_2")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox.setItemText(0, "power1")
            self.comboBox.setItemText(1, "power2")
            self.comboBox.setItemText(2, "power3")
            self.comboBox.setItemText(3, "arduino1")
            self.comboBox.setItemText(4, "arduino2")
            self.comboBox_2.setItemText(0, "9600")
            self.comboBox_2.setItemText(1, "19200")
            self.comboBox_2.setItemText(2, "115200")
            self.botton()
            self.ser = ''
            self.name_comport = ''

        def botton(self):
            self.bt_on_com.clicked.connect(lambda: self.com_port(self.com_text.toPlainText()))
            self.bt_off_com.clicked.connect(lambda: self.com_port('close'))


        def com_port(self, com):

            if com != "close":
                self.ser = serial.Serial("COM" + str(com), timeout=2) # полключается сом порт по номеру из ввода
                self.name_comport = self.comboBox.currentText()
                if self.ser.isOpen():
                    self.bt_on_com.setText("OPEN")
                    self.ser.write("HELLO".encode('utf-8'))# снести на основном проекте
                    print(f"abonent {self.name_comport} -- ", self.ser.readline().decode('utf-8')) #чтение ответа из ардуино
                    self.bt_off_com.setText("OFF")
                    connections.COM_FlAG[self.name_comport] = [True, 'open', self.ser]


            else:
                time.sleep(2)
                self.ser.close()
                self.bt_on_com.setText("ON")
                self.bt_off_com.setText("CLOSE")



def app(): # графический интерфей
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()