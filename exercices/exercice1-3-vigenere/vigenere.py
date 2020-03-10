import string;
ALPH = string.ascii_uppercase
WHITESPACE = " "

def frequences(chaine, size=1):
    freq = {};
    vChaine = chaine.replace(" ", "");
    for index in range(len(vChaine)):
        charSeq = vChaine[index:index + size];
        if charSeq not in freq.keys():
            freq[charSeq] = 1;
        else:
            freq[charSeq] += 1;

    return {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)};

def formatFrequences(freqCharDict):
    freqDisplay = {};
    for key in freqCharDict:
        if freqCharDict[key] > 1:
            freqDisplay[key] = freqCharDict[key];

    return WHITESPACE.join("".join((str(k), str(v))) for k, v in freqDisplay.items());


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