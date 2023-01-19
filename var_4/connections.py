import time
import socket
import threading
import sqlite3



COM_FlAG = {"arduino1" : ["close", 'ser'],
            "arduino2" : ["close", 'ser'],
            "power1" : ["close", 'ser'],
            "power2" : ["close", 'ser']}  #sostoyanie_porta = ['close', 'open', 'write', 'client']

SERVER_FLAG = True

# управление обращением к сом портам

def client_to_com(client): #разовое обращение к портам
        try:
            data = client.recv(1024).decode('utf-8').split()  # спиок входных данных типа [x, y]: x - имя сом порта, у - команда для компорта
            if len(data) != 2:
                client.send('<ASK_error - bad struct massage>'.encode('utf-8'))

            elif data[0] not in COM_FlAG:
                client.send('<ASK_error - NULL COM_abonent>'.encode('utf-8'))
            else:
                while COM_FlAG[data[0]][1] == 'close':
                    time.sleep(0.1)
                else:
                    try:
                        COM_FlAG[data[0]][0] = 'close'
                        if COM_FlAG[data[0]][1].isOpen():
                            COM_FlAG[data[0]][1].write(data[1].encode('utf-8'))
                            ask = COM_FlAG[data[0]][1].readline().decode('utf-8')
                            with sqlite3.connect('../var_3/data_base.db') as tabl:
                                cursor = tabl.cursor()
                                zaps = (time.time(), data[1], ask)
                                cursor.execute(f'''INSERT INTO arduino (time, in_com, out_com) VALUES (?, ?, ?)''', zaps)
                                tabl.commit()
                            client.send(ask.encode('utf-8'))
                            COM_FlAG[data[0]][0] = 'open'
                        else:
                            client.send('<ASK_error - COM error>'.encode('utf-8'))
                    except:
                        client.send('<ASK_error - COM error>'.encode('utf-8'))

        except:
            pass

def loop(ser): # обращение к порту с зацикливанием

    if ser.isOpen():
        ser.write("text".encode())
        print(ser.readline().decode('utf-8'))


# блок управления сервером

server = ''
def server_on(): # включение сервера
    global server
    Spisok_client = [False] * 1000
    SERVER_ADDRESS = ('localhost', 5000)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(SERVER_ADDRESS)
    server.listen(10)
    print(' <<< server is running >>> ')
    while SERVER_FLAG:  # сканер появления клиентов. отправка сообщения в сом порт и обратно
        try:
            client, address = server.accept()
            for i in Spisok_client:
                if i == False:
                    i = threading.Thread(target=client_to_com, args = (client, ))
                    i.start()
                    break
        except:
            print('ex_server')


def server_off(): #отключение сервера
    global SERVER_FLAG
    SERVER_FLAG = False
    server.close()
    print ('<<< server OFF >>>')


