from utils import random
from utils import conversion
from joueur import Joueur
from utils.couleur import Couleurs
from ocean import Ocean
from bateau import *
import os
import clear

from batailleNavale.bateau import *

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
        tours += 4
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


class BattleshipGame:

    def print_grille(self, gri):
        for ligne in gri:
            print("  ".join(ligne))

    def utilisateur_placer_bateaux(self, grille, bateau : int):
        for b in list(bateau.keys()):
            valide = False
            trait = ""
            while (not valide):
                print("Place " + b + " sur " + str(bateau[b]) + " cases")
                x, y = self.get_coordonnes()
                ori = self.v_ou_h()
                if ori == "v":
                    trait = '|'
                else:
                    trait = "-"
                valide = self.validate(grille, bateau[b], x, y, ori)
                if not valide:
                    print("Un pirate ne placerait jamais son bateau sur terre...Réessaye.")
                    input("Continuer")
            grille = self.placer_bateaux(grille, bateau[b], trait, ori, x, y)
            self.print_grille(grille)

        input("Capitaine, les bateaux sont placés. Appuyer sur enter pour continuer")
        return grille

    def ordinateur_placer_bateaux(self, grille, bateau: dict):
        for b in list(bateau.keys()):
            trait = ""
            ori = ""
            valide = False
            while (not valide):
                x = random.randint(1, hauteur)
                y = random.randint(1, hauteur)
                o = random.randint(0, 1)
                if o == 0:
                    ori = "v"
                    trait = "|"
                else:
                    ori = "h"
                    trait = "-"
                valide = self.validate(grille, bateau[b], x, y, ori)

            grille = self.placer_bateaux(grille, bateau[b], trait, ori, x, y)
        return grille

    def placer_bateaux(self, grille, bateau : int, s : str, ori : str, x: int , y: int):
        """
        accepte la grille la taille et la position du navire, place le navire, il doit déjà être vérifié by user_place_ships function
        """
        # orientation ships
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

    #bool permet determiner ce que renvoi la fonction
    def validate(self, grille, bateau, x: int, y: int, ori : str) -> bool:
        """
        vérifier si le navire convient, sur la base de sa taille, de a grille, de l'orientation et des coordonnées du navire
        """
        if ori == "v":
            for i in range(bateau):
                if x + i > hauteur:
                    return False
                elif "-" in grille[x][y] or "-" in grille[x + i][y]:
                    return False
                elif "|" in grille[x][y] or "|" in grille[x + i][y]:
                    return False
        elif ori == "h":
            for i in range(bateau):
                if y + i > hauteur:
                    return False
                elif "-" in grille[x][y] or "-" in grille[x][y + i]:
                    return False
                elif "|" in grille[x][y] or "|" in grille[x][y + i]:
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

    def tir(self, grille, x : int, y : int) -> str:
        if grille[x][y] == ".":
            return "rate"
        elif grille[x][y] == "*" or grille[x][y] == "X":
            return "toucheAvant"
        else:
            return "touche"

    def utilisateur_tir(self, grille):
        valide = False
        while valide:
            x, y = self.get_coordonnes()
            tir = self.tir(grille, x, y)
            if tir == "rate":
                print("Capitaine, vous avez rate le tir")
                grille[x][y] = "*"
                valide = True
            elif tir == "toucheAvant":
                print("Capitaine, vous avez déjà touché")
                valide = True
            elif tir == "touche":
                print("Bravo capitaine, vous avez touché le bateau")
                grille[x][y] = "X"
                valide = True
            if tir != "toucheAvant":
                return grille
        # wesley

    def tir_ordinateur(self, grille):
        """
        générer des coordonnées aléatoires pour que l'ordinateur réalise les mouvements
        """
        while (True):
            x = random.randint(1, hauteur)
            y = random.randint(1, hauteur)
            tir = self.tir(grille, x, y)
            if tir == "touche":
                grille[x][y] = 'X'
            elif tir == "rate":
                grille[x][y] = "*"
            return grille

    def check_couler(self, x, y, grille, bateau):
        pass


a = BattleshipGame()
print(a.print_grille(ma_grille))
x = a.utilisateur_placer_bateaux(ma_grille, total_bateau)
d = a.ordinateur_placer_bateaux(grille_ennemie, total_bateau)
# print(a.print_grille(grille_ennemie))
if __name__ == "__main__":
    print(x)
    print(d)
