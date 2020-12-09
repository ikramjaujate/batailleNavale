import unittest
from batailleNavale.bateau import *

class Bateau(unittest.TestCase):
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
