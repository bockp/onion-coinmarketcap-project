from OmegaExpansion import oledExp
import time

# clear the display, wait 2 seconds then script is over.

ret 	= oledExp.clear()
print "clear return: ", ret
if (ret != 0):
	exit()
# Honestly no idea why it's necessary to wait at the very end of the script.
# they did it in the tutorial I followed to I just did it too XD
time.sleep(2)
