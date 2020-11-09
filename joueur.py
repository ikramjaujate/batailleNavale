# Classe Joueur
class Joueur:
    """
    :param nom: le nom de l'utilisateur
    :param function: la function de l'utilisateur dans le jeu

    :type nom: string
    :type function : string
    """
    def __init__(self, nom):
        self.username = nom
        self.function = "Capitaine"

    def getNom(self):
        '''Obtient le noms de l'utilisateur'''
        return self.username

    def getFunction(self):
        '''Obtient la function de l'utilisateur'''
        return self.function

    def __str__(self):
        return "Le nouveau {} est {}, tout le monde à ses ordres !".format(self.function, self.username)

