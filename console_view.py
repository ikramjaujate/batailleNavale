import random
from game import *
from tir import *
from batailleNavale.prints_phrases import print_grille

class ConsoleView:
    def __init__(self):
        self.niv = 0
        self.continuer = 1

    def demandeNomUtilisateur(self):
        return input("Comment vous appelez-vous ? ")

    def demandeContinuerJeu(self):
        return int(input('Capitaine , souhaitez-vous continuer la bataille ?(1 pour oui, 0 pour non )'))

    def getDifficulte(self):
        self.estOk = 0
        difficulte = input(
            "Bonjour Capitaine , quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()
        while self.estOk == 0:
            if difficulte == "FACILE":
                self.estOk = 1
                return "FACILE"
            elif difficulte == "MOYEN":
                self.estOk = 1
                return "MOYEN"
            elif difficulte == "DIFFICILE":
                self.estOk = 1
                return "DIFFICILE"
            else:
                print("Ce niveau n'existe pas :/")
                difficulte = input("Capitaine, quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()
                self.estOk = 0

    def utilisateur_placer_bateaux(self, grille: list, bateau: dict, niveau: int):
        """
        Function qui permet à l'utilisateur de placer les bateau dans la grille
        :param grille: la grille sur laquelle il y a le placement des bateau
        :param bateau: contient sous forme de dictionnaire, tous les bateaux a placé sur la grille
        PRE: -
        POST: Renvoi la grille ainsi que ajoute dans une variable global le coordonnées des bateaux placé par l'utilisateur
        """
        self.niv = niveau
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
            grille = Ocean(self.niv).placer_bateaux(grille, bateau[b], b[0], ori, x, y)

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

            print_grille(grille)

        coord_bateau_utilisateur = []

        for i in total_coordonees:
            if i != []:
                coord_bateau_utilisateur.append(i)

        input("Capitaine, les bateaux sont placés. Appuyer sur enter pour continuer")

        return [grille, coord_bateau_utilisateur]

    def ordinateur_placer_bateaux(self, grille: list, bateau: dict, niveau:int):
        """
        Function qui permet à l'ordinateur de placer les bateaux aléatoirement dans la grille
        :param grille: la grille sur laquelle il y a le placement des bateau
        :param bateau: contient sous forme de dictionnaire, tous les bateaux a placé sur la grille
        PRE: -
        POST: Renvoi la grille ainsi que ajoute dans une variable global le coordonnées des bateaux placé par l'ordinateur de forme aléatoire
        """
        self.niv = niveau
        noms_bateau = []
        for b in list(bateau.keys()):
            noms_bateau.append(b[0])
            ori = ""
            valide = False
            while not valide:
                x = random.randint(1, self.niv)
                y = random.randint(1, self.niv)
                o = random.randint(0, 1)
                ori = "v" if o == 0 else "h"
                valide = self.validate(grille, bateau[b], x, y, ori)

            grille = Ocean(self.niv).placer_bateaux(grille, bateau[b], b[0], ori, x, y)

            total_coordonees = [[], [], [], [], []]
            for i in range(len(grille)):
                if i != 0:
                    for x in range(len(grille[i])):
                        for f in range(len(noms_bateau)):
                            compteur = f

                            if grille[i][x] == noms_bateau[f] == 'T':
                                total_coordonees[0].append((i, x))
                                compteur += 1
                            elif grille[i][x] == noms_bateau[f] == 'H':
                                total_coordonees[1].append((i, x))
                                compteur += 1
                            elif grille[i][x] == noms_bateau[f] == 'S':
                                total_coordonees[2].append((i, x))
                                compteur += 1
                            elif grille[i][x] == noms_bateau[f] == 'Q':
                                total_coordonees[3].append((i, x))
                                compteur += 1
                            elif grille[i][x] == noms_bateau[f] == 'B':
                                total_coordonees[4].append((i, x))
                                compteur += 1

        coord_bateau_ordi = []
        for i in total_coordonees:
            if i != []:
                coord_bateau_ordi.append(i)
        return [grille, coord_bateau_ordi]


    def get_coordonnes(self):
        """
        Function qui permet à l'utilisateur de choisir le placement des bateaux
        PRE: -
        POST: Renvoi les coordonnées désirés par les utilisateurs
        RAISE : Si pas assez de coordonnées ou trop, il y a Exception
        RAISE : Si les coordonnées désirés sont en dehors de la hauteur de la grille, il y a Exception
        :exception : Si les valeurs ne sont pas valides, il y a ValueError
        """
        while True:
            user_input = input("Entrez coordonnées (ligne,colonne) ? ")
            try:
                coordonnees = user_input.split(",")
                if len(coordonnees) != 2:
                    raise Exception("Vous avez rentrez trop / pas assez de coordonnées.")

                # check that 2 values are integers
                coordonnees[0] = int(coordonnees[0])
                coordonnees[1] = int(coordonnees[1])

                if coordonnees[0] > self.niv or coordonnees[0] < 0 or coordonnees[1] > self.niv or coordonnees[1] < 0:
                    raise Exception("Introduisez des valeurs entre 0 et " + str(self.niv))

                return coordonnees
            except ValueError:
                print("Erreur. Rentrez des valeurs valides.")
            except Exception as e:
                print(e)

    def validate(self, grille: list, bateau, x: int, y: int, ori: str):
        """
        Vérifier si le navire convient, sur la base de sa taille, de a grille, de l'orientation et des coordonnées du navire
        :param grille : la grille sur laquelle l'utilisateur veut placer les bateaux
        :param bateau : les bateaux a placé sur la grille
        :param x : placement dans la ligne
        :param y : placement dans la colonne
        :param ori : orientation du bateau
        PRE: -
        POST : Renvoi True si le placement du bateau est bon, renvoi False si ce n'est pas le cas
        """
        if ori == "v":
            for i in range(bateau):
                if x + i > self.niv:
                    return False
                elif "." not in grille[x][y] or "." not in grille[x + i][y]:
                    return False
        elif ori == "h":
            for i in range(bateau):
                if y + i > self.niv:
                    return False
                elif "." not in grille[x][y] or "." not in grille[x][y + i]:
                    return False
        else:
            return True
        return True

    def v_ou_h(self):
        """
        Function qui permet déterminer l'orientation des bateaux
        PRE: -
        POST : Renvoi l'orientation désiré par l'utilisateur
        RAISE : Si l'utilisateur choisit autre chose que v ou h alors il y a ValueError
        """
        while True:
            user_input = input("verticale ou horizontale (v,h) ? ")
            if user_input == "v" or user_input == "h":
                return user_input
            else:
                print('Mauvaise orientation retentez')

    def utilisateur_tir(self, grille: list):
        """
        Permet à l'utilisateur de tirer sur une case de la grille ennemi
        :param grille: list
        PRE: -
        POST : Renvoi la grille avec la case que l'utilisateur à viser
        """
        print("Capitaine, ou voulez vous tiré ?")
        x, y = self.get_coordonnes()
        status = Tirer().tir(grille, x, y)
        return {
            "status": status,
            "x": x,
            "y": y
        }

    def tir_ordinateur(self, grille: list):
        """
        Générer des coordonnées aléatoires pour que l'ordinateur réalise les mouvements
        PRE: -
        POST : Renvoi la grille avec la case que l'utilisateur à viser
        """
        x = random.randint(1, self.niv)
        y = random.randint(1, self.niv)
        status = Tirer().tir(grille, x, y)
        return {
            "status": status,
            "x": x,
            "y": y
        }
Game(ConsoleView()).play()
