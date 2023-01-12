


import time
import threading
import socket
import sqlite3 as sql

class Server():
    def __init__(self, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', port))
        self.server.listen(10)
        print(f'server with port {port} is running')
        self.flag = True
        self.active()

    def read(self):
        conn = sql.connect('../example.db')
        cursor = conn.cursor()
        while self.flag:

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
        self.client, self.address = self.server.accept()
        self.client.send('Hello client'.encode('UTF-8'))
        print("new connection from {address}".format(address=self.address))
        vvod = threading.Thread(target=self.read)
        vivod = threading.Thread(target=self.send)
        vvod.start()
        vivod.start()







