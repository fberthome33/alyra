import string
import random
import time
import logging
logging.basicConfig(level=logging.INFO)

def randomString(length):
    chaine = ""
    for index in range(0, length):
        chaine += random.choice(string.ascii_uppercase)
    return chaine;

def rechercheDebut(prefix, length):
    start_time = time.time()
    while True:
        randomStr = randomString(length);
        logging.debug(randomStr);
        if randomStr.startswith(prefix):
            break;
    print("--- %s seconds ---" % (time.time() - start_time))


for longueur in range (8, 13):
    print("longueur", longueur)
    rechercheDebut("AAAA", longueur)

