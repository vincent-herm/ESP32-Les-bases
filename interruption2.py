from machine import Pin
from time import sleep

# le parametre pin est fourni par la methode irq lors de l'appel
# ce parametre est la pin qui cause l'interruption
def gestion_interrupt(pin):                 # fonction d'interruption
    led_bleue.value(not led_bleue.value())  # bascule l'etat de LED bleue
    global inter                    # definition de la variable globale             
    inter = True                    # la variable globale est mise a True
    global interrupt_pin            # definition de la variable globale  
    interrupt_pin = pin             # correspond a la pin d'interruption
  
bpA = Pin(25, Pin.IN)
led_bleue = Pin(2, Pin.OUT)

# configure l'interruption sur le front montant de bpA,
# et renvoie vers la fonction gestion_interrupt pour son traitement
bpA.irq(trigger=Pin.IRQ_RISING, handler = gestion_interrupt)  

compt = 0
inter = False

while True:                 # boucle principale qui compte les 0.25 s
    compt = compt + 1
    print(compt)
    if inter :
        print('Interruption causee par :', interrupt_pin)  
        inter = False
    sleep(.25)
