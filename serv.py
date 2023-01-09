import time
import socket
import sqlite3 as sql
import threading
import time



SERVER_ADDRESS = ('localhost', 8686)

# Настраиваем сокет
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)
server.listen(10)
print('server is running, please, press ctrl+c to stop')

class Server():
    def __init__(self, client, address):
        self.client, self.address = client, address
        self.client.send('Hello client'.encode('UTF-8'))
        print("new connection from {address}".format(address=self.address))
        self.flag = True
    def read(self):
        conn = sql.connect('example.db')
        cursor = conn.cursor()
        while self.flag:
            global text
            try:
                data = self.client.recv(1024)
                text = data.decode('utf-8')
                cursor.execute(f"INSERT INTO to_com VALUES({text})")
                conn.commit()
            except:
                pass
            time.sleep(1)
    def send(self):
        while self.flag:
            try:
                vvod = input()
                if vvod == 'close':
                    self.client.send('server close'.encode('utf-8'))
                    self.client.close()
                    print('server close')
                    self.flag = False
                    break
                else:
                    self.client.send(vvod.encode('utf-8'))
            except:
                pass
            time.sleep(1)

    def active(self):
        vvod = threading.Thread(target=self.read)
        vivod = threading.Thread(target=self.send)
        vvod.start()
        vivod.start()

import serial


def cikl():
    with serial.Serial("COM4") as ser:
        print(ser.readline().decode('utf-8'))
        global text
        conn = sql.connect('example.db')
        cursor = conn.cursor()
        while True:
            try:
                cursor.execute('SELECT * FROM to_com')
                Q = cursor.fetchall()

                ser.write(Q[-1][-1].encode('utf-8'))
                print(ser.readline().decode('utf-8'))
            except:
                pass

def serv():
    try:
        client, address = server.accept()
        client1 = Server(client, address)
        client1.active()
    except:
        pass


com_port = threading.Thread(target=cikl)
servtr_vkl = threading.Thread(target=serv)
com_port.start()
servtr_vkl.start()
