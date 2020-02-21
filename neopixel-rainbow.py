from machine import Pin, ADC
from time import sleep_ms
from neopixel import NeoPixel

n = 8                              # nombre de pixels
p = 26                             # pin de commande du neopixel
np = NeoPixel(Pin(p), n)           # creation de l'instance np

def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(n):
            rc_index = (i * 256 // n) + j
            np[i] = wheel(rc_index & 255)
        np.write()
        sleep_ms(wait)

while True :
    rainbow_cycle(1)
    
