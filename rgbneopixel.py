import machine 
import time
import neopixel

PIN = 4
NUM_PIX = 3
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_PIX)
np[0] = (100,50,20)
np.write()