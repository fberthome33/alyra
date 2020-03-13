dictHexa = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'};


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
    return '0x' + ' '.join([''.join(map(str, hexArray[i:i + 2])) for i in range(0, len(hexArray), 2)])


def hexBigEndian(number):
    hexBigEndian = conversionHexa(number);
    return formatHexArray(hexBigEndian);


def hexLittleEndian(number):
    hexLittleEndian = conversionHexa(number);
    for index in range(0, int(len(hexLittleEndian) / 2) - 1, 2):
        tmp = hexLittleEndian[index: index + 2];
        hexLittleEndian[index: index + 2] = hexLittleEndian[
                                            len(hexLittleEndian) - index - 2:len(hexLittleEndian) - index];
        hexLittleEndian[len(hexLittleEndian) - index - 2:len(hexLittleEndian) - index] = tmp;

    return formatHexArray(hexLittleEndian);


def convertHexa(number):
    if number >= 10:
        return dictHexa.get(number);
    return number;


hexBigEndian = hexBigEndian(466321);
print("conv1", hexBigEndian);  # → 0x 07 1d 91 (big endian)
hexLittleEndian = hexLittleEndian(466321);
print("conv2", hexLittleEndian)  # → 0x 91 1d 07 (little endian)
