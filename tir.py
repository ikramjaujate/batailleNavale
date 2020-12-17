class Tirer:

    def tir(self, grille: list, x: int, y: int):
        """
        Vérifier l'état de la case dans laquelle les utilisateurs souhaitent tiré

        :param grille: list
        :param x: int
        :param y: int

        PRE: -
        POST : Renvoi l'état de la case dans laquelle les utilisateurs ont tiré
        """
        etat = ""
        if grille[x][y] == ".":
            etat += "rate"
            return etat
        elif grille[x][y] == "*" or grille[x][y] == "X":
            etat += "toucheAvant"
            return etat
        else:
            etat += "touche"
            return etat

