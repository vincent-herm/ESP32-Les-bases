from machine import Pin
import time

led = Pin(2, Pin.OUT)

while True:
    led.value(1)          # on allume la LED    
    time.sleep(0.5)       # delai de 0.5 s
    led.value(0)          # on eteint la LED    
    time.sleep(0.5)       # delai de 0.5 s

#while True:
#    if led.value() == 1 :         # si la LED est allumee...
#        led.value(0)              # on l'eteint
#    else :                        # sinon (elle est eteinte)...
#        led.value(1)              # on l'allume       
#    time.sleep(0.5)               # delai de 0.5 s entre 2 boucles (1 Hz)

#while True:
#    led.value(not led.value()) ;  # inversion de l'etat de la LED
#    time.sleep(0.5)               # delai de 0.5 s entre 2 boucles (1 Hz)
   