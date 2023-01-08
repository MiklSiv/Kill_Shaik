'''  сервер запускается, при активном клиенте появляется связь.
Сервер поучает сообщения, при любом инпуте отправляет на клиент остановку и рубит связь'''

import time
import socket
import threading
import sqlite3 as sq
import animathion

SERVER_ADDRESS = ('localhost', 8686)

# Настраиваем сокет
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)
server.listen(10)
print('server is running, please, press ctrl+c to stop')


client, address = server.accept()
client.send('Hello client'.encode('UTF-8'))
print("new connection from {address}".format(address=address))

Q = True
x_graf = []
y_graf = []


def read():
    global x_graf, y_graf
    while True:
        if Q == False:
            client.send('server close'.encode('utf-8'))
            client.close()
            cur.close()
            print ('server close')
            break
        data = client.recv(1024).decode('utf-8')
        a, b = data.split(',')
        print(a, b)
        with sq.connect('primer.db') as con:
            cur = con.cursor()
            cur.execute(f""" INSERT INTO data(time, num)VALUES({a}, {b})
            """)
        x_graf.append(a)
        y_graf.append(b)
        time.sleep(1)

def close_connecthion():
    global Q
    input()
    Q = False



vvod = threading.Thread(target=read)
end = threading.Thread(target=close_connecthion)


vvod.start()

animathion.graf(x_graf, y_graf)
end.start()

