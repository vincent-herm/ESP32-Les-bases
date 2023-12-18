from machine import I2C, Pin
from time import sleep
OLED = 0                                # 1 : 1.3 pouces, 0 : 0.96 pouces

# choix de la bibliotheque en fonction du type d'ecran OLED
if OLED == 1 :                             
    from ssd1306 import SSD1306_I2C     # module pour commander le OLED
    i2c = I2C(-1, Pin(22), Pin(21))     # pin SCK et SDA du OLED
    display = SSD1306_I2C(128, 64, i2c) # declaration taille ecran, pins
else :
    from sh1106 import SH1106_I2C
    i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
    display = SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
    display.sleep(False)

bp = Pin(25, Pin.IN)                   # poussoir sur pin 25 pour passer

# fonction pour attendre l'appui+relach. pour passer au graphique suivant
def attend_appui():
    while bp.value() == False : pass ; sleep(.02) # attend appui poussoir
    while bp.value() == True : pass ; sleep(.02)  # attend le relachement
        
display.fill(0)                  # Remplit l'afficheur avec 0 -> OFF
display.show()                   # Mise a jour de l'affichage (envoie)

display.text("Presse Poussoir !", 1, 10, 1)
display.show() ; attend_appui()  # la fonction attend l'appui/relachement

display.fill(1)                  # Remplit l'afficheur avec 1 -> ON
display.show() ; attend_appui()

display.fill(0)                  # Remplit l'afficheur avec 0 -> OFF
display.show() ; attend_appui()

# Affiche le texte en 1, 0 (x,y), et etat : 1 (blanc). (0 : noir)
display.text("Hello World !", 1, 0, 1) 
display.show() ; attend_appui()
    
display.contrast(50)             # contraste mis a 50 sur max = 255
attend_appui()

display.contrast(255)            # contraste maxi
attend_appui()

display.invert(1)                # inversion sortie (fond blanc) 
attend_appui()

display.invert(0)                # remise affichage normal
attend_appui()

# Affiche le texte en 1, 10 (x,y), et 1 signifie en blanc (0 : noir)
display.text("Tu vas bien ?", 1, 10, 1)
display.show() ; attend_appui()

# Affiche le texte en 1, 20 (x,y), et 1 signifie en blanc (0 : noir)
display.text("Estoy muy biene", 1, 20, 1)
display.show() ; attend_appui()

# Cela ecrit en couleur 0 (noir) le meme texte, donc ca l'efface 
display.text("Tu vas bien ?", 1, 10, 0)  
display.show() ; attend_appui()

# La hauteur d'une lettre est de 7 pixels
# On aurait pu afficher sur la ligne 8 et non 10, soit 1 pixel d'ecart
display.text("Tu vas bien ?", 1, 8, 1)  
display.show() ; attend_appui()

# On aurait aussi pu afficher sur la ligne 7, mais on touche !
display.text("Tu vas bien ?", 1, 8, 0)  # on efface
display.text("Tu vas bien ?", 1, 7, 1)  # on ecrit trop pres !!
display.show() ; attend_appui()

display.fill(0)  # Efface tout
display.show() ; attend_appui()

# Mets le pixel 3, 4 (x, y) a 1 (allume)
# .pixel(x,y,c)
display.pixel(127, 31, 1)  
display.show() ; attend_appui()

# Retourne la valeur a 127,31 (x,y)
# .pixel(x,y,c)
c = display.pixel(127, 31)  # affiche l'etat 1 ou 0 du pixel (x,y)
print("Etat du pixel :", c)
display.text("...voir shell... !", 1, 10, 1)
display.show() ; attend_appui()


c = display.pixel(126, 30) # affiche l'etat 1 ou 0 du pixel (x,y)
print("Etat du pixel :", c)
display.text("...encore... !", 1, 20, 1)
display.show() ; attend_appui()

# Trace une ligne horizontale, d'origine 0,0 (x,y),
    # de longueur l= 128 (vers la droite)
# .hline(x,y,l,c)
display.fill(0)  # Efface tout
display.hline(0, 0, 128, 1)  
display.show() ; attend_appui()

# Trace une ligne verticale, d'origine 0,0 (x,y),
    # de hauteur h= 63 (vers le bas)
# .hline(x,y,h,c)
display.vline(0, 0, 63, 1)
display.show() ; attend_appui()

# Trace une ligne, d'origine 0,63 (x1,y1), d'extremite 127,0 (x1,y1)
# .line(x1,y1,x2,y2,c)
display.line(0, 63, 127, 0, 1)
display.show() ; attend_appui()

# Trace un rectangle vide, d'origine 4,4 (x,y), de dimensions 68,28 (l,h)
# .rect(x,y,l,h,c)
display.rect(4, 4, 60, 28, 1)
display.show() ; attend_appui()

# Trace un rectangle plein, d'origine 4,36 (x,y), de dimensions 20,15 (l,h)
# .fill_rect(x,y,l,h,c)
display.fill_rect(4, 36, 20, 15, 1)
display.show() ; attend_appui()

# Pour de simples graphiques, nous pouvons creer une matrice, qui contient 
# les elements de notre icone, comme celui-ci par exemple :
ICON = [
    [ 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],]

display.fill(0)                      # Efface tout 
x0, y0 = 60, 12
for y, row in enumerate(ICON):       # prendre chaque ligne
    for x, c in enumerate(row):      # et prendre chaque colonne
        display.pixel(x0+x, y0+y, c) # pixel = 1 ou 0, centre (x0,y0)
display.show()
attend_appui()

for x in range(1,74):
  display.scroll(-1, 0)
  display.show()
  sleep(.01)
attend_appui()

display.text("C'est fini !", 1, 10, 1)
display.show() ; attend_appui()
