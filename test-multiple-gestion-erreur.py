def multiple(n, x):
  return (n % x) == 0

try :
  nombre = int(input("Quel est le nombre n a tester ? : "))
  diviseur = int(input("Quel est le diviseur a tester ? : "))

  if multiple(nombre, diviseur) : 
    print("Le nombre {} est multiple de {}.".format(nombre,diviseur))
  else :
    print("Le nombre {} n'est pas multiple de {}".format(nombre,diviseur))

except :
  print("Veuillez saisir des valeurs entieres !")