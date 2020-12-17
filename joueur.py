# Classe Joueur
class Joueur:
    """
    :param nom: le nom de l'utilisateur
    :param function: la function de l'utilisateur dans le jeu

    :type nom: string
    :type function : string

    PRE: -
    POST: Assigne à la variable username le nom de l'utilisateur

    RAISES : Si valeur n'est pas de type string, alors il y a TypeError
    """
    def __init__(self, nom : str):
        self.joueurs_points = 0
        try :
            self.username = nom
            if type(self.username) != str:
                raise TypeError("Insérez un string")
        except TypeError as te:
            print(te)

    def getNom(self) -> str:
        '''Obtient le nom de l'utilisateur'''
        return self.username

    def getPoints(self):
        return self.joueurs_points
