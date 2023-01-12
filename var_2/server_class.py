import time
import socket
import threading




class Connecthion_my():
    def __init__(self, client, address):
        self.client, self.address = client, address
        self.client.send('Hello client'.encode('UTF-8'))
        print(f"new connection from {address}")
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


def server():

    SERVER_ADDRESS = ('localhost', 8686)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(SERVER_ADDRESS)
    server.listen(10)
    print('server is running, please, press ctrl+c to stop')

    count = 0
    Spisok_client = [{'client' + str(count): 0}]

    while True:
        try:
            client, address = server.accept()
            Spisok_client[count] = Connecthion_my(client, address)
            Spisok_client[count].active()
            count += 1
            Spisok_client.append('client' + str(count))
        except:
            break




