import urllib
from stripogram import html2text
from time import sleep

URL_EOS_BTC = "https://min-api.cryptocompare.com/data/price?fsym=EOS&tsyms=BTC" # EOS to bitcoin
URL_BTC_USD = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD" # Bitcoin to Usd
URL_XLM_BTC ="https://min-api.cryptocompare.com/data/price?fsym=XLM&tsyms=BTC" #Stellar to Bitcoin

# change x < 5 to True if want to last forever
def updateinfo():
    x = 0
    while x < 25:
        sleep(1)
        #BTC to Usd First
        File = open("fileBtcUsd.txt","a")
        myurl = urllib.urlopen(URL_BTC_USD)
        html_string = myurl.read()
        text = html2text(html_string).strip("{}")
        splitText = text.split(":")
        splitText[0] = 1 + x
        splitText[1] = float(splitText[1])
        File.write("\n%s" % str(splitText).strip("[]"))
        File.close()
        File = open("fileEosBtc.txt","a")
        myurl = urllib.urlopen(URL_EOS_BTC)
        html_string = myurl.read()
        text = html2text(html_string).strip("{}")
        splitText = text.split(":")
        splitText[0] = 1 + x
        splitText[1] = float(splitText[1])
        File.write("\n%s" % str(splitText).strip("[]"))
        File.close()
        x += 1
        print x

updateinfo()
