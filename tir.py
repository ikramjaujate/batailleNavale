import random
from batailleNavale.jeu_console import hauteur
class Tir:

    def tir(self, grille, x: int, y: int) -> str:
        etat = ""
        if grille[x][y] == ".":
            etat += "rate"
            return etat
        elif grille[x][y] == "*" or grille[x][y] == "X":
            etat += "toucheAvant"
            return etat
        else:
            etat += "touche"
            return etat

    def utilisateur_tir(self, grille: list, tableau, grille_affiche, points: int):
        while True:
            print("Capitaine, ou voulez vous tiré ?")
            x, y = b.get_coordonnes()
            tir = self.tir(grille, x, y)
            if tir == "rate":
                print("Capitaine, vous avez rate le tir")
                grille[x][y] = "*"
                grille_affiche[x][y] = "*"
            elif tir == "toucheAvant":
                print("Capitaine, vous avez déjà touché")
            elif tir == "touche":
                points += 1
                print("Bravo capitaine, vous avez touché le bateau")
                grille[x][y] = "X"
                grille_affiche[x][y] = "X"
                if tir == "touche":
                    grille[x][y] = 'X'
                    for liste in tableau:
                        for element in liste:
                            if (x, y) == element:
                                liste.remove((x, y))

            if tir != "toucheAvant":
                return grille

    def tir_ordinateur(self, grille: list, tableau, points: int):
        """
        générer des coordonnées aléatoires pour que l'ordinateur réalise les mouvements
        """
        while True:
            x = random.randint(1, hauteur)
            y = random.randint(1, hauteur)
            tir = self.tir(grille, x, y)
            if tir == "touche":
                points += 1
                print("NOOOOON !!! MOUSSAILLON, ILS ONT TOUCHÉ UN DE NOS BATEAUX ! ")
                grille[x][y] = 'X'
                for liste in tableau:
                    for element in liste:
                        if (x, y) == element:
                            liste.remove((x, y))
            elif tir == "rate":
                print("HIHI, ils ont touché la balaine ")
                grille[x][y] = "*"
            return grille
