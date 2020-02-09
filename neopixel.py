from machine import Pin, ADC
from neopixel import NeoPixel  # import de la classe NeoPixel du module

n = 8                          # nombre de pixels
p = 26                         # pin de commande du neopixel
np = NeoPixel(Pin(p), n)       # creation de l'instance np
          
np[0] = (30, 0, 0)             # rouge, 30/255 brightness, soit 12%
np[1] = (255, 0, 0)            # rouge, 100% brightness
np[2] = (0, 255, 0)            # vert, 100% brightness
np[3] = (0, 0, 255)            # bleu, 100% brightness
np[4] = (255, 255, 0)          # rouge + vert = jaune
np[5] = (0, 255, 255)          # vert + bleu = cyan
np[6] = (255, 0, 255)          # rouge + bleu = magenta (violet)
np[7] = (255, 255, 255)        # rouge + vert + bleu = blanc
np.write()                     # Ecriture des valeurs sur le ruban


