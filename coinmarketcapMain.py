from OmegaExpansion import oledExp
import time

from coinmarketcap import Market


# these print statements appear in your console.
print 'Starting to use oled-exp functions...'

oledExp.setVerbosity(0)


## write a message

# get's the ticker information for each coin.
coinmarketcap = Market()
eth_ticker = coinmarketcap.ticker("ethereum", limit=3)
steem_ticker = coinmarketcap.ticker("steem", limit=3)
smartcash_ticker = coinmarketcap.ticker("smartcash", limit=3)

# information is stored as [{...}], so to access it you need to first access list item 0 (the Dic),
#then use the key you want to extract.

ethUSD = eth_ticker[0]["price_usd"]
steemUSD = steem_ticker[0]["price_usd"]
smartcashUSD = smartcash_ticker[0]["price_usd"]

# Write the ticker symbol, price in USD, and dollar sign to display at coords (0,0).
ret1 	= oledExp.write("ETH: " + ethUSD + "$")
# Move cursor (where any write commands are executed) to position (1,0), AKA., move down 2 lines.
oledExp.setCursor(2, 0)
ret2	= oledExp.write("STEEM: " + steemUSD + "$")
oledExp.setCursor(4, 0)
ret3    = oledExp.write("SMART: " + smartcashUSD + "$")

# test that every write statement was a success, else exit script.
print "write return: ", ret1,ret2,ret3
if (ret1 != 0 or ret2 != 0 or ret3 !=0):
	exit()
