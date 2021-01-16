from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
bp = Pin(25, Pin.IN)
compt = 0
ancien_etat = bp.value()

for cycle in range(500):           # on fait 500 cycles, donc durant 10 s
    etat = bp.value()              # = 1 si on appuie
    if not ancien_etat and etat :  # si front montant
        compt = compt + 1          # on incremente
        print("Compteur :",compt)
        led.value(not led.value()) # basculement de la LED
    sleep(.02)                     # temps de cycle
    ancien_etat = etat             # memorise l'etat de la boucle avant           