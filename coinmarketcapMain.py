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

coinmarketcap = Market()
eth_ticker = coinmarketcap.ticker("ethereum", limit=3)
steem_ticker = coinmarketcap.ticker("steem", limit=3)
smartcash_ticker = coinmarketcap.ticker("smartcash", limit=3)

ethUSD = eth_ticker[0]["price_usd"]
steemUSD = steem_ticker[0]["price_usd"]
smartcashUSD = smartcash_ticker[0]["price_usd"]

ret 	= oledExp.write("Ethereum price: " + ethUSD + "$\n" +
                        "Steem price: " +  steemUSD + "$\n" +
                        "SmartCash price: " + smartcashUSD + "$\n") # need to write these 3 one by one on separate lines ?
                        # also, need to reduce num of significant digits...
print "write return: ", ret
if (ret != 0):
	exit()
time.sleep(10)


# clear the display
ret 	= oledExp.clear()
print "clear return: ", ret
if (ret != 0):
	exit()
time.sleep(2)
