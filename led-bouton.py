from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
bouton = Pin(25, Pin.IN)
    
while True :
    if bouton.value() :
        led.value(1)
    else :
        led.value(0)
    sleep(0.1)

#while True :
#    led.value(bouton.value())
#    sleep(0.1)
