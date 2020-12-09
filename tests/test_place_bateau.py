from unittest import *
from nose.tools import *
from unittest import mock
from batailleNavale.jeu_console import PlaceBateau


class TestPlaceBateau(TestCase):
    def test_get_v(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "v"
        self.assertEqual(PlaceBateau().v_ou_h(), "v")
        mock.builtins.input = original_input

    def test_get_h(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "h"
        self.assertEqual(PlaceBateau().v_ou_h(), "h")
        mock.builtins.input = original_input

