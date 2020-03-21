from .conversionHexa import *
from .conversionVarInt import *
import unittest


class HexaTest(unittest.TestCase):

    def test_convertBigEndian(self):
        self.assertEqual('0x 07 1d 91', hexBigEndian(466321))

    def test_convertLittleEndian(self):
        self.assertEqual('0x 91 1d 07', hexLittleEndian(466321))

    def test_convertLittleEndianVarInt(self):
        self.assertEqual('0x fd 91 1d 07', hexLittleEndianVarInt(466321))

