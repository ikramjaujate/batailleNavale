def print_grille(grille: list):
    """
    Function qui permet de afficher la grille en console
    :param grille: la grille qui est utilisé
    PRE : -
    POST : Renvoi la grille sous forme de string pour qu'elle soit afficher dans la console

    """
    for ligne in grille:
        print("  ".join(ligne))

def plouf(grille: list):
    print("Capitaine, vous avez rate le tir")
    print("------------------------GRILLE ENNEMI ---------------------------")
    print_grille(grille)


def boum(grille: list):
    print("Bravo capitaine, vous avez touché le bateau")
    print("------------------------GRILLE ENNEMI ---------------------------")
    print_grille(grille)


def ploufOrdi(grille: list):
    print("HIHI, ils ont touché la balaine ")
    print("------------------------MA GRILLE ---------------------------")
    print_grille(grille)


def boumOrdi(grille: list):
    print("NOOOOON !!! MOUSSAILLON, ILS ONT TOUCHÉ UN DE NOS BATEAUX ! ")
    print("------------------------MA GRILLE ---------------------------")
    print_grille(grille)

def joueur_gagne():
    print("Jack Sparrow serait très fière de vous capitaine, ")

def ordi_gagne():
    print("Capitaine, vous nous avez deçu....")

def egalite():
    print("C'était une très bonne partie mon capitaine, vous êtes à égalité ")

def chiffre_pas_valable():
    print("Chiffre pas valable")