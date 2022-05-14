import unittest

from src.calculator.basic import add


class AddTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(1, 1), 2)
