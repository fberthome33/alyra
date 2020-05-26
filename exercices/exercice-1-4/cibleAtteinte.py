

def cibleAtteinte(coefficient, exposant, hash):

    coefficient_int = int.from_bytes(bytearray.fromhex(coefficient), byteorder='little')
    print(coefficient_int)
    cible = coefficient_int * 2 ** (8*(exposant-3));
    return int(hash, 16) < cible;

print(cibleAtteinte("3218a5", 23, "00000000000000000019b2634066a100e56ed58a0ae40ca5a4e2d1dba6a4be22"));