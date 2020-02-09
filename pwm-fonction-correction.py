from time import sleep_ms           
from machine import Pin, PWM

led = PWM(Pin(2, Pin.OUT), 500)      # initialise la freqence a 500 Hz

def correction(i, coef) :
    return int ((i / 1023) ** coef * 1023)

for boucle in range(3) :   
    for i in range(0, 1023, 10) :
        led.duty(correction(i, 3.5)) # utilisation fonction correction
        sleep_ms(10)      
led.deinit()
