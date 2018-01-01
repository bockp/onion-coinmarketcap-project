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
eth-ticker = coinmarketcap.ticker("ethereum", limit=3, convert='EUR')

ret 	= oledExp.write("Ethereum price", eth-ticker[0]["price_eur"])
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
