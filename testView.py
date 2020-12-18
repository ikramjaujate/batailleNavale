from batailleNavale.ViewInterface import ViewInterface

class testView(ViewInterface):

    def demandeNomUtilisateur(self):
        return "my test Name"

    def getDifficulte(self):
        return "DIFFICILE"

    def utilisateur_placer_bateaux(self, grille: list, bateau: dict, niveau: str):
        return [[['  ', 'A', 'B', 'C', 'D', 'E', 'F'], [' 1', '.', '.', '.', '.', '.', '.'], [' 2', '.', '.', '.', '.', '.', '.'], [' 3', '.', '.', '.', '.', '.', '.'], [' 4', '.', '.', '.', '.', '.', '.'], [' 5', '.', '.', '.', '.', '.', '.'], [' 6', '.', '.', '.', '.', '.', '.']], [[(1, 4), (2, 4)], [(1, 1), (2, 1), (3, 1)]]]

    def ordinateur_placer_bateaux(self, grille: list, bateau: dict, niveau):
        return [[['  ', 'A', 'B', 'C', 'D', 'E', 'F'], [' 1', '.', '.', '.', '.', '.', '.'], [' 2', '.', '.', '.', '.', '.', '.'], [' 3', '.', '.', '.', '.', '.', '.'], [' 4', '.', '.', '.', '.', '.', '.'], [' 5', '.', '.', '.', '.', '.', '.'], [' 6', '.', '.', '.', '.', '.', '.']], [[(2, 5), (2, 6)], [(1, 4), (2, 4), (3, 4)]]]
    
    def utilisateur_tir(self, grille: list):
        pass

    def tir_ordinateur(self, grille: list):
        pass


