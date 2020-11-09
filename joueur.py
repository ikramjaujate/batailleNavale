
# Classe Joueur
class Joueur:
    """
    :param nom: le nom de l'utilisateur
    """
    def __init__(self, nom):
        self.username = nom
        self.function = "Capitaine"

    def getNom(self):
        return self.username

    def getFunction(self):
        return self.function

    def __str__(self):
        return "Le nouveau {} est {}, tout le monde à ses ordres !".format(self.function, self.username)

