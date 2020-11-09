from utils import random
from utils import conversion
from colorama import Fore, Back, Style
from joueur import Joueur
from utils.couleur import Couleurs
from ocean import Ocean
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
    # we also want to avoid duplicates
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
joueurs_coup = 0
ennemi_coup = 0
def another_turn(tour):
    if tour == nombre_tours - 1:
        print("C'est fini....")
        return False
    else:
        return True


ennemi_bateaux = []

ordi_grille = ocean.grille()

for i in range(NOMBRE_BATEAUX):

    while True:
        colonne_enemie = random.random_colonne(ordi_grille)
        ligne_enemie = random.random_ligne(ordi_grille)

        if (colonne_enemie, ligne_enemie) not in ennemi_bateaux:
            ennemi_bateaux.append((colonne_enemie, ligne_enemie))
            ordi_grille[ligne_enemie][colonne_enemie] = '|'
            break

# print_grille(ordi_grille)
grille_tirs = ocean.grille()
grille_ennemi = ocean.grille()

#print(ennemi_bateaux)
#Creation d'une boucle pour s'assurer que l'utilisateur puisse jouer autant de fois qu'il le souhaite
continuer = "Y"
while continuer:
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


        # Resolution tirs joueur
        if tuple_ensemble_coordonees_tir in ennemi_bateaux:
            print(ennemi_bateaux)
            grille_tirs[tir_ligne][tir_colonne] = "X"
            ennemi_bateaux.pop(ennemi_bateaux.index(tuple_ensemble_coordonees_tir))
            joueurs_coup += 1
            print(Couleurs.CGREEN + "BIEN MOUSSAILLON !! On a coulé le navire !" + Couleurs.CEND)

            if len(ennemi_bateaux) == 0:
                print("ON LES A BATTU !!!!!")
                break
        else:
            if grille_tirs[tir_ligne][tir_colonne] == "*":
                print(Couleurs.CVIOLET + "Moussaillon, vous avez déjà tiré là ! Donnez moi ça !!!" + Couleurs.CEND)
                print("---------------------------------------------------")
            else:
                grille_tirs[tir_ligne][tir_colonne] = "*"
                print(Couleurs.CBLUE + "Moussaillon....vous avez tiré sur le requin !" + Couleurs.CEND)
                print("---------------------------------------------------")

        print_grille(grille_tirs)

        if tuple_ensemble_coordonees_tir_ennemie in joueur_bateaux:
            ma_grille[ligne_enemie][colonne_enemie] = "X"
            joueur_bateaux.pop(joueur_bateaux.index(tuple_ensemble_coordonees_tir_ennemie))
            ennemi_coup += 1
            print(Couleurs.CRED + "NOOOOON !!! MOUSSAILLON, ILS ONT TOUCHÉ UN DE NOS BATEAUX !" + Couleurs.CEND)
            print("---------------------------------------------------")

            if len(joueur_bateaux) == 0:
                print("ON EST ENTRAIN DE COULER !!!!!")
                break
        else:
            if ma_grille[ligne_enemie][colonne_enemie] == "*":
                print(Couleurs.CYELLOW + "Toute façon, ils l'ont déjà touché ce bateau" + Couleurs.CEND)
                print("---------------------------------------------------")
            else:
                ma_grille[ligne_enemie][colonne_enemie] = "*"
                ("---------------------------------------------------")
                ("---------------------------------------------------")
                print(Couleurs.CYELLOW + "HIHI, ils ont touché la balaine" + Couleurs.CEND)
                print("---------------------------------------------------")

        print_grille(ma_grille)

        if another_turn(tours) == False:
            break

        print("---------------------------------------------------")

    continuer = input( str(joueur_nom.getFunction()) + ' ' + str(joueur_nom.getNom()) + " , souhaitez vous continuer la bataille ?(1 pour oui, 0 pour non) ")
    while continuer != "1" and continuer != "0":
        print("Chiffre pas valable")
        continuer = input(str(joueur_nom.getFunction()) + ' ' + str(joueur_nom.getNom()) + " , souhaitez vous continuer la bataille ?(1 pour oui, 0 pour non) ")
    continuer = int(continuer)