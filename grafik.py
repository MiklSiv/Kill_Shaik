
def grafic_online():
    import matplotlib.pyplot as plt
    import matplotlib.animation as animathion

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    def animate(i):
        global x_graf, y_graf
        ax.clear()
        ax.plot(x_graf, y_graf)

        plt.xlabel("time")
        plt.ylabel("num")
        plt.title('grafic')

    ani = animathion.FuncAnimation(fig, animate, interval=1000)
    plt.show()




grafic_online()