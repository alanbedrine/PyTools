from math import *

versionprog = "1.2.1"
majdate = "17/09/2019"

print("")
print("calcvol version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":
        print("Type de volume à calculer")
        print(" - Cube (1)")
        print(" - Parallélépipède rectangle (2)")
        print(" - Pyramide à base carrée (3)")
        print(" - Sphère (4)")
        print(" - Cylindre (5)")
        print(" - Prisme (6)")
        print("")

        op = float(input("Qu'elle volume voulez vous calculez ? : "))

        if op == 1:
            print("")
            longcube = eval(input("Longueur des côtés : "))

            volcube = longcube**3

            print("")
            print(volcube)
        elif op == 2:
            print("")
            longparaLo = eval(input("Longueur: "))
            longparaLa = eval(input("Largeur: "))
            longparaHa = eval(input("Hauteur: "))

            volpara = longparaLo * longparaLa * longparaHa

            print("")
            print(volpara)
        elif op == 3:
            print("")
            longpyrBa = eval(input("Base: "))
            longpyrHa = eval(input("Hauteur: "))

            volpyr = (longpyrBa*longpyrHa)/3

            print("")
            print(volpyr)
        elif op == 4:
            print("")
            longsphRa = eval(input("Rayon : "))

            volsph = 4 / 3 * pi * longsphRa ** 3

            print("")
            print(volsph)
        elif op == 5:
            print("")
            longcyRa = eval(input("Rayon : "))
            longcyHa = eval(input("Hauteur : "))

            volcy = pi * longcyRa ** 2 * longcyHa

            print("")
            print(volcy)
        elif op == 6:
            print("")
            longpriLo = eval(input("Longueur : "))
            longpriLa = eval(input("Largeur : "))
            longpriHa = eval(input("Hauteur : "))

            volpri = 1 / 2 * longpriLo * longpriLa * longpriHa

            print("")
            print(volpri)
        else:
            print("erreur type de volume non trouvés")
    elif option == "2":
        print("Infos :")
        print(" - Nom : Calcvol")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
    elif option == "3":
        print("")
        print("Fin du programme")
        break