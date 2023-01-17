import time
import socket
import threading
import sqlite3


COM_FlAG = {"arduino1" : [False, "close", 'ser'],
            "arduino2" : [False, "close", 'ser'],
            "power1" : [False, "close", 'ser'],
            "power2" : [False, "close", 'ser']}  #sostoyanie_porta = ['close', 'open', 'write', 'client']

SERVER_FLAG = True
class Connection_client():
    def __init__(self, client, address):
        self.client, self.address = client, address
        self.client.send('Hello client'.encode('UTF-8'))
        print(f"new connection  from {address}")
        self.flag = True


    def read(self):
        while self.flag:
            try:

                data = self.client.recv(1024).decode('utf-8').split()  # спиок входных данных типа [x, y]: x - имя сом порта, у - команда для компорта

                if data[0] == 'close':
                    self.client.send('connection close'.encode('utf-8'))
                    self.client.close()
                    print(f'connection  client {self.address} close ')
                    self.flag = False
                    break
                elif len(data) != 2:
                    self.client.send('<ASK_error - bad struct massage>'.encode('utf-8'))
                    print (data) # снести на проекте
                elif data[0] not in COM_FlAG:
                    self.client.send('<ASK_error - NULL COM_abonent>'.encode('utf-8'))
                else:
                    while COM_FlAG[data[0]][1] == 'close':
                        time.sleep(0.1)
                    else:
                        try:
                            COM_FlAG[data[0]][1] = 'close'
                            ask = self.сomport_potok(COM_FlAG[data[0]][2], data[1])
                            with sqlite3.connect('data_base.db') as tabl:
                                cursor = tabl.cursor()
                                zaps = (time.time(), data[1], ask)
                                cursor.execute(f'''INSERT INTO arduino (time, in_com, out_com) VALUES (?, ?, ?)''', zaps)
                                tabl.commit()

                            self.client.send(ask.encode('utf-8'))
                            COM_FlAG[data[0]][1] = 'open'
                        except:
                            pass
            except:
                pass
            time.sleep(0.5)
    def send(self):
        self.client.send('connection close'.encode('utf-8'))
        self.client.close()
        print(f'connection  client {self.address} close ')
        self.flag = False  # смена для отключения соединения
    def сomport_potok(self, ser, text, loop=False):
        if loop == False:
            try:
                ser.write(text.encode('utf-8'))
                return ser.readline().decode('utf-8')
            except:
                    pass

        '''else:
            try:
                ser.write(text.encode('utf-8'))
                print(ser.readline().decode('utf-8'))
                except:
                    pass
                time.sleep(2)'''

    def active(self):
        vvod = threading.Thread(target=self.read)
        vvod.start()


server = ''
Spisok_client = []

def server_on(): # включение сервера
    global server, Spisok_client
    SERVER_ADDRESS = ('localhost', 8686)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(SERVER_ADDRESS)
    server.listen(10)
    print(' <<< server is running >>> ')

    while SERVER_FLAG:  # сканер появления клиентов. создание класса подключения  при появлении клиента
        try:
            client, address = server.accept()
            Spisok_client.append(Connection_client(client, address))
            Spisok_client[-1].active()
            print (Spisok_client)
        except:
            break


def server_off():
    global server, Spisok_client
    for i in Spisok_client:
        i.send()
    server.close()
    print ('<<< server OFF >>>')


