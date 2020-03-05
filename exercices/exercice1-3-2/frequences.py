WHITESPACE = " "


def frequences(chaine):
    freq = {};
    for char in chaine:
        if char != " ":
            if char not in freq.keys():
                freq[char] = 1;
            else:
                freq[char] += 1;

    return {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)};


def formarFrequences(freqCharDict):
    return WHITESPACE.join("".join((str(k), str(v))) for k, v in freqCharDict.items());


freqDict = frequences("Etre contesté, c’est être constaté");
print(formarFrequences(freqDict));
