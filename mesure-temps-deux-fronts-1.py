##############   mesure de temps entre 2 fronts   ################
from machine import Pin
from time import sleep, sleep_ms, sleep_us
cont = True

led = Pin(2, Pin.OUT)
bpA = Pin(25, Pin.IN)
bpB = Pin(34, Pin.IN)
compt = 0
    
print("Attente du front montant de bpA")
while not bpA.value():  # attente a l'etat bas du front montant
    pass
led.value(1)
    
print("Attente du front montant de bpB") 
while not bpB.value():  # attente a l'etat bas du front montant
    compt = compt + 1
    sleep_ms(1)
led.value(0)

print("Temps entre deux fronts : {0} ms \n".format(compt))
    


