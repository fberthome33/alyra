import unittest
from recompense import *

class RecompenseTestCase(unittest.TestCase):
    def test_recompenseBloc(self):
        self.assertEqual(50, recompenseBloc(0));
        self.assertEqual(25, recompenseBloc(210000));
        self.assertEqual(0.04882812, recompenseBloc(2100001));

if __name__ == '__main__':
    unittest.main()
