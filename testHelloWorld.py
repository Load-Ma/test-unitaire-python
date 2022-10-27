import unittest
import main
from datetime import datetime


class TestMain(unittest.TestCase):
    def test_hello_morning(self):
        date = datetime.now()
        self.assertEqual(main.hello(date), "good morning world")

    def test_hello_noon(self):
        date = datetime.now().replace(hour=12)
        self.assertEqual(main.hello(date), "Bon appétit")

    def test_hello_evening(self):
        date = datetime.now().replace(hour=15)
        self.assertEqual(main.hello(date), "Bon après-midi")

    def test_goodby_morning(self):
        date = datetime.now().replace(hour=10)
        self.assertEqual(main.goodby(date), "Bonne journée")

    def test_goodby_noon(self):
        date = datetime.now().replace(hour=12)
        self.assertEqual(main.goodby(date), "Bon appétit")

    def test_goodby_evening(self):
        date = datetime.now().replace(hour=15)
        self.assertEqual(main.goodby(date), "Au revoir")

    def test_invert_with_palindrome(self):
        word = "laval"
        self.assertEqual(main.invertWord(word), "Bien dit !")

    def test_invert_without_palindrome(self):
        word = "la phrase est turbo longue"
        self.assertEqual(main.invertWord(word), word[::-1])
