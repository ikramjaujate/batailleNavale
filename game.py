from batailleNavale.tir import *
from batailleNavale.place_bateau import *


utilisateur_place = PlaceBateau().utilisateur_placer_bateaux(ma_grille, total_bateau)
ordi_place = PlaceBateau().ordinateur_placer_bateaux(grille_tirs, total_bateau)

# Encore un tours
def another_turn(tour : int) -> bool:
    if tour == tours - 1:
        print("C'est fini....")
        return False
    else:
        return True


def jeu():
    continuer = 1
    while continuer:
        joueurs_points = 0  # stockage des points gagnés par le joueur
        ennemi_points = 0  # stockage des points gagnés par l'ennemi
        for nombre_tours in range(0, tours):
            # Tours du joueur
            print("Capitaine, à votre tour!")
            Tirer().utilisateur_tir(grille_tirs, coord_bateau_ordi, grille_ennemie, joueurs_points)
            print("------------------------GRILLE ENNEMI ---------------------------")
            ocean.print_grille(grille_ennemie)

            verifier_coord_ordi = [tableau for tableau in coord_bateau_ordi if tableau != []]  # comprehension des liste
            if len(verifier_coord_ordi) == 0:
                print("Capitaine, nous avons coulé tous les navires de nos ennemis")
                break

            # Tours de l'ordinateur
            print("C'est au tour de l'ennemi")
            Tirer().tir_ordinateur(ma_grille, coord_bateau_utilisateur, ennemi_points)
            print("------------------------MA GRILLE ---------------------------")
            ocean.print_grille(ma_grille)
            verifier_coord_utilisateur = [x for x in coord_bateau_utilisateur if x != []]
            if len(verifier_coord_utilisateur) == 0:
                print("Capitaine, nous avons coulé tous les navires de nos ennemis")
                break

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

if __name__ == "__main__":
    jeu()
