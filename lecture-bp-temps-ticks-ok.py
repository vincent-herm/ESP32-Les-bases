from machine import Pin
from time import sleep, sleep_ms, sleep_us, ticks_ms, ticks_us

led = Pin(2, Pin.OUT)
bp = Pin(25, Pin.IN)

ancien_etat = bp.value()           # initialisation ancien_etat
for t in range(10000):             # duree = 10000 * 0.001 = 10 s
    etat = bp.value()              # lecture etat
    if etat and not ancien_etat :  # condition vrai : front montant
        start = ticks_ms()         # memorisation de start       
    if not etat and ancien_etat :  # condition vrai : front descendant
        stop = ticks_ms()          # stop sur front montant 2        
        delta = stop - start       # calul du temps d'appui  
        print("Temps d'appui : {0} ms".format(delta))
    ancien_etat = etat             # memorisation ancien-etat
    sleep_ms(1)

