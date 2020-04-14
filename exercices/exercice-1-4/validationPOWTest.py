import unittest
from validationPOW import *


class ValidationPowTest(unittest.TestCase):
    def test_validationPow(self):
        self.assertEqual(True, validationPOW(("01000000008de6ae7a37b4f26a763f4d65c5bc7feb1ad9e3ce0fff4190c067f0000000000913281d"
                "b730c5cff987146330508c88cc3e642d1b9f5154854764fd547e0a54eaf26849ffff001d2e4a4c3d010100000001000000"
                "0000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d013fffffffff0100f205"
                "2a010000004341041ada81ea00c11098d2f52c20d5aa9f5ba13f9b583fda66f2a478dd7d95a7ab615159d98b63df2e6f3e"
                "cb3ef9eda138e4587e7afd31e7f434cbb6837e17feb0c5ac00000000")))


if __name__ == '__main__':
    unittest.main()
