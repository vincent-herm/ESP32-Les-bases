from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel     

n = 8                              # nombre de pixels
p = 26                             # pin de commande du neopixel
np = NeoPixel(Pin(p), n)           # creation de l'instance np

x = int(input("Combien voulez vous de LED allumees ? : "))
        
for led in range(0, n):
    np[led] = (0, 0, 20*(led<x))  # = 255 si (led < x) ;  = 0 sinon
np.write()


