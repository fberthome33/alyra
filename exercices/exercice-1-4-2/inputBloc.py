import struct;
from binascii import hexlify
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


    def print(self):
        print(self.hash)
        print(self.outputIndex);
        print(self.signature);
        print(self.public_key);
        print(self.sequence);


def getEntryLength(data):

    firstOctet = str(data[0]);
    firstIndex = 0;
    varint_len = 0;
    if firstOctet == 'fd':
        firstIndex = 1;
        varint_len = 3;
    elif firstOctet == 'fe':
        firstIndex = 1;
        varint_len = 5;
    elif firstOctet == 'ff':
        firstIndex = 1;
        varint_len = 9;
    else:
        firstIndex = 0;
        varint_len = 1;

    return varint_len, int.from_bytes(data[firstIndex:varint_len], byteorder='little');

def decodeScriptSig(scriptSig, input_decode):
    varint_scriptsig_len, varIntScriptSig = getEntryLength(scriptSig);
    scriptSig = scriptSig[varint_scriptsig_len:]

    varint_signature_len, varIntSignature = getEntryLength(scriptSig);
    input_decode.signature = hex_to_str(scriptSig[varint_signature_len:varint_signature_len + varIntSignature]);

    publicKeyWrapper = scriptSig[varint_scriptsig_len + varIntSignature:];
    varint_plublickey_len, varIntPublicKey = getEntryLength(publicKeyWrapper);
    input_decode.public_key = hex_to_str(publicKeyWrapper[varint_plublickey_len:varint_plublickey_len + varIntPublicKey]);

def decodeInput(input):
    input_decode = Input();
    input_byteArray = bytearray.fromhex(input)


    input_decode.hash = hex_to_str(input_byteArray[0:HASH_FIELD_LEN]);
    input_decode.outputIndex = hex_to_str(input_byteArray[HASH_FIELD_LEN:HASH_FIELD_LEN + OUTPUTINDEX_FIELD_LEN]);

    scriptSig = input_byteArray[HASH_FIELD_LEN + OUTPUTINDEX_FIELD_LEN:-4];

    decodeScriptSig(scriptSig, input_decode);
    input_decode.sequence = hex_to_str(input_byteArray[-SIGNATURE_FIELD_LEN:]);
    return input_decode;


def hex_to_str(hex_array):
    return str(hexlify(hex_array), "utf-8");


inputTest  = (  "941e985075825e09de53b08cdd346bb67075ef0ce5c94f98853292d4bf94c10d01000000"
                "6b483045022100ab44ef425e6d85c03cf301bc16465e3176b55bba9727706819eaf07cf84cf52d02203f7dc7ae9ab36bead14dd3c83c8c030bf8"
                "ce596e692021b66441b39b4b35e64e012102f63ae3eba460a8ed1be568b0c9a6c947abe9f079bcf861a7fdb2fd577ed"
                "48a81Feffffff");

input_decode = decodeInput(inputTest);
input_decode.print()



