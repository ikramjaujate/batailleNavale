class Difficulte:
    def __init__(self):
        """
        Classe définissant la hauteur et le nombre de tours en fonction de la difficulté

        PRE: -
        POST: Renvoie hauteur de la grille et nombre de tours du jeu
        """
        self.haut = 0
        self.tour = 0

    def get_hauteur(self, niveau : str) -> int:
        """Permet d'obtenir la hauteur de la grille
        :param niveau : niveau désiré par l'utilisateur
        :type niveau : str

        PRE: -
        POST: Renvoi la hauteur de la grille

        RAISE : Si utilisateur introduit autre chose que FACILE, MOYEN, DIFFICILE, alors il y a ValueError
        """
        if niveau == "FACILE":
            self.haut = 6
            return self.haut
        elif niveau == 'MOYEN':
            self.haut = 8
            return self.haut
        elif niveau == 'DIFFICILE':
            self.haut = 11
            return self.haut
        else:
            raise ValueError("Introduisez le bon niveau")

    def get_tours(self, niveau : str) -> int:
        """Permet d'obtenir le nombre de tours du jeu
        :param niveau : niveau désiré par l'utilisateur
        :type niveau : str

        PRE: -
        POST: Renvoi le nombre de tours du jeu

        RAISE : Si utilisateur introduit autre chose que FACILE, MOYEN, DIFFICILE, alors il y a ValueError
        """
        if niveau == "FACILE":
            self.tour = 8
            return self.tour
        elif niveau == 'MOYEN':
            self.tour = 12
            return self.tour
        elif niveau == 'DIFFICILE':
            self.tour = 20
            return self.tour
        else:
            raise ValueError("Introduisez le bon niveau")

