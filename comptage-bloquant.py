from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
bp = Pin(25, Pin.IN)
compt = 0

for cycle in range(10):        # on fait juste 10 cycles appui/relachement
    while not bp.value() :     # on attend l'appui sur le bp   
        pass                   # on ne fait rien, mais il faut le dire
    compt = compt + 1
    print("Compteur :",compt)
    led.value(not led.value()) # basculement de la LED
    sleep(0.02)                # delai pour supprimer les rebonds du bp
    while bp.value() :         # on attend l'appui sur le bp   
        pass                   # on ne fait rien, mais il faut le dire
    sleep(.02)                 # delai pour supprimer les rebonds du bp