# Définitions des colonnes et lignes quis eront utilisé dans notre grille
#from batailleNavale.joueur import Joueur

col_header = {0: 'x', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K'}
row_header = {0: 'x', 1: ' 1', 2: ' 2', 3: ' 3', 4: ' 4', 5: ' 5', 6: ' 6', 7: ' 7', 8: ' 8', 9: ' 9', 10: '10',
              11: '11'}

class Ocean:
    def __init__(self, hauteur : int):
        """
        Utilisation : mon_ocean = Ocean(hauteur)
        :param hauteur: la hauteur de la grille

        :type hauteur: int

        PRE : -
        POST : Assigne la valeur hauteur introduite comme paramettre à une autre variable
        """
        self.haut = hauteur

    def get_haut(self) -> int:
        """
        Getter qui permet de prendre la valeur hauteur

        PRE: -
        POST : Renvoi la valeur hauteur
        """
        return self.haut

    def grille(self) -> list:
        """ Création de la grille sous forme de liste

        PRE: -
        POST: Renvoie la grille sous forme de liste
        """
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

        :param gri: la grille qui est utilisé
        :type gri: list

        PRE : -
        POST : Renvoi la grille sous forme de string pour qu'elle soit afficher dans la console

        """
        for ligne in gri:
            print("  ".join(ligne))

    def placer_bateaux(self, grille: list, bateau: int, s: str, ori: str, x: int, y: int) ->list :
        """
        Accepte dans la grille la taille et la position du navire, place le navire, il doit déjà être vérifié by user_place_ships function

        :param grille: grille dans la quelle on place les bateaux
        :param bateau : bateau qui est placer dans la grille
        :param s : première lettre du bateau a placé
        :param ori : orientation du bateau
        :param x : position de la ligne
        :param y : position de la colonne

        :type grille: list
        :type bateau: int
        :type s: str
        :type ori: str
        :type x: int
        :type y: int

        PRE : -
        POST : Place les bateaux dans la grille et renvoi celle-ci
        """
        if ori == "v":
            for i in range(bateau):
                grille[x + i][y] = s
        elif ori == "h":
            for i in range(bateau):
                grille[x][y + i] = s
        return grille

o = Ocean(2)
o.get_haut()
o.grille()
o.placer_bateaux(o.grille(), 1, 'b', "v", 2, 2)