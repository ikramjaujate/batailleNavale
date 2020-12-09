import random

from batailleNavale.tir import *
from batailleNavale.ocean import *
from batailleNavale.bateau import *

nom = input("Comment vous appelez-vous ?")
joueur_nom = Joueur(nom)

estOk = 0
total_bateau = {}

difficulte = input(
    "Bonjour Capitaine , quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()


while estOk == 0:
    if difficulte == "FACILE":
        estOk = 1
        total_bateau[TheDyingGull("The Dying Gull").getNom] = TheDyingGull("The Dying Gull").length
        total_bateau[HmsIntercepteur("HMS Intercepteur").getNom] = HmsIntercepteur("HMS Intercepteur").length
        continue
    elif difficulte == "MOYEN":
        estOk = 1
        total_bateau[TheDyingGull("The Dying Gull").getNom] = TheDyingGull("The Dying Gull").length
        total_bateau[HmsIntercepteur("HMS Intercepteur").getNom] = HmsIntercepteur("HMS Intercepteur").length
        total_bateau[SilentMary("Silent Mary").getNom] = SilentMary("Silent Mary").length
        continue
    elif difficulte == "DIFFICILE":
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


#DEFINITION DE LA DIFFICULTÉ
diff = Difficulte()
nivel = diff.get_hauteur(difficulte)
tours = diff.get_tours(difficulte)

#DEFINITION DE L'OCEAN
ocean = Ocean(nivel)
ma_grille = ocean.grille()

grille_ennemie = ocean.grille()
grille_tirs = ocean.grille()

#DEFINITION COORDONNEES
coord_bateau_utilisateur = []
coord_bateau_ordi = []

class PlaceBateau:

    def utilisateur_placer_bateaux(self, grille: list, bateau: dict) -> list:
        """
        Function qui permet à l'utilisateur de placer les bateau dans la grille

        :param grille: list
        :param bateau: dict

        :return:
        """
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

            ocean.print_grille(grille)

        for i in total_coordonees:
            if i != []:
                coord_bateau_utilisateur.append(i)

        input("Capitaine, les bateaux sont placés. Appuyer sur enter pour continuer")

        return grille

    def ordinateur_placer_bateaux(self, grille: list, bateau: dict) -> list:
        """
        Function qui permet à l'ordinateur de placer les bateaux aléatoirement dans la grille

        :param grille: list
        :param bateau: dict

        :return:
        """
        noms_bateau = []
        for b in list(bateau.keys()):
            noms_bateau.append(b[0])
            ori = ""
            valide = False
            while not valide:
                x = random.randint(1, nivel)
                y = random.randint(1, nivel)
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
        Accepte la grille la taille et la position du navire, place le navire, il doit déjà être vérifié by user_place_ships function
        """
        if ori == "v":
            for i in range(bateau):
                grille[x + i][y] = s
        elif ori == "h":
            for i in range(bateau):
                grille[x][y + i] = s
        return grille

    def get_coordonnes(self):
        """
        Function qui permet à l'utilisateur de choisir le placement des bateaux
        :return:
        """
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

                if coordonnees[0] > nivel or coordonnees[0] < 0 or coordonnees[1] > nivel or coordonnees[1] < 0:
                    raise Exception("Introduisez des valeurs entre 0 et " + str(nivel))

                # si tout va bien, renvoyer les coordonnées
                return coordonnees
            except ValueError:
                print("Erreur. Rentrez des valeurs valides.")
            except Exception as e:
                print(e)

    # bool permet determiner ce que renvoi la fonction
    def validate(self, grille: list, bateau, x: int, y: int, ori: str) -> bool:
        """
        Vérifier si le navire convient, sur la base de sa taille, de a grille, de l'orientation et des coordonnées du navire
        """
        if ori == "v":
            for i in range(bateau):
                if x + i > nivel:
                    return False
                elif "." not in grille[x][y] or "." not in grille[x + i][y]:
                    return False
        elif ori == "h":
            for i in range(bateau):
                if y + i > nivel:
                    return False
                elif "." not in grille[x][y] or "." not in grille[x][y + i]:
                    return False
        else:
            return True
        return True

    def v_ou_h(self) -> str:
        """
        Function qui permet déterminer l'orientation des bateaux
        """
        while True:
            user_input = input("verticale ou horizontale (v,h) ? ")
            if user_input == "v" or user_input == "h":
                return user_input
            else:
                print("Erreur mon capitaine. Entrez v ou h")


b = PlaceBateau()
utilisateur_place = b.utilisateur_placer_bateaux(ma_grille, total_bateau)
ordi_place = b.ordinateur_placer_bateaux(grille_tirs, total_bateau)