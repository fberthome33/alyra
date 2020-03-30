from .calculatrice import *
import unittest


class CalcultriceTest(unittest.TestCase):

    def test_addOperator(self):
        self.assertEqual(16, calculate("12 4 +"));

    def test_SubstractOperator(self):
        self.assertEqual(8, calculate("12 4 -"));

    def test_Add_Mult_Operator(self):
        self.assertEqual(16, calculate("12 4 - 2 *"));

    def test_Equal_Operator(self):
        self.assertEqual(True, calculate("12 4 - 2 * 16 ="));

    def test_Greater_Operator(self):
        self.assertEqual(False, calculate("12 4 - 2 * 18 >"));
        self.assertEqual(True, calculate("12 4 - 2 * 1 >"));

    def test_Greater_Operator(self):
        self.assertEqual(True, calculate("12 4 - 2 * 18 <"));
        self.assertEqual(False, calculate("12 4 - 2 * 1 <"));

