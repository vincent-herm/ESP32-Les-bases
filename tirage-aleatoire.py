from random import randint
 
liste=[]
 
for i in range(20):        # pour 20 nombres...
    tirage = randint(0,8)  # tirage entre 0 et 8
    liste.append(tirage)   # ajout a la liste des tirages
 
print(liste)             
liste.sort()               # classement de la liste dans l'ordre croissant
print(liste)
