for valeur_brute in [0, 200, 400, 600, 800, 1023] :
    valeur_corrigee = int((valeur_brute/1023)** 2 * 1023)
    print('valeur brute : {0:4d} ; valeur corrigee : {1:4d} '.format
          (valeur_brute , valeur_corrigee))
