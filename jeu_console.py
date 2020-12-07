import random
from batailleNavale.joueur import Joueur
from batailleNavale.ocean import Ocean
from batailleNavale.bateau import *
from batailleNavale.clear import clear

hauteur = 0
largeur = 0
estOk = 0
tours = 0
total_bateau = {}

nom_joueur = input("Capitaine, comment-vous appelez vous ?").upper()
joueur_nom = Joueur(nom_joueur)

difficulte = input(
    joueur_nom.getFunction() + " " + joueur_nom.getNom() + ", quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()
while estOk == 0:
    if difficulte == "FACILE":
        hauteur += 6
        largeur += 6
        tours += 8
        estOk = 1
        total_bateau[TheDyingGull("The Dying Gull").getNom] = TheDyingGull("The Dying Gull").length
        total_bateau[HmsIntercepteur("HMS Intercepteur").getNom] = HmsIntercepteur("HMS Intercepteur").length
        continue
    elif difficulte == "MOYEN":
        hauteur += 8
        largeur += 8
        tours += 7
        estOk = 1
        total_bateau[TheDyingGull("The Dying Gull").getNom] = TheDyingGull("The Dying Gull").length
        total_bateau[HmsIntercepteur("HMS Intercepteur").getNom] = HmsIntercepteur("HMS Intercepteur").length
        total_bateau[SilentMary("Silent Mary").getNom] = SilentMary("Silent Mary").length
        continue
    elif difficulte == "DIFFICILE":
        hauteur += 11
        largeur += 11
        tours += 10
        estOk = 1
        total_bateau[TheDyingGull("The Dying Gull").getNom] = TheDyingGull("The Dying Gull").length
        total_bateau[HmsIntercepteur("HMS Intercepteur").getNom] = HmsIntercepteur("HMS Intercepteur").length
        total_bateau[SilentMary("Silent Mary").getNom] = SilentMary("Silent Mary").length
        total_bateau[QueenAnneRevenge("Queen Anne's Revenge").getNom] = QueenAnneRevenge("Queen Anne's Revenge").length
        total_bateau[BlackPearl("Black Pearl").getNom] = BlackPearl("Black Pearl").length
        continue
    else:
        print("Ce niveau n'existe pas :/")
        difficulte = input("Capitaine, quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()
        estOk = 0

ocean = Ocean(hauteur, largeur)
ma_grille = ocean.grille()

grille_ennemie = ocean.grille()
grille_tirs = ocean.grille()

coord_bateau_utilisateur = []
coord_bateau_ordi = []


class Bateau:

    def print_grille(self, gri : list):
        for ligne in gri:
            print("  ".join(ligne))

    def utilisateur_placer_bateaux(self, grille: list, bateau: dict) -> list:
        noms_bateau = []

        for b in list(bateau.keys()):
            noms_bateau.append(b[0])

            valide = False
            while not valide:
                print("Place " + b + " sur " + str(bateau[b]) + " cases")
                x, y = self.get_coordonnes()
                ori = self.v_ou_h()

                valide = self.validate(grille, bateau[b], x, y, ori)
                if not valide:
                    print("Un pirate ne placerait jamais son bateau sur terre...Réessaye.")
                    input("Continuer")
            grille = self.placer_bateaux(grille, bateau[b], b[0], ori, x, y)

            total_coordonees = [[], [], [], [], []]
            for i in range(len(grille)):
                if i != 0:
                    for x in range(len(grille[i])):
                        for f in range(len(noms_bateau)):
                            a = f

                            if grille[i][x] == noms_bateau[f] == 'T':
                                total_coordonees[0].append((i, x))
                                a += 1
                            elif grille[i][x] == noms_bateau[f] == 'H':
                                total_coordonees[1].append((i, x))
                                a += 1
                            elif grille[i][x] == noms_bateau[f] == 'S':
                                total_coordonees[2].append((i, x))
                                a += 1
                            elif grille[i][x] == noms_bateau[f] == 'Q':
                                total_coordonees[3].append((i, x))
                                a += 1
                            elif grille[i][x] == noms_bateau[f] == 'B':
                                total_coordonees[4].append((i, x))
                                a += 1

            self.print_grille(grille)

        for i in total_coordonees:
            if i != []:
                coord_bateau_utilisateur.append(i)

        # print(coord)
        input("Capitaine, les bateaux sont placés. Appuyer sur enter pour continuer")

        return grille

    def ordinateur_placer_bateaux(self, grille: list, bateau: dict) -> list:
        noms_bateau = []
        for b in list(bateau.keys()):
            noms_bateau.append(b[0])
            ori = ""
            valide = False
            while not valide:
                x = random.randint(1, hauteur)
                y = random.randint(1, hauteur)
                o = random.randint(0, 1)
                ori = "v" if o == 0 else "h"
                valide = self.validate(grille, bateau[b], x, y, ori)

            grille = self.placer_bateaux(grille, bateau[b], b[0], ori, x, y)

            total_coordonees = [[], [], [], [], []]
            for i in range(len(grille)):
                if i != 0:
                    for x in range(len(grille[i])):
                        for f in range(len(noms_bateau)):
                            a = f

                            if grille[i][x] == noms_bateau[f] == 'T':
                                total_coordonees[0].append((i, x))
                                a += 1
                            elif grille[i][x] == noms_bateau[f] == 'H':
                                total_coordonees[1].append((i, x))
                                a += 1
                            elif grille[i][x] == noms_bateau[f] == 'S':
                                total_coordonees[2].append((i, x))
                                a += 1
                            elif grille[i][x] == noms_bateau[f] == 'Q':
                                total_coordonees[3].append((i, x))
                                a += 1
                            elif grille[i][x] == noms_bateau[f] == 'B':
                                total_coordonees[4].append((i, x))
                                a += 1

        for i in total_coordonees:
            if i != []:
                coord_bateau_ordi.append(i)
        # print(coord)
        # return coord
        return grille

    def placer_bateaux(self, grille: list, bateau: int, s: str, ori: str, x: int, y: int):
        """
        accepte la grille la taille et la position du navire, place le navire, il doit déjà être vérifié by user_place_ships function
        """
        if ori == "v":
            for i in range(bateau):
                grille[x + i][y] = s
        elif ori == "h":
            for i in range(bateau):
                grille[x][y + i] = s
        return grille

    def get_coordonnes(self):
        while True:
            user_input = input("Entrez coordonnées (ligne,colonne) ? ")
            try:
                # voir que l'utilisateur a entré 2 valeurs séparées par une virgule
                coordonnees = user_input.split(",")
                if len(coordonnees) != 2:
                    raise Exception("Vous avez rentrez trop / pas assez de coordonnées.")

                # check that 2 values are integers
                coordonnees[0] = int(coordonnees[0])
                coordonnees[1] = int(coordonnees[1])

                if coordonnees[0] > hauteur or coordonnees[0] < 0 or coordonnees[1] > hauteur or coordonnees[1] < 0:
                    raise Exception("Introduisez des valeurs entre 0 et " + str(hauteur))

                # si tout va bien, renvoyer les coordonnées
                return coordonnees
            except ValueError:
                print("Erreur. Rentrez des valeurs valides.")
            except Exception as e:
                print(e)

    # bool permet determiner ce que renvoi la fonction
    def validate(self, grille: list, bateau, x: int, y: int, ori: str) -> bool:
        """
        vérifier si le navire convient, sur la base de sa taille, de a grille, de l'orientation et des coordonnées du navire
        """
        if ori == "v":
            for i in range(bateau):
                if x + i > hauteur:
                    return False
                elif "." not in grille[x][y] or "." not in grille[x + i][y]:
                    return False
        elif ori == "h":
            for i in range(bateau):
                if y + i > hauteur:
                    return False
                elif "." not in grille[x][y] or "." not in grille[x][y + i]:
                    return False
        else:
            return True
        return True

    def v_ou_h(self) -> str:
        """
        Disposition du bateau dans la grille
        """
        while True:
            user_input = input("verticale ou horizontale (v,h) ? ")
            if user_input == "v" or user_input == "h":
                return user_input
            else:
                print("Erreur mon capitaine. Entrez v ou h")


b = Bateau()
utilisateur_place = b.utilisateur_placer_bateaux(ma_grille, total_bateau)
ordi_place = b.ordinateur_placer_bateaux(grille_tirs, total_bateau)


class Tir:

    def tir(self, grille : list, x: int, y: int) -> str:
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

    def utilisateur_tir(self, grille: list, tableau : list, grille_affiche : list, points: int):
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

    def tir_ordinateur(self, grille: list, tableau : list, points: int):
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


# Encore un tours
def another_turn(tour):
    if tour == tours - 1:
        print("C'est fini....")
        return False
    else:
        return True


t = Tir()

def main():
    continuer = 1
    while continuer:
        joueurs_points = 0  # stockage des points gagnés par le joueur
        ennemi_points = 0  # stockage des points gagnés par l'ennemi
        for nombre_tours in range(0, tours):
            print("Capitaine, à votre tour!")
            t.utilisateur_tir(grille_tirs, coord_bateau_ordi, grille_ennemie, joueurs_points)
            print("------------------------GRILLE ENNEMI ---------------------------")
            print(b.print_grille(grille_ennemie))

            verifier_coord_ordi = [x for x in coord_bateau_ordi if x != []]
            # print(verifier_coord_ordi)
            if len(verifier_coord_ordi) == 0:
                print("Capitaine, nous avons coulé tous les navires de nos ennemis")
                break

            # Tours de l'odinateur
            print("C'est au tour de l'ennemi")
            t.tir_ordinateur(ma_grille, coord_bateau_utilisateur, ennemi_points)
            print("------------------------MA GRILLE ---------------------------")
            print(b.print_grille(ma_grille))
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
        continuer = input(str(joueur_nom.getFunction()) + ' ' + str(
            joueur_nom.getNom()) + " , souhaitez-vous continuer la bataille ?(1 pour oui, 0 pour non) ")
        while continuer != "1" and continuer != "0":
            print("Chiffre pas valable")
            continuer = input(str(joueur_nom.getFunction()) + ' ' + str(
                joueur_nom.getNom()) + " , souhaitez-vous continuer la bataille ?(1 pour oui, 0 pour non) ")
        continuer = int(continuer)


if __name__ == "__main__":
    main()
