import time
import socket
import threading


SERVER_ADDRESS = ('localhost', 8686)

# Настраиваем сокет
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)
server.listen(10)
print('server is running, please, press ctrl+c to stop')

class Connecthion_my():
    def __init__(self, client, address):
        self.client, self.address = client, address
        self.client.send('Hello client'.encode('UTF-8'))
        print("new connection from {address}".format(address=self.address))
        self.flag = True
    def read(self):
        while self.flag:
            try:
                data = self.client.recv(1024)
                print (data.decode('utf-8'))
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

client1 = ''
client2 = ''
Spisok = [client1, client2]
count = 0


while True:
    try:
        client, address = server.accept()
        Spisok[count] = Connecthion_my(client, address)
        Spisok[count].active()
        count += 1
    except:
        break




