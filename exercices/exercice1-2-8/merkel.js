const sha256 = require('crypto-js/sha256');

params = process.argv.slice(2);

if(params.length % 2 != 0) {
    params.push(params[params.length - 1]);
}
let hash = sha256(params[0]);

console.log(params)
merkelTree = merkel(params);

displayMerkel(merkelTree, params.length);

function merkel(hashArray) {
    merkelTree = [];
    hashArray.forEach(element => merkelTree.push(sha256(element).toString()));
    let n = merkelTree.length;
    for (i = 1; i <= n; i+=2) {
        let hash = sha256(merkelTree[n-1] + merkelTree[n]).toString();
        merkelTree.push(hash);
        n += 1;
    }
    return merkelTree;
}


function displayMerkel(merkelTree, n) {
    if(n % 2 == 0) {
        displayMerkel(merkelTree.slice(n), n / 2);
    }
}
