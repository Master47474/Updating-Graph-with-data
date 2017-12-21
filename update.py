import urllib
from stripogram import html2text
from time import sleep

# change x < 5 to True if want to last forever
def updateinfo():
    x = 0
    while x < 5:
        sleep(5)
        File = open("filen.txt","a")
        myurl = urllib.urlopen("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR&e=Coinbase&extraParams=your_app_name")
        html_string = myurl.read()
        text = html2text(html_string).strip("{}")
        splitText = text.split(",")[0].split(":")
        splitText[0] = 1 + x #splitText[0].strip("\"\"")
        #splitText[0] = splitText[0].strip("\'\'")
        splitText[1] = float(splitText[1]) - (x**5)
        """ doing the - x**10 to see if how it looks when it drastcially changes """
        print splitText
        File.write("\n%s" % str(splitText).strip("[]"))
        File.close()
        x += 1

updateinfo()
