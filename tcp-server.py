import time
import socket
import threading
import  sqlite3 as sq
import grafik

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

    x_graf = []
    y_graf = []

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

def grafic_online():
    import matplotlib.pyplot as plt
    import matplotlib.animation as animathion
    print (211)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    def animate(i):
        #global x_graf, y_graf
        x_graf = [1, 2, 3, 4, 5]
        y_graf = [10, 15, 10,20, 25]
        ax.clear()
        ax.plot(x_graf, y_graf)

        plt.xlabel("time")
        plt.ylabel("num")
        plt.title('grafic')

    ani = animathion.FuncAnimation(fig, animate, interval=1000)
    plt.show()

vvod = threading.Thread(target=read)
end = threading.Thread(target=close_connecthion)
graf = threading.Thread(target=grafik.grafic_online)

vvod.start()
graf.start()
end.start()
#time.sleep(5)
