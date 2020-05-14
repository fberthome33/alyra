import struct;
from binascii import hexlify
from codecs import encode  # alternative
from transaction import *
from varintutils import *
from hexaUtils import *

BLOC_SIZE_FIELD_LEN = 4;
BLOC_HEADER_FIELD_LEN = 80;

HEADER_VERSION_FIELD_LEN = 4;
HEADER_PREVIOUS_VERSION_FIELD_LEN = 32;
HEADER_MERKLEROOT_VERSION_FIELD_LEN = 32;
HEADER_TIMESTAMP_FIELD_LEN = 4;
HEADER_BITS_FIELD_LEN = 4;
HEADER_NONCE_FIELD_LEN = 4;

class Bloc:
    header = None;
    transactionNumber = None;
    transactions = None;

    def __init__(self, header, transactionNumber, transactions):
        self.header = header
        self.transactionNumber = transactionNumber
        self.transactions = transactions

class Header:
    version = None;
    previousBloc = None;
    merkleRoot = None;
    timestamp = None;
    bits = None;
    nonce = None;




def decodeHeader(headerHex):
    header = Header()
    print("header", hex_to_str(headerHex));
    index = 0;
    header.version = littleEndianToInt(headerHex[index:index + HEADER_VERSION_FIELD_LEN]);
    index += HEADER_VERSION_FIELD_LEN;

    header.previousBloc = hex_to_str(switchBigLittleEndian(headerHex[index:index + HEADER_PREVIOUS_VERSION_FIELD_LEN]));
    index += HEADER_PREVIOUS_VERSION_FIELD_LEN;

    header.merkleRoot = hex_to_str(switchBigLittleEndian(headerHex[index:index + HEADER_MERKLEROOT_VERSION_FIELD_LEN]));
    index += HEADER_MERKLEROOT_VERSION_FIELD_LEN;

    header.timestamp = littleEndianToInt(headerHex[index:index + HEADER_TIMESTAMP_FIELD_LEN]);
    index += HEADER_TIMESTAMP_FIELD_LEN;

    bits = switchBigLittleEndian(headerHex[index:index + HEADER_BITS_FIELD_LEN]);
    header.bits = hex_to_str(bits);
    index += HEADER_BITS_FIELD_LEN;

    cible = extractCible(bits);
    header.cible = cible
    header.difficulty = calculerDifficulteFromCible(cible)

    header.nonce = littleEndianToInt(headerHex[index:index + HEADER_NONCE_FIELD_LEN]);
    index += HEADER_NONCE_FIELD_LEN;
    
    return header;


def decodeStrBloc(bloc_string):
    bloc_bytearray = bytearray.fromhex(bloc_string)
    return decodeBloc(bloc_bytearray);

def decodeBloc(blocHex):

    index = 0;
    header = decodeHeader(blocHex[index:BLOC_HEADER_FIELD_LEN])
    index += BLOC_HEADER_FIELD_LEN

    lenIntTran, varIntTran = getVarInt(blocHex[index:]);
    transactionNumber = varIntTran;


    start_index = BLOC_HEADER_FIELD_LEN + lenIntTran;
    trans = []
    for nbInput in range(0, transactionNumber ):
        tran = decodeTransaction(blocHex[start_index:])
        start_index += tran.length
        trans.append(tran);
    bloc = Bloc(header, transactionNumber, trans)

    return bloc;


def hex_to_str(hex_array):
    return str(hexlify(hex_array), "utf-8");

def extractCible(bits):
    print("bits")
    exponent = int.from_bytes(bits[0:1], byteorder='big');
    coefficient = hex_to_str(bits[1:4]);
    coefficient_int = int.from_bytes(bytearray.fromhex(coefficient), byteorder='big')
    print(coefficient_int)
    return coefficient_int * 2 ** (8*(exponent-3));


if __name__ == "__main__":
    # execute only if run as a script
    bloc_decode = decodeStrBloc("");
    print(bloc_decode)


