from machine import TouchPad, Pin
from time import sleep

tp1 = TouchPad(Pin(15))
led_bleue = Pin(2, Pin.OUT)
compt = 0
seuil = 100
ancien_etat = tp1.read()

for boucle in range (10) :         # on fait juste 10 cycles, et on arrete
    while not tp1.read() < seuil : # on attend l'appui sur le touch pad
        pass                       # on ne fait rien, mais il faut le dire
    compt = compt + 1
    print("Compteur :",compt)
    led_bleue.value(not led_bleue.value())     # basculement de led_bleue
    while tp1.read() < seuil :     # on attend l'appui sur le touch pin   
        pass                       # on ne fait rien, mais il faut le dire