# Classe Joueur
class Joueur:
    """
    :param nom: le nom de l'utilisateur
    :param function: la function de l'utilisateur dans le jeu

    :type nom: string
    :type function : string
    """
    def __init__(self, nom : str):
        self.username = nom

    def getNom(self) -> str:
        '''Obtient le noms de l'utilisateur'''
        return self.username


