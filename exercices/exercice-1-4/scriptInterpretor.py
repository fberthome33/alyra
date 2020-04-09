from inputBloc import *
import hashlib
from varintutils import *


def printStack(stack):
    print("startStack")
    for value in stack:
        print(value)
    print("endStack")

def hash160_str(str):
    return hash160(bytearray.fromhex(str));

def hash160(databyte):
    m = hashlib.sha256()
    m.update(databyte);
    res_hash_256 = m.digest()

    h = hashlib.new('ripemd160');
    h.update(res_hash_256);
    return h.digest();

def verificationP2PKH(scriptSig, scriptPubKey):
    input = Input();
    startIndex = 0;
    if scriptSig.startswith('0x'):
        startIndex = 2;
    scriptSigArray = bytearray.fromhex(scriptSig[startIndex:]);
    decodeScriptSig(scriptSigArray, input);
    print("signature", input.signature);
    print("publicKey", input.public_key);

    stack = [];
    stack.append(input.signature);
    stack.append(input.public_key);

    startIndex = 0;
    if scriptPubKey.startswith('0x'):
        startIndex = 2;
    scriptPubArray = bytearray.fromhex(scriptPubKey[startIndex:])

    index = 0;
    while index < len(scriptPubArray):
        octet = scriptPubArray[index:index+1];
        octet_str = hex_to_str(octet);

        if octet_str == '00':
            stack.append();
        elif octet_str == '51':
            stack.append(1);
        elif octet_str == '76':
            stack.append(stack[len(stack) - 1]);
        elif octet_str == '93':
            number1 = stack.pop();
            number2 = stack.pop();
            stack.append(number1+number2);
        elif octet_str == '88':
            hash_from_scriptPubKey = stack.pop();
            calculte_hash = stack.pop();
            if calculte_hash != hash_from_scriptPubKey:
                stack.append(False);
                return False;
        elif octet_str == 'a9':
            elem1 = stack.pop();
            elemArray = bytearray.fromhex(elem1);
            hash160_bt = hash160(elemArray);
            stack.append(hex_to_str(hash160_bt));
        elif octet_str == 'ac':
            pass;
        else:
            hashpubkey = scriptPubArray[index:];
            varint_hashPubKey_len, varIntHashPubKey = getVarInt(hashpubkey);
            stack.append(hex_to_str(hashpubkey[varint_hashPubKey_len:varint_hashPubKey_len + varIntHashPubKey]));
            index += varint_hashPubKey_len + varIntHashPubKey - 1;
        index += 1;
    return True;
