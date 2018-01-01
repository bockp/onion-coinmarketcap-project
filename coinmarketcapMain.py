from OmegaExpansion import oledExp
import time

from coinmarketcap import Market



print 'Starting to use oled-exp functions...'

oledExp.setVerbosity(0)


# initialize
ret 	= oledExp.driverInit()
print "driverInit return: ", ret
if (ret != 0):
	exit()

# write a message

coinmarketcapM = Market()
eth-ticker = coinmarketcap.ticker("ethereum", limit=3)
steem-ticker = coinmarketcap.ticker("steem", limit=3)
smartcash-ticker = coinmarketcap.ticker("smartcash", limit=3)

ethUSD = eth-ticker[0]["price_usd"]
steemUSD = steem-ticker[0]["price_usd"]
smartcashUSD = smartcash-ticker[0]["price_usd"]

ret 	= oledExp.write("Ethereum price: " + ethUSD + "$\n" +
                        "Steem price: " +  steemUSD + "$\n" +
                        "SmartCash price: " + smartcashUSD + "$\n")
print "write return: ", ret
if (ret != 0):
	exit()
time.sleep(4)


# clear the display
ret 	= oledExp.clear()
print "clear return: ", ret
if (ret != 0):
	exit()
time.sleep(2)
