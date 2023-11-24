from machine import TouchPad, Pin
from time import sleep

tp1 = TouchPad(Pin(15))
led_bleue = Pin(2, Pin.OUT)
compt = 0
seuil = 200
ancien_etat = tp1.read()

for boucle in range (500) :        # duree de la boucle : 10 s
    etat = tp1.read() < seuil      # le test renvoie 1 si on touche
    if etat and not ancien_etat :  # si front montant
        compt = compt + 1          # on incremente
        print("Compteur :",compt)
        led_bleue.value(not led_bleue.value()) # bascule de led_bleue
    ancien_etat = etat             # memorisation ancien etat
    sleep(.02)                     # temps de cycle
