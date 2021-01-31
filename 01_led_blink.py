import board
import time
from digitalio import DigitalInOut, Direction

# GP25 correspond to GPIO25
# it is the corresponding GPIO
# for controlling the onboard LED

led = DigitalInOut(board.GP25)

# We need to specify that this GPIO
# is an output, we use Direction

led.direction = Direction.OUTPUT

# A simple loop that will turn on
# the led (True) wait for 0.2 seconds
# then turn it off (False) and wait
# again for 0.2 seconds, before repeat

while True:
    led.value = True
    time.sleep(0.2)
    led.value = False
    time.sleep(0.2)

# You should now see your LED blinking !

# There is an other way to make your LED blink
# it's by using 'not' instead of defining every
# time the needed value of your LED, when in this
# case you just want the value which she's not

# For example if your LED is on value 'false'
# (turned off), what you want is the other value
# 'true' (turned on). Code implementation :  

# While True:
#     led.value = not led.value
#     time.sleep(0.2)
