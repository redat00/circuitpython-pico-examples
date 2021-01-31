import time
import board
from digitalio import DigitalInOut, Direction

# For this example you will need to connect
# 3 LED onto your Pico. You can choose whatever
# color please you, but I'd recommand using 
# Red, Yellow/Amber (or Orange if you have some!) 
# and Green. 

# Remember to put a resistor before your LEDs! 
# 330ohm should be good. 

# We start by defining each LED for each GPIO 
# it is connected on. This may vary regarding 
# how you wired everything on your Pico.

led_green = DigitalInOut(board.GP15)
led_yellow = DigitalInOut(board.GP13)
led_red = DigitalInOut(board.GP14)

# We set all of those GPIO as output.

led_green.direction = Direction.OUTPUT 
led_yellow.direction = Direction.OUTPUT
led_red.direction = Direction.OUTPUT

# A simple loop that will turn on (True) the green 
# LED for 7 seven second, then turn it off, and turn
# on the yellow one for 2 second. It will then
# finally turn off the yellow one, and turn on the
# red one, before repeating herself all the way up.

while True:
    led_green.value = True
    time.sleep(7)
    led_green.value = False
    led_yellow.value = True
    time.sleep(2)
    led_yellow.value = False
    led_red.value = True
    time.sleep(7)
    led_red.value = False

# This system should replicate what a real traffic 
# light is actually doing. Of course you can adjust
# all sleep time to make it more real!
