from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel  # import de la classe NeoPixel du module

n = 8                          # nombre de pixels
p = 26                         # pin de commande du neopixel
delai = .125
np = NeoPixel(Pin(p), n)       # creation de l'instance np

for x in range(0, n):
    np[x] = (0, 0, 255)        # bleu, 100% brightness
    np.write()
    sleep(delai)

for x in range(0,n):
    np[x] = (0, 0, 0)          # eteint
    np.write()
    sleep(delai)