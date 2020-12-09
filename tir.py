from batailleNavale.jeu_console import *
from batailleNavale.utils.clear import clear


class Tirer:

    def tir(self, grille: list, x: int, y: int) -> str:
        """
        Vérifier l'état de la case dans laquelle les utilisateurs souhaitent tiré

        :param grille:
        :param x:
        :param y:
        :return:
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

        :param grille:
        :param tableau:
        :param grille_affiche:
        :param points:
        :return:
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


# Encore un tours
def another_turn(tour : int) -> bool:
    if tour == tours - 1:
        print("C'est fini....")
        return False
    else:
        return True


def tirer():
    continuer = 1
    while continuer:
        joueurs_points = 0  # stockage des points gagnés par le joueur
        ennemi_points = 0  # stockage des points gagnés par l'ennemi
        for nombre_tours in range(0, tours):
            # Tours du joueur
            print("Capitaine, à votre tour!")
            t.utilisateur_tir(grille_tirs, coord_bateau_ordi, grille_ennemie, joueurs_points)
            print("------------------------GRILLE ENNEMI ---------------------------")
            ocean.print_grille(grille_ennemie)

            verifier_coord_ordi = [x for x in coord_bateau_ordi if x != []]  # comprehension des liste
            if len(verifier_coord_ordi) == 0:
                print("Capitaine, nous avons coulé tous les navires de nos ennemis")
                break

            # Tours de l'ordinateur
            print("C'est au tour de l'ennemi")
            t.tir_ordinateur(ma_grille, coord_bateau_utilisateur, ennemi_points)
            print("------------------------MA GRILLE ---------------------------")
            ocean.print_grille(ma_grille)
            verifier_coord_utilisateur = [x for x in coord_bateau_utilisateur if x != []]
            if len(verifier_coord_utilisateur) == 0:
                print("Capitaine, nous avons coulé tous les navires de nos ennemis")
                break

            clear()

            if another_turn(tours) == False:
                break

            print("---------------------------------------------------")

        for liste in verifier_coord_utilisateur:
            for element in liste:
                joueurs_points += 1
        for liste in verifier_coord_ordi:
            for element in liste:
                ennemi_points += 1
        if joueurs_points == ennemi_points:
            print("C'était une très bonne partie mon capitaine " + joueur_nom.getNom() + " , vous êtes à égalité")
        elif joueurs_points < ennemi_points:
            print("Vous voilà noyé....vous avez perdu moussaillon !")
        else:
            print(
                "Jack Sparrow serait très fière de vous capitaine " + joueur_nom.getNom() + " , vous avez coulé les bateaux ennemis !!")
        continuer = input('Capitaine ' + str(
            joueur_nom.getNom()) + " , souhaitez-vous continuer la bataille ?(1 pour oui, 0 pour non) ")
        while continuer != "1" and continuer != "0":
            print("Chiffre pas valable")
            continuer = input('Capitaine ' + str(
                joueur_nom.getNom()) + " , souhaitez-vous continuer la bataille ?(1 pour oui, 0 pour non) ")
        continuer = int(continuer)
