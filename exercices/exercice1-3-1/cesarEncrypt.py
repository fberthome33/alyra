def chiffreCesar(pStringToEncode, pDecalage):
    vEncodedString=""
    for char in pStringToEncode:
        vEncodedString += chr(ord(char) + pDecalage);
    return vEncodedString;

chaineTest2="J'aime bien, les burger de chez PAPI BURGER!!!";
encodedString = chiffreCesar(chaineTest2, 1);
print(encodedString);

decodedString = chiffreCesar(encodedString, -1);
print(decodedString);