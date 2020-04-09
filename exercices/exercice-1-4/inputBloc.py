import struct;
from binascii import hexlify
from varintutils import *
from codecs import encode  # alternative

HASH_FIELD_LEN = 32;
OUTPUTINDEX_FIELD_LEN = 4;
SIGNATURE_FIELD_LEN = 4;

class Input:
    hash = bytes()
    outputIndex = bytes()
    scriptSig = bytes()
    signature = bytes()
    public_key = bytes()
    sequence = bytes()
    length = 0;


    def print(self):
        print(self.hash)
        print(self.outputIndex);
        print(self.signature);
        print(self.public_key);
        print(self.sequence);


def decodeScriptSig(scriptSig, input_decode):
    varint_signature_len, varIntSignature = getVarInt(scriptSig);
    input_decode.signature = hex_to_str(scriptSig[varint_signature_len:varint_signature_len + varIntSignature]);

    publicKeyVarInt = scriptSig[ varint_signature_len + varIntSignature:];
    varint_plublickey_len, varIntPublicKey = getVarInt(publicKeyVarInt);

    input_decode.public_key = hex_to_str(publicKeyVarInt[varint_plublickey_len:varint_plublickey_len + varIntPublicKey]);


def decodeScriptSigVarInt(varInt_scriptSig, input_decode):
    varint_scriptsig_len, varIntScriptSigValue = getVarInt(varInt_scriptSig);
    scriptSig = varInt_scriptSig[varint_scriptsig_len:]

    decodeScriptSig(scriptSig, input_decode)

    return varint_scriptsig_len + varIntScriptSigValue;

def decodeStrInput(input):
    input_byteArray = bytearray.fromhex(input)
    return decodeInput(input_byteArray)

def decodeInput(input_byteArray):
    input_decode = Input();

    input_decode.hash = hex_to_str(input_byteArray[0:HASH_FIELD_LEN]);
    input_decode.outputIndex = hex_to_str(input_byteArray[HASH_FIELD_LEN:HASH_FIELD_LEN + OUTPUTINDEX_FIELD_LEN]);

    scriptSig = input_byteArray[HASH_FIELD_LEN + OUTPUTINDEX_FIELD_LEN:-4];

    script_sig_len = decodeScriptSigVarInt(scriptSig, input_decode);
    index_start_sequence = HASH_FIELD_LEN + OUTPUTINDEX_FIELD_LEN + script_sig_len;
    input_decode.sequence = hex_to_str(input_byteArray[index_start_sequence:index_start_sequence + OUTPUTINDEX_FIELD_LEN]);
    input_decode.length = index_start_sequence + OUTPUTINDEX_FIELD_LEN
    return input_decode;


def hex_to_str(hex_array):
    return str(hexlify(hex_array), "utf-8");



def test():
    inputTest  = (  "941e985075825e09de53b08cdd346bb67075ef0ce5c94f98853292d4bf94c10d01000000"
                    "6b483045022100ab44ef425e6d85c03cf301bc16465e3176b55bba9727706819eaf07cf84cf52d02203f7dc7ae9ab36bead14dd3c83c8c030bf8"
                    "ce596e692021b66441b39b4b35e64e012102f63ae3eba460a8ed1be568b0c9a6c947abe9f079bcf861a7fdb2fd577ed"
                    "48a81Feffffff");
    print(len(inputTest))
    input_decode = decodeStrInput(inputTest);
    input_decode.print()
    print(input_decode.length)

if __name__ == "__main__":
    # execute only if run as a script
    test()


