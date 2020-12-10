from unittest import *

from batailleNavale.jeu_console import *
from batailleNavale.ocean import *


class TestDifficulte(TestCase):
    def test_get_hauteur(self):
        niveau_facile = "FACILE"
        self.assertEqual(Difficulte().get_hauteur(niveau_facile), 6)

        niveau_pas_bon = "a"
        self.assertRaises(ValueError, lambda: Difficulte().get_hauteur(niveau_pas_bon))

    def test_get_tours(self):
        niveau_facile = "FACILE"
        self.assertEqual(Difficulte().get_tours(niveau_facile), 8)

        niveau_pas_bon = "a"
        self.assertRaises(ValueError, lambda: Difficulte().get_hauteur(niveau_pas_bon))


