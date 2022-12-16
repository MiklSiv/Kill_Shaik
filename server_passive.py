import time
import socket
import threading


SERVER_ADDRESS = ('localhost', 8686)

# Настраиваем сокет
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)
server.listen(10)
print('server is running, please, press ctrl+c to stop')


client, address = server.accept()
client.send('Hello client'.encode('UTF-8'))
print("new connection from {address}".format(address=address))


flag = True

def read():
    global flag
    while flag:
        try:
            data = client.recv(1024)
            print (data.decode('utf-8'))
        except:
            pass
        time.sleep(1)


def send():
    global flag
    while flag:
        try:
            vvod = input()
            if vvod == 'close':
                client.send('server close'.encode('utf-8'))
                client.close()
                print('server close')
                flag = False
                break
            else:
                client.send(vvod.encode('utf-8'))
        except:
            pass
        time.sleep(1)

vvod = threading.Thread(target=read)
vivod = threading.Thread(target=send)
#end = threading.Thread(target=close_connecthion())

vvod.start()
vivod.start()
vivod.join()
vvod.join()

print ('end')