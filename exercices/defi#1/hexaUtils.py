from binascii import hexlify

def calculerDifficulteFromCible(cible):
    return (2**16 - 1) * 2**208 / cible;

def switchBigLittleEndian(hexBigEndian):
    prefix = ""
    startIndex = 0;
    if hexBigEndian[0:2] == "0x":
        prefix = "0x"
        startIndex = 2;
    return prefix + "".join(reversed([hexBigEndian[i:i+2] for i in range(startIndex, len(hexBigEndian), 2)]))


def switchBigLittleEndian(hexEndian):
    return hexEndian[::-1]


def littleEndianToInt(hex):
    return int.from_bytes(hex, byteorder='little')

def hex_to_str(hex_array):
    return str(hexlify(hex_array), "utf-8");