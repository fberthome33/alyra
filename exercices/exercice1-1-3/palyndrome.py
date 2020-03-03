def estPalindrome(string):
    strTmp = string.replace(" ", "");
    for index in range(int(len(strTmp) / 2)):
        if strTmp[index] != strTmp[len(strTmp) - index - 1]:
            return False;
    return True;

str = "ABCd"
print(str[::-1])

print(len("ESOPE RESTE ICI ET SE REPOSE") / 2)
print(estPalindrome("ESOPE RESTE ICI ET SE REPOSE"))
print(estPalindrome("YOOYP"))