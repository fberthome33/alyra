import string;

ALPH = string.ascii_uppercase

def vigenere(chaine, key, decrypt = None):
    vigenereString = "";
    index = 0;
    while index < len(chaine):
        while chaine[index] == ' ':
            vigenereString += chaine[index];
            index += 1;
        mult = 1;
        if decrypt:
            mult = -1;
        vigenereString += ALPH[(ALPH.index(chaine[index]) + mult * ALPH.index(key[index % len(key)])) % len(ALPH)];
        index += 1;
    return vigenereString;

def regroupement(chaine, taille):
    chaineTmp = chaine.replace(" ", "").upper();
    group = ["" for x in range(taille)]
    for index in range(len(chaineTmp)):
        group[index % taille] += chaineTmp[index];
    return group;



chaineToEncrypt = "VOI  CIU  NME  SSA  GE";
key = "ABC  ABC  ABC  ABC  AB";
encryptChaine = vigenere(chaineToEncrypt, key);
print(encryptChaine);
print(vigenere(encryptChaine, key, decrypt=True));


print(regroupement ("Mes vieilles tantes", 3));