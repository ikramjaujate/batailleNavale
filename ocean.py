#Définitions des colonnes et lignes quis eront utilisé dans notre grille
col_header = {0: 'x', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K'}
row_header = {0: 'x', 1: ' 1', 2: ' 2', 3: ' 3', 4: ' 4', 5: ' 5', 6: ' 6', 7: ' 7', 8: ' 8', 9: ' 9', 10: '10', 11:'11'}

class Ocean:
    def __init__(self, hauteur, largeur):
        """
        Utilisation : mon_ocean = Ocean(hauteur, largeur)
        :param hauteur:
        :param largeur:
        :return: un ocean
        """
        self.haut = hauteur
        self.larg = largeur

    def grille(self):
        ma_grille = []
        calcule = self.haut + 1
        for x in range(calcule) :
            ma_grille.append(["."] * calcule)

        for i in range(0, len(ma_grille)):
            ma_grille[0][0] = "  "
            ma_grille[0][i] = col_header[i]  # col
            ma_grille[i][0] = row_header[i]  # row


        return ma_grille

