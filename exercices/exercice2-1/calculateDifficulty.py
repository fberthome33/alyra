def cible(coefficient, exposant):
    coefficient_int = int.from_bytes(coefficient, byteorder='big')
    cible = coefficient_int * 2 ** (8 * (exposant - 3));
    return cible;


def calculerDifficulteFromCible(cible):
    return 2.7 * 10**67 / cible;


def calculerDifficulteFromBits(bits):
    bits_byteArray = bytearray.fromhex(bits)
    exponent = int.from_bytes(bits_byteArray[0:1], byteorder='little');
    coeff = bits_byteArray[1:4];
    return calculerDifficulteFromCible(cible(coeff, exponent));

def blocReajustement(bloc):
    return bloc % 2016 == 0;

