from time import sleep_ms
from machine import Pin, PWM

led = PWM(Pin(2, Pin.OUT), 500)  # initialise la frequence a 500 Hz
bp = Pin(25, Pin.IN)

def correction(i, coef):
    return int((i / 1023) ** coef * 1023)

while True:
    while not bp.value(): pass  # attente de l'appui
    while bp.value(): pass      # attente du relachement

    for i in range(0, 1023, 10):  # allumage de la LED
        led.duty(correction(i, 3.5))  # utilisation fonction correction
        sleep_ms(10)

    while not bp.value():
        pass  # attente de l'appui
    while bp.value():
        pass  # attente du relachement

    for i in range(0, 1023, 10):  # extinction de la LED
        led.duty(correction(1023 - i, 3.5))
        sleep_ms(10)
