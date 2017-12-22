
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time
from time import sleep
import urllib
from stripogram import html2text
import numpy
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot

f0 = figure(num = 0, figsize = (12,8))
f0.suptitle("CryptoCurrenty", fontsize=12)
ax01 = subplot2grid((2, 2), (0, 0))
ax02 = subplot2grid((2, 2), (0, 1))

ax01.set_title('BTC - USD')
ax02.set_title('EOS - BTC')

ax01.grid(True)
ax02.grid(True)

ax01.set_xlabel("Time")
ax01.set_ylabel("USD")
ax02.set_xlabel("Time")
ax02.set_ylabel("BTC")

BTCUSD=zeros(0)
EOSBTC=zeros(0)
t=zeros(0)



x = 0.0

def updateData(self):
    global x
    global BTCUSD
    global EOSBTC
    global t
    #BTC to USD
    pullData = open("fileBtcUsd.txt","r").read()
    dataArray = pullData.split('\n')
    try:
        dataArray = dataArray[-20:]
    except:
        pass
    xar = []
    yar = []
    for eachLine in dataArray:
        if len (eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(float(y))

    ax01.set_ylim( float(min(yar)) - 10,float(max(yar)) + 10)
    ax01.set_xlim(float(xar[0]),float(xar[-1]) + 1)
    tmpp1 = yar[-1]
    BTCUSD=append(BTCUSD,tmpp1)
    t=append(t,xar[-1])
    p011, = ax01.plot(t,BTCUSD,'b-', label="1 BTC = %d USD" % float(yar[-1]))
    #EOS TO BTC
    pullData = open("fileEosBtc.txt","r").read()
    dataArray = pullData.split('\n')
    try:
        dataArray = dataArray[-20:]
    except:
        pass
    xar = []
    yar = []
    for eachLine in dataArray:
        if len (eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(float(y))


    ax02.set_ylim( float(min(yar)) - .0005,float(max(yar)) + 0.0005)
    ax02.set_xlim(float(xar[0]),float(xar[-1]) + 1)
    tmpv1 = yar[-1]
    EOSBTC=append(EOSBTC,tmpv1)
    p021, = ax02.plot(t,EOSBTC,'b-', label="1 EOS = %d BTC"% float(yar[-1]))

    ax01.legend([p011], [p011.get_label()])
    ax02.legend([p021], [p021.get_label()])
    p011.set_data(t,BTCUSD)
    p021.set_data(t,EOSBTC)

    return p011, p021

simulation = animation.FuncAnimation(f0, updateData, blit=False, frames=200, interval=1000, repeat=False)
plt.show()
