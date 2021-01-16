from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
bp = Pin(25, Pin.IN)
compt = 0

for t in range(500):               # le programme s'arrete au bout de 10 s
    if bp.value() :
        compt = compt + 1          # inversion de l'etat de la LED
        print ("compteur", compt)  # affiche le compt si le bp est presse
        led.value(not led.value()) # basculement de la LED
    sleep(.02)    
    
