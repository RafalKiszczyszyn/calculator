import unittest

from src.calculator.basic import add, sub


class AddTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, add(1, 1))


class SubTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, sub(1, 1))
