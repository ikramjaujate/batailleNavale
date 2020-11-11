from utils import random
from utils import conversion
from joueur import Joueur
from utils.couleur import Couleurs
from ocean import Ocean
import os
import clear
hauteur = 0
largeur = 0
estOk = 0
tours = 0

nom_joueur = input("Capitaine, comment-vous appelez vous ?").upper()
joueur_nom = Joueur(nom_joueur)

difficulte = input(joueur_nom.getFunction() + " " + joueur_nom.getNom() + ", quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()
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

ocean = Ocean(hauteur, largeur)
ma_grille = ocean.grille()


def print_grille(gri):
    for ligne in gri:
        print("  ".join(ligne))


joueur_bateaux = []

NOMBRE_BATEAUX = 3
for i in range(NOMBRE_BATEAUX):
    '''Parcours du nombre de bateaux afin de les ajouter dans une liste appartenant au joueur '''
    while True:
        # COLONNE DU JOUEUR
        while True:
            try:
                joueur_colonne = str(input("Choissez la colonne désirée pour votre bateau:"))
                if len(joueur_colonne) == 1 and joueur_colonne.isalpha() and conversion.conversion_int(
                        joueur_colonne) <= hauteur:
                    break
                else:
                    print("Votre bateau se trouve en dehors de l'océan :/")
            except ValueError:
                print("Un pirate ne placerait jamais son bateau sur terre...Réessaye")
                continue
        joueur_colonne = conversion.conversion_int(joueur_colonne) #conversion de la lettre en nombre

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
            ma_grille[joueur_ligne][joueur_colonne] = '|' # ajout du bateaux dans la grille
            break

print('------------MA GRILLE---------------------------')
print_grille(ma_grille) #affichage de notre grille avec les bateaux


# Encore un tours
def another_turn(tour):
    if tour == tours - 1:
        print("C'est fini....")
        return False
    else:
        return True


ennemi_bateaux = []
ordi_grille = ocean.grille()

for i in range(NOMBRE_BATEAUX):
    '''Parcours du nombre de bateaux afin de les ajouter dans une liste appartenant à l'ennemi '''
    while True:
        colonne_enemie = random.random_colonne(ordi_grille)
        ligne_enemie = random.random_ligne(ordi_grille)

        if (colonne_enemie, ligne_enemie) not in ennemi_bateaux:
            ennemi_bateaux.append((colonne_enemie, ligne_enemie))
            ordi_grille[ligne_enemie][colonne_enemie] = '|'
            break


grille_tirs = ocean.grille()
clear.clear()
#Creation d'une boucle pour s'assurer que l'utilisateur puisse jouer autant de fois qu'il le souhaite
def main():
    continuer = 1
    while continuer:

        joueurs_points = 0 #stockage des points gagnés par le joueur
        ennemi_points = 0 #stockage des points gagnés par l'ennemi
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

            # Tours de l'odinateur
            colonne_enemie = random.random_colonne(ordi_grille)
            ligne_enemie = random.random_ligne(ordi_grille)
            tuple_ensemble_coordonees_tir_ennemie = (colonne_enemie, ligne_enemie)
            print(ennemi_bateaux)

            clear.clear()
            # Resolution tirs joueur
            if tuple_ensemble_coordonees_tir in ennemi_bateaux:

                grille_tirs[tir_ligne][tir_colonne] = str(Couleurs.CRED +" {} " + Couleurs.CEND).format("X")
                ennemi_bateaux.pop(ennemi_bateaux.index(tuple_ensemble_coordonees_tir))
                joueurs_points += 1
                print(str(Couleurs.CGREEN  +" {} " + Couleurs.CEND).format("BIEN MOUSSAILLON !! On a coulé le navire !" + "(en " + str(nombre_tours + 1) + " tirs)"))

                if len(ennemi_bateaux) == 0:
                    print("Capitaine, nous avons coulé tous les navires de nos ennemis")
                    break
            else:
                if grille_tirs[tir_ligne][tir_colonne] == "*":
                    print(str(Couleurs.CVIOLET +" {} " + Couleurs.CEND).format("Moussaillon, vous avez déjà tiré là ! Donnez moi ça !!!"))
                    print("---------------------------------------------------")
                else:
                    grille_tirs[tir_ligne][tir_colonne] = str(Couleurs.CYELLOW +" {} " + Couleurs.CEND).format("*")
                    print(str(Couleurs.CBLUE +" {} " + Couleurs.CEND).format("Moussaillon....vous avez tiré sur le requin !"))
                    print("---------------------------------------------------")

            print_grille(grille_tirs)

            # Resolution tirs ennemie
            if tuple_ensemble_coordonees_tir_ennemie in joueur_bateaux:
                ma_grille[ligne_enemie][colonne_enemie] = str(Couleurs.CRED +" {} " + Couleurs.CEND).format("X")
                joueur_bateaux.pop(joueur_bateaux.index(tuple_ensemble_coordonees_tir_ennemie))
                ennemi_points += 1
                print(str(Couleurs.CRED +" {} " + Couleurs.CEND).format("NOOOOON !!! MOUSSAILLON, ILS ONT TOUCHÉ UN DE NOS BATEAUX !"))
                print("---------------------------------------------------")

                if len(joueur_bateaux) == 0:
                    print("ON EST ENTRAIN DE COULER !!!!!")
                    break
            else:
                if ma_grille[ligne_enemie][colonne_enemie] == "*":
                    print(str(Couleurs.CYELLOW +" {} " + Couleurs.CEND).format("Toute façon, ils l'ont déjà touché ce bateau"))
                    print("---------------------------------------------------")
                else:
                    ma_grille[ligne_enemie][colonne_enemie] = str(Couleurs.CYELLOW +" {} " + Couleurs.CEND).format("*")
                    ("---------------------------------------------------")
                    ("---------------------------------------------------")
                    print(str(Couleurs.CYELLOW +" {} " + Couleurs.CEND).format("HIHI, ils ont touché la balaine"))
                    print("---------------------------------------------------")

            print_grille(ma_grille)
            if another_turn(tours) == False:
                break

            print("---------------------------------------------------")

        if joueurs_points == ennemi_points:
            print("C'était une très bonne partie mon capitaine " + joueur_nom.getNom() + " , vous êtes à égalité")
        elif joueurs_points < ennemi_points:
            print("Vous voilà noyé....vous avez perdu moussaillon !")
        else:
            print("Jack Sparrow serait très fière de vous capitaine "+ joueur_nom.getNom() + " , vous avez coulé les bateaux ennemis !!")
        continuer = input( str(joueur_nom.getFunction()) + ' ' + str(joueur_nom.getNom()) + " , souhaitez-vous continuer la bataille ?(1 pour oui, 0 pour non) ")
        while continuer != "1" and continuer != "0":
            print("Chiffre pas valable")
            continuer = input(str(joueur_nom.getFunction()) + ' ' + str(joueur_nom.getNom()) + " , souhaitez-vous continuer la bataille ?(1 pour oui, 0 pour non) ")
        continuer = int(continuer)

