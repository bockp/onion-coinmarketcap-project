from OmegaExpansion import oledExp

print 'Starting to use oled-exp functions...'

oledExp.setVerbosity(0)


## initialize the OLED display.
# By putting the commands in the ret variable, it will contain the return value. 0 is OK, 1 means an error occured.
# This is a good way of avoiding continuing your program if, for example, the initialization failed.
ret 	= oledExp.driverInit()
print "driverInit return: ", ret

# test for command failure.
if (ret != 0):
	exit()
