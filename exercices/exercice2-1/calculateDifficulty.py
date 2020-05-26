def cible(coefficient, exposant):
    coefficient_int = int.from_bytes(coefficient, byteorder='big')
    cible = coefficient_int * 2 ** (8 * (exposant - 3));
    return cible;


def calculerDifficulteFromCible(cible):
    #return 0xffff << 208 / cible;
    return 2.7 * 10**67 / cible;


def calculerDifficulteFromBits(bits):
    #return 0xffff / int(bits[4:10], 16) * 256 ** (29 - int(bits[2:4], 16))
    if bits[0] == "0" and bits[1] == 'x':
        bits = bits [2:]
    bits_byteArray = bytearray.fromhex(bits)
    exponent = int.from_bytes(bits_byteArray[0:1], byteorder='little');
    coeff = bits_byteArray[1:4];
    return calculerDifficulteFromCible(cible(coeff, exponent));

def blocReajustement(hauteurBloc):
    return hauteurBloc % 2016 == 0;

print(calculerDifficulteFromCible(1147152896345386682952518188670047452875537662186691235300769792000))
#23.50125722290317
print(calculerDifficulteFromCible(1))
#2.695953529101131e+67
