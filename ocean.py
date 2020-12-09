# Définitions des colonnes et lignes quis eront utilisé dans notre grille
from batailleNavale.joueur import Joueur

col_header = {0: 'x', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K'}
row_header = {0: 'x', 1: ' 1', 2: ' 2', 3: ' 3', 4: ' 4', 5: ' 5', 6: ' 6', 7: ' 7', 8: ' 8', 9: ' 9', 10: '10',
              11: '11'}

'''Classe Ocean'''


class Difficulte:
    def __init__(self):
        """
        Classe définissant la hauteur et le nombre de tours en fonction de la difficulté
        """
        self.haut = 0
        self.tour = 0

    def get_hauteur(self, niveau):
        if niveau == "FACILE":
            self.haut = 6
            return self.haut
        elif niveau == 'MOYEN':
            self.haut = 8
            return self.haut
        elif niveau == 'DIFFICILE':
            self.haut = 11
            return self.haut

    def get_tours(self, niveau):
        if niveau == "FACILE":
            self.tour = 8
            return self.tour
        elif niveau == 'MOYEN':
            self.haut = 12
            return self.tour
        elif niveau == 'DIFFICILE':
            self.haut = 20
            return self.tour


class Ocean:
    def __init__(self, hauteur):
        """
        Utilisation : mon_ocean = Ocean(hauteur)
        :param hauteur:
        :return: un ocean
        """
        self.haut = hauteur


    def get_haut(self):
        return self.haut

    def grille(self) -> list:
        ma_grille = []
        calcule = self.haut + 1
        for x in range(calcule):
            ma_grille.append(["."] * calcule)

        for i in range(0, len(ma_grille)):
            ma_grille[0][0] = "  "
            ma_grille[0][i] = col_header[i]  # col
            ma_grille[i][0] = row_header[i]  # row

        return ma_grille

    def print_grille(self, gri: list):
        """
        Function qui permet de afficher la grille en console

        :param gri: list
        :return: Return la grille sous forme de string dans la console
        """
        for ligne in gri:
            print("  ".join(ligne))

