dictHexa = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'd'};


def conversionHexa(number):
    bigEndian = [];
    while number > 0:
        remainder = number % 16;
        quotient = int(number / 16);
        bigEndian.insert(0, convertHexa(remainder));
        number = quotient;
    if len(bigEndian) % 2 == 1:
        bigEndian.insert(0, 0);
    return bigEndian;


def formatHexArray(hexArray):
    return '0x ' + ' '.join([''.join(map(str, hexArray[i:i + 2])) for i in range(0, len(hexArray), 2)])


def hexBigEndian(number):
    hexBigEndian = conversionHexa(number);
    return formatHexArray(hexBigEndian);

def convertBigToLittleEndian(hexBigEndian):
    for index in range(0, int(len(hexBigEndian) / 2) - 1, 2):
        tmp = hexBigEndian[index: index + 2];
        hexBigEndian[index: index + 2] = hexBigEndian[
                                            len(hexBigEndian) - index - 2:len(hexBigEndian) - index];
        hexBigEndian[len(hexBigEndian) - index - 2:len(hexBigEndian) - index] = tmp;
    return hexBigEndian;

def hexLittleEndian(number):
    hexBigEndian = conversionHexa(number);
    hexLittleEndian = convertBigToLittleEndian(hexBigEndian);

    return formatHexArray(hexLittleEndian);


def convertHexa(number):
    if number >= 10:
        return dictHexa.get(number);
    return number;

def test():
    hexBigEndian = hexBigEndian(466321);
    print("conv BigEndian", hexBigEndian);  # → 0x 07 1d 91 (big endian)
    hexLittleEndian = hexLittleEndian(466321);
    print("conv LittleIndian", hexLittleEndian)  # → 0x 91 1d 07 (little endian)
