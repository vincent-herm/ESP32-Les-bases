from time import sleep_ms           
from machine import Pin, PWM

led = PWM(Pin(2, Pin.OUT), 500)    # Initialise la freq : 500 Hz

for boucle in range(3) :   
    for i in range(0, 1023, 10) :  # de 0 a 1023 par pas de 10
        led.duty(i)
        sleep_ms(10)      
led.deinit()                       # liberation des ressources du PWM

    