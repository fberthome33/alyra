import unittest
from bitcoinCalculate import *

class MyTestCase(unittest.TestCase):
    def test_bitcoinsEnCirculation(self):
        self.assertEqual(50, bitcoinsEnCirculation(0));
        self.assertEqual(10500025.0, bitcoinsEnCirculation(210000));
        self.assertEqual(20979492.28515624, bitcoinsEnCirculation(2100001));


if __name__ == '__main__':
    unittest.main()
