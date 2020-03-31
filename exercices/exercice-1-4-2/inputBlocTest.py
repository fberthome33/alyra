from .inputBloc import *
import unittest


class InputBlocTest(unittest.TestCase):

    def test_decodeInput(self):
        inputText = ("941e985075825e09de53b08cdd346bb67075ef0ce5c94f98853292d4bf94c10d01000000"
                     "6b483045022100ab44ef425e6d85c03cf301bc16465e3176b55bba9727706819eaf07cf84cf52d02203f7dc7ae9ab36bead14dd3c83c8c030bf8"
                     "ce596e692021b66441b39b4b35e64e012102f63ae3eba460a8ed1be568b0c9a6c947abe9f079bcf861a7fdb2fd577ed"
                     "48a81Feffffff");
        decoded_result = decodeInput(inputText)
        self.assertEqual("941e985075825e09de53b08cdd346bb67075ef0ce5c94f98853292d4bf94c10d", decoded_result.hash)
        self.assertEqual("01000000", decoded_result.outputIndex)

        tested_sign_value = "3045022100ab44ef425e6d85c03cf301bc16465e3176b55bba9727706819eaf07cf84cf52d02203f7dc7ae9ab36bead14dd3c83c8c030bf8ce596e692021b66441b39b4b35e64e01"
        self.assertEqual(tested_sign_value, decoded_result.signature)
        self.assertEqual("02f63ae3eba460a8ed1be568b0c9a6c947abe9f079bcf861a7fdb2fd577ed48a81", decoded_result.public_key)
        self.assertEqual("feffffff", decoded_result.sequence);


