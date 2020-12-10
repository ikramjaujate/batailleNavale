import unittest
from batailleNavale.difficulte import Difficulte
from batailleNavale.joueur import Joueur
from batailleNavale.ocean import Ocean
from batailleNavale.bateau import *
from batailleNavale.tir import another_turn
from batailleNavale.tir import Tirer


class TestGeneral(unittest.TestCase):
    def test_get_nom_joueur(self):
        nom_joueur = "ikram"
        self.assertEqual(Joueur(nom_joueur).getNom(), "ikram")
        self.assertRaises(ValueError, lambda : Joueur(1))

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

    def test_another_tours(self):
        another = another_turn(5)
        self.assertEqual(type(another), bool)
        self.assertEqual(another, True)

    def test_tir_etat(self):
        t = Tirer()
        ocean = Ocean(6)
        ma_grille = ocean.grille()
        ma_grille[1][1] = "X"
        self.assertEqual(t.tir(ma_grille, 1, 4), "rate")
        self.assertEqual(t.tir(ma_grille, 1, 1), 'toucheAvant')


if __name__ == '__main__':
    unittest.main()
