def multiple(n, x):
    return (n % x) == 0

nombre = int(input("Quel est le nombre n a tester ? : "))
diviseur = int(input("Quel est le diviseur a tester ? : "))

if multiple(nombre, diviseur) :      
  print("Le nombre {0} est multiple de {1}, car la division de {0} par {1} donne {2}, et le reste est nul.".format(nombre, diviseur, int(nombre/diviseur)))
else :
  print("Le nombre {0} n'est pas multiple de {1} car la division de {0} par {1} donne {2}, et le reste vaut {3}.".format(nombre, diviseur, int(nombre/diviseur), nombre%diviseur))