from .conversionHexa import conversionHexa, convertBigToLittleEndian, formatHexArray;


def hexLittleEndianVarInt(number):
    hexBigEndian = conversionHexa(number);
    hexLittleEndian = convertBigToLittleEndian(hexBigEndian);
    if number > 253:
        hexLittleEndian[0:0] = ['f', 'd']
    return formatHexArray(hexLittleEndian);


