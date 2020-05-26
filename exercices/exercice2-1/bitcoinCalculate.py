from recompense import *;

def bitcoinsEnCirculation(hauteurBloc):
    nbBitcoin = 0;
    index = 0;
    while  index <= hauteurBloc:
        nbBitcoin += recompenseBloc(index);
        index+=1;
    return round(nbBitcoin, 8);