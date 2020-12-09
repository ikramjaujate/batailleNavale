# Classe Joueur
class Joueur:
    """
    :param nom: le nom de l'utilisateur
    :param function: la function de l'utilisateur dans le jeu

    :type nom: string
    :type function : string
    """
    def __init__(self, nom : str):
        if type(nom) == str:
            self.username = nom
        else:
            raise ValueError("Insérez un string")

    def getNom(self) -> str:
        '''Obtient le noms de l'utilisateur'''
        return self.username


