from time import sleep_ms           
from machine import Pin, PWM

led = PWM(Pin(2, Pin.OUT), 500)    # Initialise la freq a 500 Hz  

for boucle in range(3) :   
    for i in range(0, 1023, 10) :
        led.duty(int((i/ 1023)** 2 * 1023))
        sleep_ms(10)      
led.deinit()    