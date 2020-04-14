from inputBloc import *
from transaction import *
import hashlib
from cibleAtteinte import *

HASH_FIELD_LEN = 32;

def hash160(databyte):
    m = hashlib.sha256()
    m.update(databyte);
    return m.digest();

def validationPOW(bloc):
    bloc_byteArray = bytearray.fromhex(bloc)
    header = bloc_byteArray[0:80];
    print("header", hex_to_str(header))
    bits = header[72:72+4];
    print("target", hex_to_str(bits))
    print(hex_to_str(bits[0:1]))
    exponent = int.from_bytes(bits[0:1], byteorder='little');
    coeff = hex_to_str(bits[1:3]);

    hash_header = hex_to_str(hash160(hash160(header)));
    return cibleAtteinte(coeff, exponent, hash_header)




