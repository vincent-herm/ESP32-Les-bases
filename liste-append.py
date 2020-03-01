ma_liste = []
for x in range(1,11) :
    if (x % 5) != 0 :          # si x n'est pas multiple de 5 :
        ma_liste.append(x**2)  # ajout de x**2 a la liste en construction
for element in ma_liste :
    print(element , end="-")