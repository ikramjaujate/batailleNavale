from unittest import *
from nose.tools import *
from unittest import mock
from batailleNavale.jeu_console import PlaceBateau
from batailleNavale.jeu_console import *

class TestPlaceBateau(TestCase):
    # def test_get_v(self):
    #     original_input = mock.builtins.input
    #     mock.builtins.input = lambda _: "v"
    #     self.assertEqual(PlaceBateau().v_ou_h(), "v")
    #     mock.builtins.input = original_input
    #
    # def test_get_h(self):
    #     original_input = mock.builtins.input
    #     mock.builtins.input = lambda _: "h"
    #     self.assertEqual(PlaceBateau().v_ou_h(), "h")
    #     mock.builtins.input = original_input

    # def test_autre_v_h(self):
    #     self.assertRaises(ValueError, lambda : PlaceBateau().v_ou_h())

    def test_nom(self):
        nom_joueur = nom
        self.assertEqual(type(nom_joueur), str)

    def test_difficulte(self):
        diff = difficulte
        if diff == "FACILE":
            self.assertEqual(len(total_bateau), 2)
        elif diff == "MOYEN":
            self.assertEqual(len(total_bateau), 3)
        elif diff == "DIFFICILE":
            self.assertEqual(len(total_bateau), 5)

    # def test_coord(self):
    #     coord = PlaceBateau().get_coordonnes()
    #     self.assertEqual(len(coord), 2)
    #     if len(coord) < 2:
    #         self.assertRaises(Exception, lambda : coord)
