from unittest import TestCase

from batailleNavale.jeu_console import ma_grille
from batailleNavale.ocean import *

class TestOcean(TestCase):
    def test_grille(self):
        ocean = Ocean(hauteur=8)
        grille = ocean.grille()
        self.assertIsNone(ocean.print_grille(grille))
        self.assertEqual(type(grille), list)

    # def test_get_hauteur(self):

    # def test_get_tours(self):
    #



