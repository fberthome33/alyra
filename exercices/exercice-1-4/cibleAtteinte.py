def cibleAtteinte(exposant, coefficient, hash):
    exposant_int = x = int(exposant, 16)
    cible = coefficient * 2 ** (8*(exposant_int-3));
    return int(hash, 16) < cible;

print(cibleAtteinte("3218a5", 23, "00000000000000000019b2634066a100e56ed58a0ae40ca5a4e2d1dba6a4be22"));