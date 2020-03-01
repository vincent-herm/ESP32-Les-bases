from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
bp = Pin(25, Pin.IN)

compt = 0 
while True :   
    if bp.value() : compt = 20     
    led.value(compt > 0)   # si compt > 0, cela fait led.value(True) 
    sleep(0.1)
    compt -= (compt > 0)   # raccourci pour : compt = compt - (compt > 0)