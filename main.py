
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time
from time import sleep
import urllib
from stripogram import html2text


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#change filen to what ever

def animate(i):
    pullData = open("filen.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len (eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(float(y))
    ax1.clear()
    plt.axis([-1, float(xar[-1]) + 1,   float(min(yar)) - 1000, float(max(yar)) + 1000])
    ax1.plot(xar,yar)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
