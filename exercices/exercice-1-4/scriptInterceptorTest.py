import unittest


from scriptInterpretor import *


class ScriptInterpretorTest(unittest.TestCase):

    def test_hash160(self):
        # Given
        text_to_hash = '0372cc7efb1961962bba20db0c6a3eebdde0ae606986bf76cb863fa460aee8475c'
        text_to_hash_bt = bytearray.fromhex(text_to_hash);

        # Then
        hashtext_from_input = hex_to_str(hash160(text_to_hash_bt));

        # Else
        text_output_hash = "7c3f2e0e3f3ec87981f9f2059537a355db03f9e8";
        self.assertEqual(text_output_hash, hashtext_from_input);

    def test_decodeInput(self):
        scriptSig = ("0x483045022100d544eb1ede691f9833d44e5266e923dae058f702d2891e4ee87621a433ccdf4f022021e40"
                     "5c26b0483cd7c5636e4127a9510f3184d1994015aae43a228faa608362001210372cc7efb1961962bba20db0c6a3eebdde0ae60698"
                     "6bf76cb863fa460aee8475c")
        scriptPubKey = "0x76a9147c3f2e0e3f3ec87981f9f2059537a355db03f9e888ac"
        self.assertTrue(verificationP2PKH(scriptSig, scriptPubKey));



if __name__ == '__main__':
    unittest.main()
