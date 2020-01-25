class Personne :
    def __init__(self, nom, prenom, age, lieu_residence) :
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.lieu_residence = lieu_residence
    def description(self) :
        print("{1} {0} a {2} ans et habite a {3}.".format(self.nom,
            self.prenom, self.age, self.lieu_residence))
    
personne1 = Personne("DELUNE", "Claire", 30, "METZ")
personne1.description()