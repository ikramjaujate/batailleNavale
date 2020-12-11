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
        if type(nom) == str:
            self.username = nom
        else:
            raise TypeError("Insérez un string")

    def getNom(self) -> str:
        '''Obtient le nom de l'utilisateur'''
        return self.username

#j = Joueur(1)
j = Joueur("ikram")





