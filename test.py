import unittest
from batailleNavale.difficulte import Difficulte
from batailleNavale.game import Game
from batailleNavale.joueur import Joueur
from batailleNavale.ocean import Ocean
from batailleNavale.bateau import *
from batailleNavale.prints_phrases import print_grille, plouf, boum, ploufOrdi, boumOrdi
from batailleNavale.tir import Tirer
from batailleNavale.utils.couleur import Couleurs

class TestGeneral(unittest.TestCase):
    def test_get_nom_joueur(self):
        nom_joueur = "ikram"
        self.assertEqual(Joueur(nom_joueur).getNom(), "ikram")
        self.assertRaises(TypeError, lambda : Joueur(1))

    def test_get_haut(self):
        ocean = Ocean(6)
        self.assertEqual(ocean.get_haut(), 6)

    def test_grille(self):
        ocean = Ocean(6)
        self.assertTrue(ocean.grille(), list)


    def test_placer_bateaux(self):
        ocean = Ocean(6)
        ma_grille = ocean.grille()
        self.assertEqual(type(ocean.placer_bateaux(ma_grille, 1, 'b', "v", 2, 2)), list)

    def test_silent_mary(self):
        silent_mary = SilentMary("Silent Mary")
        self.assertEqual(silent_mary.length, 3)
        self.assertFalse(silent_mary.length == 4)
        self.assertTrue(type(silent_mary.getNom) == str)

    def test_black_pearl(self):
        black_pearl = BlackPearl("Black Pearl")
        self.assertEqual(black_pearl.length, 5)
        self.assertFalse(black_pearl.length == 4)
        self.assertTrue(type(black_pearl.getNom) == str)

    def test_hms_intercepteur(self):
        hms_intercepteur = HmsIntercepteur("HMS Intercepteur")
        self.assertEqual(hms_intercepteur.length, 3)
        self.assertFalse(hms_intercepteur.length == 4)
        self.assertTrue(type(hms_intercepteur.getNom) == str)

    def test_dying_gull(self):
        dying_gull = TheDyingGull("The Dying Gull")
        self.assertEqual(dying_gull.length, 2)
        self.assertFalse(dying_gull.length == 1)
        self.assertTrue(type(dying_gull.getNom) == str)

    def test_anne_revenge(self):
        anne_revenge = QueenAnneRevenge("Queen Anne's Revenge")
        self.assertFalse(anne_revenge.length == 2)
        self.assertEqual(anne_revenge.length, 4)
        self.assertTrue(type(anne_revenge.getNom) == str)

    def test_get_hauteur_facile(self):
        d = Difficulte()
        niveau_facile = "FACILE"
        self.assertEqual(d.get_hauteur(niveau_facile), 6)
        niveau_pas_bon = "a"
        self.assertRaises(ValueError, lambda: Difficulte().get_hauteur(niveau_pas_bon))

    def test_get_hauteur_moyen(self):
        d = Difficulte()
        niveau_moyen = "MOYEN"
        self.assertEqual(d.get_hauteur(niveau_moyen), 8)
        niveau_pas_bon = "a"
        self.assertRaises(ValueError, lambda: Difficulte().get_hauteur(niveau_pas_bon))

    def test_get_hauteur_difficile(self):
        d = Difficulte()
        niveau_difficile= "DIFFICILE"
        self.assertEqual(d.get_hauteur(niveau_difficile), 11)
        niveau_pas_bon = "a"
        self.assertRaises(ValueError, lambda: Difficulte().get_hauteur(niveau_pas_bon))

    def test_get_tours_facile(self):
        d = Difficulte()
        self.assertEqual(d.get_tours("FACILE"), 8)
        self.assertRaises(ValueError, lambda: Difficulte().get_hauteur("a"))

    def test_get_tours_moyen(self):
        d = Difficulte()
        self.assertEqual(d.get_tours("MOYEN"), 12)
        self.assertRaises(ValueError, lambda: Difficulte().get_hauteur("a"))

    def test_get_tours_difficile(self):
        d = Difficulte()
        self.assertEqual(d.get_tours("DIFFICILE"), 20)
        self.assertRaises(ValueError, lambda: Difficulte().get_hauteur("a"))

    def test_tir_etat(self):
        t = Tirer()
        ocean = Ocean(6)
        ma_grille = ocean.grille()
        ma_grille[1][1] = "X"
        self.assertEqual(t.tir(ma_grille, 1, 4), "rate")
        self.assertEqual(t.tir(ma_grille, 1, 1), 'toucheAvant')
        ma_grille[1][2] = "T"
        self.assertEqual(t.tir(ma_grille, 1,2), "touche")

    def test_couleur_end(self):
        self.assertEqual(Couleurs.CEND, '\33[0m' )
        self.assertTrue(Couleurs.CEND == '\33[0m')

    def test_couleur_noir(self):
        self.assertEqual(Couleurs.CBLACK, '\33[30m' )
        self.assertTrue(Couleurs.CBLACK == '\33[30m')

    def test_couleur_rouge(self):
        self.assertEqual(Couleurs.CRED, '\33[31m')
        self.assertTrue(Couleurs.CRED == '\33[31m')

    def test_couleur_vert(self):
        self.assertEqual(Couleurs.CGREEN, '\33[32m')
        self.assertTrue(Couleurs.CGREEN == '\33[32m')

    def test_couleur_jaune(self):
        self.assertEqual(Couleurs.CYELLOW, '\33[33m')
        self.assertTrue(Couleurs.CYELLOW == '\33[33m')

    def test_couleur_blue(self):
        self.assertEqual(Couleurs.CBLUE, '\33[34m')
        self.assertTrue(Couleurs.CBLUE == '\33[34m')

    def test_couleur_violet(self):
        self.assertEqual(Couleurs.CVIOLET, '\33[35m')
        self.assertTrue(Couleurs.CVIOLET == '\33[35m')

    def test_couleur_beige(self):
        self.assertEqual(Couleurs.CBEIGE, '\33[36m')
        self.assertTrue(Couleurs.CBEIGE == '\33[36m')

    def test_couleur_blanc(self):
        self.assertEqual(Couleurs.CWHITE, '\33[37m')
        self.assertTrue(Couleurs.CWHITE == '\33[37m')

    def test_game_variables_globales(self):
        self.assertTrue(type(Game.total_bateau), list)
        self.assertTrue(type(Game.ma_grille), list)
        self.assertTrue(type(Game.grille_tirs), list)
        self.assertTrue(type(Game.coord_bateau_utilisateur), list)
        self.assertTrue(type(Game.grille_ennemie), list)

    def test_phrases(self):
        ocean = Ocean(6)
        grille = ocean.grille()
        self.assertTrue(type(print_grille(grille)), str )
        self.assertTrue(type(plouf(grille)), str )
        self.assertTrue(type(boum(grille)), str)
        self.assertTrue(type(ploufOrdi(grille)), str )
        self.assertTrue(type(boumOrdi(grille)), str )
if __name__ == '__main__':
    unittest.main()
