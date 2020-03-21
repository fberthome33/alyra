import string;

ALPH = string.ascii_uppercase
WHITESPACE = " "


def frequences(chaine, size=1):
    freq = {};
    vChaine = chaine.replace(" ", "");
    for index in range(len(vChaine)):
        charSeq = vChaine[index:index + size];
        if charSeq not in freq.keys():
            freq[charSeq] = [index];
        else:
            freq[charSeq].append(index);

    return {k: v for k, v in sorted(freq.items(), key=lambda item: len(item[1]), reverse=True)};


def formatFrequences(freqCharDict):
    freqDisplay = {};
    for key in freqCharDict:
        if len(freqCharDict[key]) > 1:
            freqDisplay[key] = freqCharDict[key];

    return WHITESPACE.join("".join((str(k), str(v))) for k, v in freqDisplay.items());


def vigenere(chaine, key, decrypt=None):
    vigenereString = "";
    index = 0;
    mult = 1;
    if decrypt:
        mult = -1;
    while index < len(chaine):
        while chaine[index] == ' ':
            vigenereString += chaine[index];
            index += 1;

        print(index % len(key));
        indexDecode = (ALPH.index(chaine[index]) + mult * ALPH.index(key[index % len(key)])) % len(ALPH);
        print(indexDecode);
        # vigenereString += ALPH[indexDecode];
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

print(regroupement("Mes vieilles tantes", 3));

text = '''PVADGHFLSHPJNPLUVAGXVVRBRUKCGXEVQINPVBXLVZLRMKFLSXEZQXOGCCHXEICIXUKSCXKEDDKORRXHPHSXGGJRRHPESTJWVBTJWVJFNGJSCLQ
LBJGUVSATNRJXFKKCBTKJOJXEVJJBQLATNZHSXECUCIBGELTGVGCJOGERPMQLRBHOVLIKGMCAXTCCHXEICIXUKYRVGJQXUNVYIHWJATLVSGTGRFSGJ
WFGXEARSCITFZAXOVBJLGTPTMEVOJBHRGIITFZAXOVBPGUCCHXEICIVGJRFNKCNTNVVRGXFZTJEILCIKCYGGXXVJTHGUGEXHZLXMRRPSXEYGUYTVPA
XPZEBXFLQEAKEVHBXFSHOQLJTSRVPRXTCCHLGTPTMUTCHMNRRPVJVBTECIYXLQECCNPJCCLEVQIECKYRAGUCATRYGAHUFNWBGRSRHPKPPBTVJTF
AJRTKGVQIICIBTYKEGIBQEBJGCLRGXQIBGXSLCAXRIMQEGDCXEGJRXGCTATLUZZAXCCYGTKJMCWCEQAXUDWHMGICHWGCYCMKHSXMGJCJEUUCGT
TVQXGKKGTLRRPKBGELTGVRJPVQDNGXJVLHBQEBJFAJRTKGVRAXEYPXLVZYCBUDCTLVSCPNEFSEINLQGTFZAPEGEADKGCCBRUKCGXGJRRXSLGTLVR
ZHHNLKTGVZLPVEVQHBDCCPECIYXLQERWHORQSTSLGCEGGJJLIIYCWVYCDEQXGTGFVRDNVVJPVJICIBGERTFGUGTOCCCTMNRPTYGICCVGVLRHTVYJ
CQLPSAWZBTMQLRTECKFTHNFEXXEYPTMKVLCXKEQXLVVQJKNVDPBVHSTECIYIBQEYABVVQPKTVRTTWJCJBNUSBRUKCGXNVKNLVVPTXUKQPVTVQX
OQLQEKGWCGXBZJTLVKPPGUTCCWCERXEGJRSBXZLPEQIQFNGCCHXEICIXUKNGHHRLTEGJCRKGKCHMKDKPGGERPECTMCWKKGDGJLKPBPVGAXUK
FJFCZLTMEVQIIQLPFNQZDXWGCCPLCMMRTVZMCECGPDUNVKPMKJYIBQEJPKGWJTQKFLEAKCMHHRYGFNGZLIXTIMVXNVQTVTVRXGVVPGHIVJWNOR
LXMGUSHXEICILKTCITKKSCFAJRTKGVJAXPVJXGVVPGHIVPPBVGYHEGDWHMGICCXUKNPLWECRTVVEDKKVNWBNFQDIJZOJX'''

keyLengthMax = 7
for keySize in range(3, keyLengthMax):
    print("Try Size:", keySize)
    print(formatFrequences(frequences(text, keySize)));

decrypt = vigenere(text, "H", decrypt=True);
print(decrypt[58:63], decrypt);
