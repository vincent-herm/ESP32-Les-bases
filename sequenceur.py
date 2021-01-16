from machine import Pin
from time import sleep

led_bleue = Pin(2, Pin.OUT)
led_verte = Pin(18, Pin.OUT)

while True:
    led_bleue.on()  ; sleep(0.25)
    led_verte.on()  ; sleep(0.25)
    led_bleue.off() ; sleep(0.25)
    led_verte.off() ; sleep(0.25)    
