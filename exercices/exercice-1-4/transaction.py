import struct;
from binascii import hexlify
from codecs import encode  # alternative
from inputBloc import *
from outputBloc import *
from varintutils import *

VERSION_FIELD_LEN = 4;
AMOUNT_FIELD_LEN = 4;
LOCKTIME_FIELD_LEN = 4;


class Transaction:
    version = bytes();
    inputs = [];
    outputs = [];
    locktime = bytes();

    def print(self):
        print(self.version);
        print("input")
        for input in self.inputs:
            input.print();
        print("output")
        for output in self.outputs:
            output.print();
        print(self.locktime);

def decodeScriptSig(scriptSig, input_decode):
    varint_scriptsig_len, varIntScriptSig = getVarInt(scriptSig);
    scriptSig = scriptSig[varint_scriptsig_len:]

    varint_signature_len, varIntSignature = getVarInt(scriptSig);
    input_decode.signature = hex_to_str(scriptSig[varint_signature_len:varint_signature_len + varIntSignature]);

    publicKeyWrapper = scriptSig[varint_scriptsig_len + varIntSignature:];
    varint_plublickey_len, varIntPublicKey = getVarInt(publicKeyWrapper);
    input_decode.public_key = hex_to_str(
        publicKeyWrapper[varint_plublickey_len:varint_plublickey_len + varIntPublicKey]);


def decodeStrTransaction(transaction_string):
    transaction_bytearray = bytearray.fromhex(transaction_string)
    return decodeTransaction(transaction_bytearray);

def decodeTransaction(transaction_bytearray):
    transaction_decode = Transaction();

    transaction_decode.version = hex_to_str(transaction_bytearray[0:VERSION_FIELD_LEN]);
    len_varint_inputs, nb_inputs = getVarInt(transaction_bytearray[VERSION_FIELD_LEN:]);

    print("nb_inputs", nb_inputs)
    start_index = VERSION_FIELD_LEN + len_varint_inputs;
    for nbInput in range(0, nb_inputs):
        input = decodeInput(transaction_bytearray[start_index:])
        start_index += input.length
        transaction_decode.inputs.append(input);

    len_varint_outputs, nb_outputs = getVarInt(transaction_bytearray[start_index:]);
    print("nb_inputs", nb_outputs)
    for nboutput in range(0, nb_outputs):
        output = decodeOutput(transaction_bytearray[start_index + len_varint_outputs:])
        start_index += output.length
        transaction_decode.outputs.append(output);

    transaction_decode.locktime = hex_to_str(transaction_bytearray[len_varint_outputs + start_index : len_varint_outputs + start_index + LOCKTIME_FIELD_LEN]);
    return transaction_decode;


def hex_to_str(hex_array):
    return str(hexlify(hex_array), "utf-8");


transation = (  "0100000001f129de033c57582efb464e94ad438fff493cc4de4481729b859712368582"
                "75c2010000006a4730440220155a2ea4a702cadf37052c87bfe46f0bd24809759acff8"
                "d8a7206979610e46f6022052b688b784fa1dcb1cffeef89e7486344b814b0c578133a7"
                "b0bce5be978a9208012103915170b588170cbcf6380ef701d19bd18a526611c0c69c62"
                "d2c29ff6863d501affffffff02ccaec817000000001976a9142527ce7f0300330012d6"
                "f97672d9acb5130ec4f888ac18411a000000000017a9140b8372dffcb39943c7bfca84"
                "f9c40763b8fa9a068700000000");


if __name__ == "__main__":
    # execute only if run as a script
    input_decode = decodeStrTransaction(transation);
    input_decode.print()


