from random import randint
#fonction qui permet de générer un chiffre aléatoirement
#randint : aléatoire entre a et b
def random_colonne(gri):
    return randint(1, len(gri[0]) - 1)

def random_ligne(gri):
    return randint(1, len(gri) - 1)
