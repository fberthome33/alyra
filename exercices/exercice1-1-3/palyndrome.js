function estPalindrome(str) {
    var strTmp = str.trim();
    var spaceLeft= 0, spaceRight = 0;
    for (var i = 0; i < strTmp.length / 2; i++) {
        while (strTmp[i + spaceLeft] === ' ') {
            spaceLeft++;
        }
        while (strTmp[strTmp.length - i - spaceRight - 1] === ' ') {
            spaceRight++;
        }
        if(strTmp[i + spaceLeft] !== strTmp[strTmp.length - i - spaceRight - 1]) {
            return false;
        }
      }

    return true;
}

var str = "       Hello World!        ";
console.log(str);
var trimmedStr = str.trim();
console.log(trimmedStr);

console.log(estPalindrome("ESOPE RESTE ICI ET SE   REPOE"));