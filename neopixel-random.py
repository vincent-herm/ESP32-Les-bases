from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel
from random import randint

n = 8                              # nombre de pixels
p = 26                             # pin de commande du neopixel
np = NeoPixel(Pin(p), n)           # creation de l'instance np

x = randint(0,8)                   # tirage aleatoire entre 0 et 8
        
for led in range(0, n):
    np[led] = (0, 0, 255*(led<x))  # = 255 si (led < x) ;  = 0 sinon
np.write()


