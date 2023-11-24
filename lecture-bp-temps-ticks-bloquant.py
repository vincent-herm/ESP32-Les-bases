from machine import Pin
from time import sleep, sleep_ms, sleep_us, ticks_ms, ticks_us
cont = True

bp = Pin(25, Pin.IN)

for t in range(5):           # on fait juste 5 cycles appui/relachement
    while not bp.value() :   # on attend l'appui sur le bp   
        pass                 # pas besoin de tempo
    start = ticks_ms()       # memorisation de start lors du front montant        
    while bp.value() :       # on attend l'appui sur le bp   
        pass                 # pas besoin de tempo    
    stop = ticks_ms()        # stop sur front montant 2        
    delta = stop - start   
    print("Temps d'appui : {0} ms".format(delta))
