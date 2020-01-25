class Personne :
    def __init__(self, nom, prenom, age, lieu_residence) :
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.lieu_residence = lieu_residence
        
personne1 = Personne("DELUNE", "Claire", 30, "METZ")
personne2 = Personne("CELERT", "Jacques", 32, "NANCY")
print(personne1.age)
print(personne2.lieu_residence)