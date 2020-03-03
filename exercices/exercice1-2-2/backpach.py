taille = [2000, 6000, 800, 700, 1200, 1000, 1300, 600]
pourboireTab = [13000, 9000, 2000, 1500, 3500, 2800, 5000, 1500]
weigthLimit = 6000;


def sumValue(weigthTab, valueTab):
    valueSum = 0;
    for weigth in weigthTab:
        valueSum += valueTab[taille.index(weigth)];
    return valueSum;


def backpackRecusif(weightTab, valueTab, weigthLimit, branch, result, maxValue):
    for i in range(len(weightTab)):
        if not weightTab[i] in branch:
            newBranch = branch[:];
            newBranch.append(weightTab[i]);
            if sum(newBranch) <= weigthLimit:
                backpackRecusif(weightTab, valueTab, weigthLimit, newBranch, result, maxValue);
            else:
                sumBranchWeigth = sum(branch);
                if sumBranchWeigth <= weigthLimit:
                    sumValues = sumValue(branch, valueTab);
                    if sumValues > maxValue:
                        maxValue = sumValues;
                        if result:
                            result.pop(0);
                        result.append((branch, sumBranchWeigth, maxValue));


def backpack(weightTab, valueTab, weigthLimit):
    result = [];
    prefix = [];
    backpackRecusif(weightTab, valueTab, weigthLimit, prefix, result, 0);
    return result[0][0],  result[0][1],  result[0][2];

result, weigthTransaction, valueTransaction = backpack(taille, pourboireTab, weigthLimit)
print("Resultat transaction: {}, weigth: {}, value: {}").format(result, weigthTransaction, valueTransaction);
