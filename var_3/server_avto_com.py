


import sys
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
import server_class
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 900)
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
            self.comboBox.setItemText(0, "power 1")
            self.comboBox.setItemText(1, "power 2")
            self.comboBox.setItemText(2, "power 3")
            self.comboBox.setItemText(3, "power 4")
            self.comboBox.setItemText(4, "arduino")
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
                self.ser = serial.Serial("COM" + str(com))
                self.name_comport = self.comboBox.
                if self.ser.isOpen():
                    self.bt_on_com.setText("OPEN")
                    print(self.ser.readline().decode('utf-8'))
                    self.bt_off_com.setText("OFF")
            else:
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

def all_app():
    #server = threading.Thread(target=server_class.server) #включение библиотеки с созданием подключений сервера
    app_w = threading.Thread(target=app)
    #server.start()
    app_w.start()

if __name__ == "__main__":
    all_app()