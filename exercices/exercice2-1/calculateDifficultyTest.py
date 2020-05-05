import unittest
from calculateDifficulty import *

class CalculateDifficultyTestCase(unittest.TestCase):
    def test_calculerDifficulteFromCible(self):
        self.assertEqual(23.50125722290317, calculerDifficulteFromCible(
            1147152896345386682952518188670047452875537662186691235300769792000))
        self.assertEqual(2.695953529101131e+67, calculerDifficulteFromCible(1))

    def test_calculerDifficulteFromBits(self):
        self.assertEqual(23.5, calculerDifficulteFromBits("1c0ae493"))

    def test_blocReajustement(self):
        self.assertTrue(blocReajustement(556416))

if __name__ == '__main__':
    unittest.main()

