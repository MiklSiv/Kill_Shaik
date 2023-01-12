import time
import socket
import threading
import  serial




class Connecthion_client():
    def __init__(self, client, address):
        self.client, self.address = client, address
        self.client.send('Hello client'.encode('UTF-8'))
        print(f"new connection from {address}")

        self.com_port = self.client.recv(1024).decode('utf-8')

        self.ser = serial.Serial(self.com_port)
        print(self.ser.readline().decode('utf-8'))
        self.client.send(f"port {self.com_port} vkl".encode('UTF-8'))
        self.flag = True


    def read(self):
        while self.flag:
            try:
                data = self.client.recv(1024)
                if  data.decode('utf-8') == 'close':
                    self.client.send('connecthione close'.encode('utf-8'))
                    self.client.close()
                    self.ser.close()
                    print(f'Connecthion  client {self.address} close ')
                    self.flag = False

                else:
                    print (data.decode('utf-8'))
                    self.ser.write(data)
                    out = self.ser.readline()
                    self.client.send(out)
            except:
                pass
            time.sleep(1)


    def active(self):
        vvod = threading.Thread(target=self.read)
        vvod.start()


def server():

    SERVER_ADDRESS = ('localhost', 8686)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(SERVER_ADDRESS)
    server.listen(10)
    print('server is running, please, press ctrl+c to stop')


    Spisok_client = []

    while True:
        try:
            client, address = server.accept()
            Spisok_client.append( Connecthion_client(client, address))
            Spisok_client[-1].active()

        except:
            break




