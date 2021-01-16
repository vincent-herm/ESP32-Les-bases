from machine import Pin
from time import sleep, sleep_ms, sleep_us, ticks_ms, ticks_us

bp = Pin(25, Pin.IN)

for t in range(100):        # duree = 100 * 0.1 = 10 s
    if bp.value() :
        print (ticks_ms())
    sleep(0.1)



