def print_grille(grille: list) -> str:
    """
    Function qui permet de afficher la grille en console
    :param grille: la grille qui est utilisé
    PRE : -
    POST : Renvoi la grille sous forme de string pour qu'elle soit afficher dans la console

    """
    for ligne in grille:
        print("  ".join(ligne))


def plouf(grille: list) -> str:
    print("Capitaine, vous avez rate le tir")
    print("------------------------GRILLE ENNEMI ---------------------------")
    print_grille(grille)


def boum(grille: list) -> str:
    print("Bravo capitaine, vous avez touché le bateau")
    print("------------------------GRILLE ENNEMI ---------------------------")
    print_grille(grille)


def ploufOrdi(grille: list) -> str:
    print("HIHI, ils ont touché la balaine ")
    print("------------------------MA GRILLE ---------------------------")
    print_grille(grille)


def boumOrdi(grille: list) -> str:
    print("NOOOOON !!! MOUSSAILLON, ILS ONT TOUCHÉ UN DE NOS BATEAUX ! ")
    print("------------------------MA GRILLE ---------------------------")
    print_grille(grille)


def joueur_gagne(points) -> str:
    print(" Jack Sparrow serait très fière de vous capitaine, vous avez gagné avec " + points + " points")


def ordi_gagne(points) -> str:
    print("Capitaine , vous nous avez deçu....vous avez perdu avec : " + points + " points")


def egalite(points) -> str:
    print("C'était une très bonne partie mon capitaine, vous êtes à égalité avec " + points + " points chacun")


def chiffre_pas_valable() -> str:
    print("Chiffre pas valable")