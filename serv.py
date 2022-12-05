from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import socket

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 209)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_server = QtWidgets.QPushButton(self.centralwidget)
        self.bt_server.setGeometry(QtCore.QRect(190, 20, 111, 31))
        self.bt_server.setObjectName("bt_server")
        self.bt_send = QtWidgets.QPushButton(self.centralwidget)
        self.bt_send.setGeometry(QtCore.QRect(60, 80, 111, 31))
        self.bt_send.setObjectName("bt_send")
        self.text_send = QtWidgets.QTextEdit(self.centralwidget)
        self.text_send.setGeometry(QtCore.QRect(220, 80, 241, 31))
        self.text_send.setObjectName("text_send")
        self.bt_give = QtWidgets.QPushButton(self.centralwidget)
        self.bt_give.setGeometry(QtCore.QRect(60, 130, 111, 31))
        self.bt_give.setObjectName("bt_give")
        self.text_give = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_give.setGeometry(QtCore.QRect(220, 130, 241, 31))
        self.text_give.setObjectName("text_give")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.server = ''
        self.client = ''

        self.add_server()
        self.send()

    def add_server(self):
        self.bt_server.clicked.connect(lambda: self.server_vkl())

    def send(self):
        self.bt_send.clicked.connect(lambda: self.send_text())

    def server_vkl(self):
        SERVER_ADDRESS = ('localhost', 8686)

        # Настраиваем сокет
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(SERVER_ADDRESS)
        self.server.listen(10)
        print('server is running, please, press ctrl+c to stop')
        self.client, address = self.server.accept()
        print("new connection from {address}".format(address=address))
        self.client.send('HELLO'.encode('UTF-8'))

    def send_text(self):

        self.client.send(self.text_send.toPlainText().encode('UTF-8'))



    def give(self):
        client, address = self.server.accept()
        client.send(input().encode('UTF-8'))
        data = client.recv(1024)
        self.text_give.setText(data)









    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_server.setText(_translate("MainWindow", "включить сервер"))
        self.bt_send.setText(_translate("MainWindow", "send"))
        self.bt_give.setText(_translate("MainWindow", "give"))


def app():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()