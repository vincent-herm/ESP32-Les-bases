def pgcd(a,b):               # Version 1 (de base)
    while b != 0 :
        r = a % b
        print(a, b, r)
        a,b = b,r
    return a
print (pgcd(70,20))          

#def pgcd(a,b) :             # Version 2 (simplifiee)
#    while b != 0 :
#        a , b = b , a % b
#    return a

#def pgcd(a,b):              # Version 3 (avec recursivite)
#    if b == 0 :
#        return a
#    else:
#        r = a % b
#        return pgcd(b,r)    