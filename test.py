import unittest
from juste_prix import verif

class TestJustePrix(unittest.TestCase):

    def test_bravo(self):
        resultat = verif(5,5)
        self.assertEqual(resultat, 0)

    def test_non_trouve(self):
        resultat = verif(5,3)
        self.assertEqual(resultat, 1)

if __name__ == '__main__':
    unittest.main()