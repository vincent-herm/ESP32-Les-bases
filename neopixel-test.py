from machine import Pin, ADC
from neopixel import NeoPixel  # import de la classe NeoPixel du module

n = 8                          # nombre de pixels
p = 26                         # pin de commande du neopixel
np = NeoPixel(Pin(p), n)       # creation de l'instance np
          
np[0] = (10, 0, 0)             # rouge, 10/255 brightness, soit 4%
np[1] = (0, 10, 0)             # vert, 10/255 brightness, soit 4%
np[2] = (0, 0, 10)             # bleu, 10/255 brightness, soit 4%
np[3] = (10, 10, 10)           # blanc = rouge + vert + bleu
np[4] = (50, 0, 0)             # rouge, 50/255 brightness, soit 20%
np[5] = (0, 50, 0)             # vert, 50/255 brightness, soit 20%
np[6] = (0, 0, 50)             # bleu, 50/255 brightness, soit 20%
np[7] = (50, 50, 50)           # blanc = rouge + vert + bleu
np.write()                     # Ecriture des valeurs sur le ruban


