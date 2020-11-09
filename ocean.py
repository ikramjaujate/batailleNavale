from utils import random
from utils import conversion
from main import clear
from colorama import Fore, Back, Style

from bateau import Bateau, BlackPearl, HmsIntercepteur, TheDyingGull, QueenAnneRevenge, SilentMary
col_header = {0: 'x', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K'}
row_header = {0: 'x', 1: ' 1', 2: ' 2', 3: ' 3', 4: ' 4', 5: ' 5', 6: ' 6', 7: ' 7', 8: ' 8', 9: ' 9', 10: '10'}

hauteur = 0
largeur = 0
estOk = 0
tours = 0
difficulte = input("Capitaine, quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()
while estOk == 0 :
    if difficulte == "FACILE":
            hauteur += 6
            largeur += 6
            tours += 4
            estOk = 1
            continue
    elif difficulte == "MOYEN":
            hauteur += 8
            largeur += 8
            tours += 7
            estOk = 1
            continue
    elif difficulte == "DIFFICILE":
            hauteur += 11
            largeur += 11
            tours += 10
            estOk = 1
            continue
    else:
            print("Ce niveau n'existe pas :/")
            difficulte = input("Capitaine, quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()
            estOk = 0

class Ocean:
    def __init__(self, hauteur=hauteur, largeur=hauteur):
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
        calcule = hauteur + 1
        for x in range(calcule) :
            ma_grille.append(["."] * calcule)

        for i in range(0, len(ma_grille)):
            ma_grille[0][0] = " "
            ma_grille[0][i] = col_header[i]  # col
            ma_grille[i][0] = row_header[i]  # row


        return ma_grille

ocean = Ocean()
ma_grille = ocean.grille()

def print_grille(gri):
    for ligne in gri:
        print("  ".join(ligne))

joueur_bateaux = []

nombre_bateaux = 3

for i in range(nombre_bateaux):
    # we also want to avoid duplicates
    while True:
        # COLONNE DU JOUEUR
        while True:
            try:
                joueur_colonne = str(input("Choissez la colonne désirée pour votre bateau:"))
                if len(joueur_colonne) == 1 and joueur_colonne.isalpha() and conversion.conversion_int(joueur_colonne) <= hauteur:
                    break
                else:
                    print("Votre bateau se trouve en dehors de l'océan :/")
            except ValueError:
                print("Un pirate ne placerait jamais son bateau sur terre...Réessaye")
                continue
        joueur_colonne = conversion.conversion_int(joueur_colonne)

        # LIGNE DU JOUEUR
        while True:
            try:
                joueur_ligne = int(input("Choissez la ligne désirée pour votre bateau:"))  # format 0-9
                if joueur_ligne <= hauteur and joueur_ligne != 0:
                    break
                else:
                    print("Un pirate ne placerait jamais son bateau sur terre...Réessaye")
            except ValueError:
                print("Votre bateau se trouve en dehors de l'océan :/")
                continue

        if (joueur_colonne, joueur_ligne) not in joueur_bateaux:
            joueur_bateaux.append((joueur_colonne, joueur_ligne))

            # we assign the player's bship on the player_grid
            ma_grille[joueur_ligne][joueur_colonne] = '|'
            break

print('------------MA GRILLE---------------------------')
print_grille(ma_grille)

# Encore un tours
def another_turn(tour):
    if tour == nombre_tours - 1:
        # failed because run out of turn
        print("C'est fini....")
        return False
    else:
        return True

ennemi_bateaux = []
ordi_grille = ocean.grille()

for i in range(nombre_bateaux):

    while True:
        colonne_enemie = random.random_colonne(ordi_grille)
        ligne_enemie = random.random_ligne(ordi_grille)

        if(colonne_enemie, ligne_enemie) not in ennemi_bateaux:
            ennemi_bateaux.append((colonne_enemie, ligne_enemie))
            ordi_grille[ligne_enemie][colonne_enemie] = '|'
            break

#print_grille(ordi_grille)
grille_tirs = ocean.grille()
grille_ennemi = ocean.grille()
for nombre_tours in range(0, tours):
    
    print("Capitaine, à votre tour!")
    while True:
        try:
            tir_colonne = input("Dans quelle colonne souhaitez-vous tirer? ")
            if len(tir_colonne) == 1 and tir_colonne.isalpha() and conversion.conversion_int(
                    tir_colonne) <= hauteur:
                break
            else:
                print("Vous ne savez pas tirer moussaillon! Allez, vite!")
        except ValueError:
            print("Vous ne savez pas tirer moussaillon! Allez, vite!")
            continue
    tir_colonne = conversion.conversion_int(tir_colonne)
    while True:
        try:
            tir_ligne = int(input("Dans quelle ligne souhaitez-vous tirer? "))
            if tir_ligne <= hauteur:
                break
            else:
                print("Vous ne savez pas tirer moussaillon! Allez, vite!")
        except ValueError:
            print("Vous ne savez pas tirer moussaillon! Allez, vite!")
            continue
    tuple_ensemble_coordonees_tir = (tir_colonne, tir_ligne)

    #Tours de l'odinateur
    colonne_enemie = random.random_colonne(ordi_grille)
    ligne_enemie = random.random_ligne(ordi_grille)
    tuple_ensemble_coordonees_tir_ennemie = (colonne_enemie, ligne_enemie)


    #Resolution tirs joueur
    if tuple_ensemble_coordonees_tir in ennemi_bateaux:
        grille_tirs[tir_ligne][tir_colonne] = "X"
        ennemi_bateaux.pop(ennemi_bateaux.index(tuple_ensemble_coordonees_tir))

        print(colors.couleurs.CGREEN + "BIEN MOUSSAILLON !! On a coulé le navire !" + colors.couleurs.CEND)
    else:
        if grille_tirs[tir_ligne][tir_colonne] == "*":
            print(colors.couleurs.CYELLOW  + "Moussaillon, vous avez déjà tiré là ! Donnez moi ça !!!" + colors.couleurs.CEND)
            print("---------------------------------------------------")
        else:
            grille_tirs[tir_ligne][tir_colonne] = "*"
            print(colors.couleurs.CYELLOW + "Moussaillon....vous avez tiré sur le requin !" + colors.couleurs.CEND )
            print("---------------------------------------------------")

    print_grille(grille_tirs)

    if tuple_ensemble_coordonees_tir_ennemie in joueur_bateaux:
        ma_grille[tir_ligne][tir_colonne].replace("|", "X")
        joueur_bateaux.pop(joueur_bateaux.index(tuple_ensemble_coordonees_tir_ennemie))
        print(colors.couleurs.CRED + "NOOOOON !!! MOUSSAILLON, ILS ONT TOUCHÉ UN DE NOS BATEAUX !" + colors.couleurs.CEND )
        print("---------------------------------------------------")

    else:
        if ma_grille[ligne_enemie][colonne_enemie] == "*":
            print(colors.couleurs.CGREEN +"Toute façon, ils l'ont déjà touché ce bateau" + colors.couleurs.CEND)
            print("---------------------------------------------------")
        else:
            ma_grille[ligne_enemie][colonne_enemie] = "*"
            ("---------------------------------------------------")
            ("---------------------------------------------------")
            print(colors.couleurs.CVIOLET +"HIHI, ils ont touché la balaine" + colors.couleurs.CEND)
            print("---------------------------------------------------")

    print_grille(ma_grille)

    if another_turn(tours) == False:
        break

    print("---------------------------------------------------")