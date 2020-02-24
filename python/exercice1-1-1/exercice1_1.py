import random

print("Devinez un nombre entre 1 et 100")
choix = random.randint(0, 100)

def message_by_diff(psaisie_user, pchoix):
    diff = abs(psaisie_user - pchoix)
    sign = "plus" if psaisie_user - pchoix < 0 else "moins"
    if 6 <= diff <= 10:
        print("C'est un peu " + sign)
    elif 1 <= diff <= 5:
        print("C'est un tout petit peu " + sign)
    else:
        print("C'est beaucoup " + sign)

while True:
    saisie_user = int(input())
    if saisie_user == choix:
        print("Exact !")
        break
    else:
        message_by_diff(saisie_user, choix)

