import struct;
from binascii import hexlify
from varintutils import *
from codecs import encode  # alternative

AMOUNT_FIELD_LEN = 8;

class Output:
    amount = int
    scriptPubKey = bytes()
    length = 0;


    def print(self):
        print(self.amount)
        print(self.scriptPubKey);

def decodeScriptSig(scriptSig, input_decode):
    varint_scriptsig_len, varIntScriptSig = getVarInt(scriptSig);
    scriptSig = scriptSig[varint_scriptsig_len:]

    varint_signature_len, varIntSignature = getVarInt(scriptSig);
    input_decode.signature = hex_to_str(scriptSig[varint_signature_len:varint_signature_len + varIntSignature]);

    publicKeyWrapper = scriptSig[varint_scriptsig_len + varIntSignature:];
    varint_plublickey_len, varIntPublicKey = getVarInt(publicKeyWrapper);
    input_decode.public_key = hex_to_str(publicKeyWrapper[varint_plublickey_len:varint_plublickey_len + varIntPublicKey]);
    return varint_scriptsig_len + varIntScriptSig;

def decodeStrInput(input):
    input_byteArray = bytearray.fromhex(input)
    return decodeInput(input_byteArray)

def decodeOutput(output_byteArray):
    output_decode = Output();
    print("amount", hex_to_str(output_byteArray[0:AMOUNT_FIELD_LEN]))
    output_decode.amount = int.from_bytes(output_byteArray[0:AMOUNT_FIELD_LEN], byteorder='little');

    scriptSig = output_byteArray[AMOUNT_FIELD_LEN:];

    varint_signature_len, varIntSignature = getVarInt(scriptSig);
    output_decode.scriptPubKey =  hex_to_str(output_byteArray[AMOUNT_FIELD_LEN + varint_signature_len : AMOUNT_FIELD_LEN + varint_signature_len + varIntSignature]);
    output_decode.length = AMOUNT_FIELD_LEN + varint_signature_len + varIntSignature;
    return output_decode;


def hex_to_str(hex_array):
    return str(hexlify(hex_array), "utf-8");



