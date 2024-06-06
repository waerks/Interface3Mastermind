# MASTERMIND
from random import randint

code = []
CodeLength = 4

lettres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(CodeLength):
    index = randint(0, len(lettres)-1)
    lettre = lettres[index]
    code.append(lettre)

ask = None

compteur = 0
NbreEssais = 12

while ask != code and compteur < NbreEssais:
    compteur += 1
    print(f"Essai n°{compteur}. Vous avez {NbreEssais} essais.")
    ask = input(f"Donnez {CodeLength} lettres pour deviner le code: ")

    while len(ask) != CodeLength:
        ask = input(f"Donnez {CodeLength} lettres pour deviner le code: ")

    ask = list(ask)

    LettresCorrectes = []
    LettresIncorrectes = []

    for i in range(CodeLength):
        if code[i] == ask[i]:
            LettresCorrectes.append(i)

    for i_ask in range(CodeLength):
        for i_code in range (CodeLength):
            if code[i_code] == ask[i_ask]:
                if i_code not in LettresCorrectes and i_ask not in LettresCorrectes:
                    if i_code not in LettresIncorrectes:
                        LettresIncorrectes.append(i_code)
                        break

    print(f"Il y a {len(LettresCorrectes)} lettre(s) bien placée(s) et {len(LettresIncorrectes)} lettre(s) mal placée(s).")

if code == ask:
    print("Whow! Vous avez trouvé!")
else:
    print(f"Oups... Vous avez perdu ! Le code était: {code}")