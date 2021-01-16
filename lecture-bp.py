from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
bp = Pin(25, Pin.IN)

for t in range(500):    # pour que le code s'arrete au bout de 10 s
    led.value(bp.value()) 
    sleep(.02)
    
#for t in range(500):   # autre ecriture pour la meme chose
#    if bp.value() :
#        led.value(1)
#    else :
#        led.value(0)
#    sleep(.02)    
    
