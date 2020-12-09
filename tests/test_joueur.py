from unittest import TestCase
from batailleNavale.joueur import Joueur

class TestJoueur(TestCase):
    def test_get_nom(self):
        nom_joueur = "ikram"
        self.assertEqual(Joueur(nom_joueur).getNom(), "ikram")
        self.assertRaises(ValueError, lambda : Joueur(1).getNom())
