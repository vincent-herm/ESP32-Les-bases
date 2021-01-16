from machine import Pin
from time import sleep, sleep_ms, sleep_us

led_bleue = Pin(2, Pin.OUT)
led_verte = Pin(23, Pin.OUT)
compt = 0

while compt < 4000  :             # on arrete la While apres 4 secondes
    compt +=1                     # on incremente chaque 1000 us
    if compt % 1 == 0 :           # compt % 1 est vrai a chaque boucle 
        led_bleue.value(not led_bleue.value()) # on bascule la LED bleue
    sleep_us(1000)                # temps de cycle 1 ms


