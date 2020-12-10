class Difficulte:
    def __init__(self):
        """
        Classe définissant la hauteur et le nombre de tours en fonction de la difficulté
        """
        self.haut = 0
        self.tour = 0

    def get_hauteur(self, niveau : str) -> int:
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

d = Difficulte()
# d.tour
# d.haut
# d.get_tours("FACILE")
# d.get_hauteur("FACILE")
# d.get_tours("tonto")