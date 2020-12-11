import random
from batailleNavale.place_bateau import PlaceBateau, nivel

class Tirer:

    def tir(self, grille: list, x: int, y: int) -> str:
        """
        Vérifier l'état de la case dans laquelle les utilisateurs souhaitent tiré

        :param grille: list
        :param x: int
        :param y: int

        PRE: -
        POST : Renvoi l'état de la case dans laquelle les utilisateurs ont tiré
        """
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

    def utilisateur_tir(self, grille: list, tableau: list, grille_affiche: list, points: int) -> list:
        """
        Permet à l'utilisateur de tirer sur une case de la grille ennemi

        :param grille: list
        :param tableau: list
        :param grille_affiche: list
        :param points: int

        PRE: -
        POST : Renvoi la grille avec la case que l'utilisateur à viser
        """
        while True:
            print("Capitaine, ou voulez vous tiré ?")
            x, y = PlaceBateau().get_coordonnes()
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

    def tir_ordinateur(self, grille: list, tableau: list, points: int) -> list:
        """
        Générer des coordonnées aléatoires pour que l'ordinateur réalise les mouvements

        PRE: -
        POST : Renvoi la grille avec la case que l'utilisateur à viser
        """
        while True:
            x = random.randint(1, nivel)
            y = random.randint(1, nivel)
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


t = Tirer()


