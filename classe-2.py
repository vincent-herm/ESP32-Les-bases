class Personne :
    def __init__(self) :
        self.nom = ""
        self.prenom = ""
        self.age = "0"
        self.lieu_residence = ""
        
personne1 = Personne()
personne1.nom = "DELUNE"
personne1.prenom = "Claire"
personne1.age = "30"
personne1.lieu_residence = "METZ"

print(personne1.age)