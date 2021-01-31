import microcontroller
import time

# The internal thermometer on CircuitPython
# is accessible by using "microcontroller" module

# This simple loop will print the current recorded
# temperature from the internal thermometer of the
# Pico then wait for 1 second, before repeating

while True:
    print(microcontroller.cpu[0].temperature)
    time.sleep(1)

# To test if it's working, try blowing some heat
# on it with your mouth gently ! 
