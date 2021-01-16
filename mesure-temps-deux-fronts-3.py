##############   mesure de temps entre 2 fronts   ################
from machine import Pin
from time import sleep, sleep_ms, sleep_us, ticks_ms, ticks_us
cont = True

led = Pin(2, Pin.OUT)
bpA = Pin(25, Pin.IN)
bpB = Pin(34, Pin.IN)

print("Attente de l'etat BAS de A")
while bpA.value():      # attente a l'etat haut 
    pass  
    
print("Attente du front montant de bpA")
while not bpA.value():  # attente a l'etat bas
    pass
start = ticks_ms()      # start sur front montant 1
led.value(1)
    
print("Attente de l'etat BAS de B")    
while  bpB.value():     # attente a l'etat haut
    pass

print("Attente du front montant de bpB") 
while not bpB.value():  # attente a l'etat bas
    pass     
stop = ticks_ms()       # stop sur front montant 2
led.value(0)
    
delta = stop - start   
print("Temps entre deux fronts : {0} ms \n".format(delta))
    


