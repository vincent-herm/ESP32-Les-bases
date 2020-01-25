x = 20  
y = 70
diviseurs_x=[]    # creation liste vide pour diviseurs de x
diviseurs_y=[]    # creation liste vide pour diviseurs de y

# creation d'une fonction pour trouver les elements communs a deux listes
def inter(liste1, liste2):  
   liste_elements_communs = [value for value in liste1 if value in liste2]
   return liste_elements_communs

for a in range (1,max(x,y)+1):
    if x % a == 0 :            # si x est divisible par a
        diviseurs_x.append(a)  # ajout a la liste des diviseurs de x
    if y % a == 0 :            # si y est divisible par a
        diviseurs_y.append(a)  # ajout a la liste des diviseurs de y 
diviseurs_communs = inter(diviseurs_x, diviseurs_y)
plus_grand_commun_diviseur = max(diviseurs_communs)  # retourne le maxi 

print("x = ", x, "; y = ", y)
print ("Liste des diviseurs de x :",diviseurs_x)
print("Liste des diviseurs de y :",diviseurs_y)
print("Liste des diviseurs communs : ", diviseurs_communs)
print("PGCD : ", plus_grand_commun_diviseur)