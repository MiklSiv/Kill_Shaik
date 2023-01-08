import time


def graf(x_graf, y_graf):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animathion

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    def animate(i):
        #global  x_graf, y_graf
        ax.clear()

        x = x_graf
        y = y_graf
        ax.plot(x, y)

        plt.xlabel("time")
        plt.ylabel("num")
        plt.title('grafic')

    ani = animathion.FuncAnimation(fig, animate, interval=1000)
    plt.show()
    time.sleep(2)