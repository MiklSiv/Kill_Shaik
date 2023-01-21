import time
import socket
import threading
import sqlite3



COM_FlAG = {"arduino1" : ["close", 'ser'],
            "arduino2" : ["close", 'ser'],
            "power1" : ["close", 'ser'],
            "power2": ["close", 'ser'],
            "power3": ["close", 'ser'],
            "power4" : ["close", 'ser']}  #sostoyanie_porta = ['close', 'open', 'write', 'client']

COM_FlAG_loop = {"power1" : ['message', 'ask'],
                 "power2" : ['message', 'ask'],
                 "power2" : ['message', 'ask'],
                 "power4" : ['message', 'ask']}

SERVER_FLAG = True

COM_config = {}

def com_config():# чтение файла с конфигурациями
    COM_conf = []
    try:
        with open('text_config.txt', 'r') as conf:
            while a := conf.readline():
                COM_conf.append(a.split())
        for i in COM_conf:
            COM_config[i[0]] = i[1]
        return True
    except:
        return False

# управление обращением к сом портам

def client_to_com(client): #разовое обращение к портам
    try:
        data = client.recv(1024).decode('utf-8').split()  # спиок входных данных типа [x, y]: x - имя сом порта, у - команда для компорта
        if len(data) != 2:
            client.send('<ASK_error - bad struct message>'.encode('utf-8'))
        elif data[0] not in COM_FlAG:
            client.send('<ASK_error - com abonent NULL>'.encode('utf-8'))

        elif data[0] in COM_FlAG_loop:
            COM_FlAG_loop[data[0]][0] = data[1]
            time.sleep(0.2)
            client.send(COM_FlAG_loop[data[0]][1].encode('utf-8'))
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
                            cursor.execute(f'''INSERT INTO {data[0]} (time, in_com, out_com) VALUES (?, ?, ?)''', zaps)
                            tabl.commit()
                        client.send(ask.encode('utf-8'))
                        COM_FlAG[data[0]][0] = 'open'
                    else:
                        client.send('<ASK_error - COM error>'.encode('utf-8'))
                except:
                    client.send('<ASK_error - COM error>'.encode('utf-8'))
    except:
        pass

def loop(ser, com_name): # обращение к порту с зацикливанием
    def send_loop():
        while COM_FlAG_loop[com_name][0] == 'message':
            time.sleep(0.5)
        in_text = ''
        while COM_FlAG[com_name][0]:
            try:
                if in_text != COM_FlAG_loop[com_name][0]:
                    in_text = COM_FlAG_loop[com_name][0]
                if ser.isOpen():
                    ser.write(in_text.encode())
            except:
                pass
            time.sleep(0.2)

    def read_loop():
        while COM_FlAG_loop[com_name][0] == 'message':
            time.sleep(0.5)
        out_text = ''
        count = 0
        while COM_FlAG[com_name][0]:
            if ser.read().decode('utf-8') == 'U':
                out_text = "U" + ser.read(size = 30).decode('utf-8')
                if COM_FlAG_loop[com_name][1] != out_text:
                    count += 1
                    COM_FlAG_loop[com_name][1] = out_text + str(count)

            else:
                   pass
            time.sleep(0.1) # задержка при опросе ком порта
    send_lo = threading.Thread(target= send_loop)
    read_lo = threading.Thread(target= read_loop)
    send_lo.start()
    read_lo.start()


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


