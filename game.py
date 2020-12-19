from batailleNavale.joueur import Joueur
from batailleNavale.difficulte import Difficulte
from batailleNavale.bateau import *
from batailleNavale.ocean import Ocean
from batailleNavale.print_text import joueur_gagne, boum, boumOrdi, ploufOrdi, egalite, ordi_gagne, plouf

class Jeu:
    total_bateau = {}
    ma_grille = []
    grille_tirs = []
    coord_bateau_utilisateur = []
    coord_bateau_ordi = []
    grille_ennemie = []
    
    def __init__(self, view):
        self.niveau = 0
        self.view = view
        self.difficulty = "DIFFICILE"
        self.tours = 0

    def placeBateau(self):
        if self.difficulty == "FACILE":
            self.total_bateau[TheDyingGull("The Dying Gull").getNom] = TheDyingGull("The Dying Gull").length
            self.total_bateau[HmsIntercepteur("HMS Intercepteur").getNom] = HmsIntercepteur("HMS Intercepteur").length
        elif self.difficulty == "MOYEN":
            self.total_bateau[TheDyingGull("The Dying Gull").getNom] = TheDyingGull("The Dying Gull").length
            self.total_bateau[HmsIntercepteur("HMS Intercepteur").getNom] = HmsIntercepteur("HMS Intercepteur").length
            self.total_bateau[SilentMary("Silent Mary").getNom] = SilentMary("Silent Mary").length
        elif self.difficulty == "DIFFICILE":
            self.total_bateau[TheDyingGull("The Dying Gull").getNom] = TheDyingGull("The Dying Gull").length
            self.total_bateau[HmsIntercepteur("HMS Intercepteur").getNom] = HmsIntercepteur("HMS Intercepteur").length
            self.total_bateau[SilentMary("Silent Mary").getNom] = SilentMary("Silent Mary").length
            self.total_bateau[QueenAnneRevenge("Queen Anne's Revenge").getNom] = QueenAnneRevenge("Queen Anne's Revenge").length
            self.total_bateau[BlackPearl("Black Pearl").getNom] = BlackPearl("Black Pearl").length

        difficulter = Difficulte()
        self.niveau = difficulter.get_hauteur(self.difficulty)
        self.tours = difficulter.get_tours(self.difficulty)

        ocean = Ocean(self.niveau)
        self.ma_grille = ocean.grille()
        self.grille_ennemie = ocean.grille()
        self.grille_tirs = ocean.grille()

        userBat = self.view.utilisateur_placer_bateaux(self.ma_grille,self.total_bateau,self.niveau)
        self.coord_bateau_utilisateur = userBat[1]
        computerBat = self.view.ordinateur_placer_bateaux(self.grille_tirs,self.total_bateau,self.niveau)
        self.coord_bateau_ordi = computerBat[1]


    def play(self):
        nom_humain = self.view.demandeNomUtilisateur()
        joueur_humain = Joueur(nom_humain)
        self.difficulty = self.view.getDifficulte()
        self.placeBateau()
        joueur_ordi = Joueur("ordinateur")

        while self.view.continuer :
            while self.tours != 0:
                tir = self.view.utilisateur_tir(self.grille_tirs)
                while tir["status"] == "toucheAvant":
                    tir = self.view.utilisateur_tir(self.grille_tirs)
                if tir["status"] == "rate":
                    self.grille_tirs[tir["x"]][tir["y"]] = "*"
                    self.grille_ennemie[tir["x"]][tir["y"]] = "*"
                    plouf(self.grille_ennemie)
                elif tir["status"] == "touche":
                    joueur_humain.joueurs_points += 1
                    self.grille_tirs[tir["x"]][tir["y"]] = "X"
                    self.grille_ennemie[tir["x"]][tir["y"]] = "X"
                    for liste in self.coord_bateau_ordi:
                        for element in liste:
                            if (tir["x"],tir["y"]) == element:
                                liste.remove((tir["x"], tir["y"]))
                    boum(self.grille_ennemie)
                    verifier_coord_ordi = [tableau for tableau in self.coord_bateau_ordi if tableau != []]
                    if len(verifier_coord_ordi) == 0:
                        joueur_gagne(joueur_humain.getPoints())
                        self.view.continuer = 0
                        break

                tir = self.view.tir_ordinateur(self.ma_grille)
                if tir["status"] == "touche":
                    joueur_ordi.joueurs_points += 1
                    self.ma_grille[tir["x"]][tir["y"]] = 'X'
                    for liste in self.coord_bateau_utilisateur :
                        for element in liste:
                            if (tir["x"], tir["y"]) == element:
                                liste.remove((tir["x"], tir["y"]))
                    boumOrdi(self.ma_grille)

                    verifier_coord_utilisateur = [x for x in self.coord_bateau_utilisateur if x != []]
                    if len(verifier_coord_utilisateur) == 0:
                        ordi_gagne(joueur_humain.getPoints())
                        self.view.continuer = 0
                        break
                elif tir["status"] == "rate":
                    self.ma_grille[tir["x"]][tir["y"]] = "*"
                    ploufOrdi(self.ma_grille)

                self.tours = self.tours - 1

            if joueur_humain.joueurs_points == joueur_ordi.joueurs_points:
                egalite(str(joueur_humain.getPoints()))
            elif joueur_humain.joueurs_points > joueur_ordi.joueurs_points:
                joueur_gagne(str(joueur_humain.getPoints()))
            elif joueur_humain.joueurs_points < joueur_ordi.joueurs_points:
                ordi_gagne(str(joueur_humain.getPoints()))

            self.view.demandeContinuerJeu()

            while type(self.view.continuer) != int:
                self.view.chiffre_pas_valable()
                self.view.demandeContinuerJeu()

            break
