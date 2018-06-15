class Banane:

    def __init__(self, couleur):
        self.couleur = couleur

class Singe(Banane):

    def __init__(self, nom, couleur):
        Banane.__init__(self, couleur)
        self.nom = nom

    def __str__(self):
        return "{0} mange la banane {1}".format(self.nom, self.couleur)


print(Singe("Pierre", "Jaune"))
print(Singe("Marie", "Verte"))