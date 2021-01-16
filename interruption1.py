from machine import Pin
from time import sleep

# le parametre pin est fourni par la methode irq lors de l'appel
# ce parametre est la pin qui cause l'interruption
def gestion_interrupt(pin):                  # fonction d'interruption
    led_bleue.value(not led_bleue.value())   # bascule l'etat de LED bleue
    print('Interruption causee par :', pin)  # affiche la pin en cause 
  
bpA = Pin(25, Pin.IN)
led_bleue = Pin(2, Pin.OUT)

# configure l'interruption sur le front montant de bpA,
# et renvoie vers la fonction gestion_interrupt pour son traitement
bpA.irq(trigger=Pin.IRQ_RISING, handler = gestion_interrupt)  

compt = 0
while True:                 # boucle principale qui compte les 0.25 s
    compt = compt + 1
    print(compt)
    sleep(0.25)




