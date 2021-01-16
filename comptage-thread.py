from machine import Pin
from time import sleep
import _thread

led_bleue = Pin(2, Pin.OUT)
bpA = Pin(25, Pin.IN)

led_orange = Pin(19, Pin.OUT)

def comptage():                     # fonction de comptage (bloquant)             
    compt = 0
    while True :
        while not bpA.value():                  # attente de l'appui
            pass                                # ne fait rien
        compt = compt + 1                       # incrementation compteur
        print("Compteur du bpA :",compt)
        led_bleue.value(not led_bleue.value())  # inversion etat de la LED
        sleep(.02)
        while bpA.value():                      # attente du relachement
            pass
        sleep(.02)

def clignotement():                 # fonction de clignotement (bloquante)                 
  while True:
    led_orange.value(not led_orange.value())    # inversion etat de LED
    sleep(.5) 

_thread.start_new_thread(clignotement, ())      # lancement du thread
_thread.start_new_thread(comptage, ())          # lancement du thread 
 