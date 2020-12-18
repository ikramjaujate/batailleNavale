from abc import ABC,abstractmethod

class ViewInterface(ABC):

    #proprio a la interfaz del juego no al juego en el mismo
    @abstractmethod
    def demandeNomUtilisateur(self):
        """
        Function qui permet à l'utilisateur de introduire son nom
        :return:
        """
        pass

    @abstractmethod
    def getDifficulte(self):
        """
        Function qui permet à l'utilisateur de définir un niveau
        :return:
        """
        pass

    @abstractmethod
    def utilisateur_placer_bateaux(self, grille: list, bateau: dict, niveau: str):
        """
        Function qui permet à l'utilisateur de placer les bateau dans la grille

        :param grille: la grille sur laquelle il y a le placement des bateau
        :param bateau: contient sous forme de dictionnaire, tous les bateaux a placé sur la grille

        PRE: -
        POST: Renvoi la grille ainsi que ajoute dans une variable global le coordonnées des bateaux placé par l'utilisateur
        """

        pass

    @abstractmethod
    def ordinateur_placer_bateaux(self, grille: list, bateau: dict, niveau):
        """
        Function qui permet à l'ordinateur de placer les bateaux aléatoirement dans la grille

        :param grille: la grille sur laquelle il y a le placement des bateau
        :param bateau: contient sous forme de dictionnaire, tous les bateaux a placé sur la grille

        PRE: -
        POST: Renvoi la grille ainsi que ajoute dans une variable global le coordonnées des bateaux placé par l'ordinateur de forme aléatoire
        """
        pass


    @abstractmethod
    def utilisateur_tir(self, grille: list):
        """
        Permet à l'utilisateur de tirer sur une case de la grille ennemi

        :param grille: list

        PRE: -
        POST : Renvoi la grille avec la case que l'utilisateur à viser

        """

        pass

    @abstractmethod
    def tir_ordinateur(self, grille: list):
        """
        Générer des coordonnées aléatoires pour que l'ordinateur réalise les mouvements

        PRE: -
        POST : Renvoi la grille avec la case que l'utilisateur à viser

        """
        pass
