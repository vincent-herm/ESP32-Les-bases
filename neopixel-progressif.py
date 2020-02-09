## pour une progression douce entre les LED
from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel     

n = 8                             # nombre de pixels
p = 26                            # pin de commande du neopixel
np = NeoPixel(Pin(p), n)          # creation de l'instance np
coef = 1.5                        # coef pour linearisation sensation lumiere
max = 1000                        # echelle maxi

for x in range (max+1):
    entier = x * n // max   
    frac2 = int((x * n / max - entier) * 255)
    frac1 = 255 - frac2    
    c2 = int((frac2/255)** coef * 255)  ## avec la pente parabolique
    c1 = int((frac1/255)** coef * 255)
    #print("x=",x,"  entier=", entier, "  frac1 =", frac1, 
    #"  c1 =", c1,  "  frac2 =", frac2, "  c2 =", c2)
    if entier != n :              # pour eviter le debordement
        np[entier] = (0, 0, c2)
    if entier > 0 :               # pour eviter d'ecrire a l'index -1
       np[entier-1] = (0, 0, c1)
    np.write()
    sleep(0.01)
    