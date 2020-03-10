WHITESPACE = " "


def frequences(chaine, size=1):
    freq = {};
    vChaine = chaine.replace(" ", "");
    for index in range(len(vChaine)):
        charSeq = vChaine[index:index + size];
        if charSeq != " ":
            if charSeq not in freq.keys():
                freq[charSeq] = 1;
            else:
                freq[charSeq] += 1;

    return {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)};


def formatFrequences(freqCharDict):
    return WHITESPACE.join("".join((str(k), str(v))) for k, v in freqCharDict.items());


freqDict = frequences("Etre contesté, c’est être constaté");
freqDict2 = frequences("Etre contesté, c’est être constaté", 2);
print(formatFrequences(freqDict));
print(formatFrequences(freqDict2));
