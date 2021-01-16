from machine import Pin, ADC
from neopixel import NeoPixel  # import de la classe NeoPixel du module

n = 8                          # nombre de pixels
p = 26                         # pin de commande du neopixel
np = NeoPixel(Pin(p), n)       # creation de l'instance np
          
np[0] = (10, 0, 0)            # rouge, 10/255 brightness, soit 4%
np[1] = (40, 0, 0)            # rouge, 40/255 brightness, soit 16%
np[2] = (0, 40, 0)            # vert, 40/255 brightness, soit 16%
np[3] = (0, 0, 40)            # bleu, 40/255 brightness, soit 16%
np[4] = (40, 40, 0)           # rouge + vert = jaune
np[5] = (0, 40, 40)           # vert + bleu = cyan
np[6] = (40, 0, 40)           # rouge + bleu = magenta (violet)
np[7] = (40, 40, 40)          # rouge + vert + bleu = blanc
np.write()   


