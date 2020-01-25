from machine import Pin
import time 

led = Pin(2, Pin.OUT)       

start = time.ticks_ms()         # memorise la valeur du ticks au lancement

for iteration in range (10000) :
    led.value(1) ; led.value(0)

delta = time.ticks_ms() - start # calcule l'ecart : apres - avant

print ("Temps total pour 10 000 cycles :", delta, "ms")
print ("Temps pour 1 cycle ON/OFF      :" , delta/10, "microsecondes")
