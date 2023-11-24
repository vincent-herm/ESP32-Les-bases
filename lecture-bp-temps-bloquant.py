from machine import Pin
from time import sleep

bp = Pin(25, Pin.IN)
compt_temps = 0

for t in range(5):           # on fait juste 5 cycles appui/relachement
    while not bpB.value() :  # on attend l'appui sur le bp   
        sleep(.02)           # on attend 20 ms, 50 boucles/s suffisant
    compt_temps = 0   
    while bpB.value() :      # on attend l'appui sur le bp   
        compt_temps += 1     # on incremente toutes les 20 ms
        sleep(.02)           # delai entre deux boucles   
    print("Compteur : {0:2d}, soit : {1:2f} s".\
          format(compt_temps, compt_temps/50))
