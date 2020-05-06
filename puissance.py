from math import *

versionprog = "1.0"
majdate = "22/11/2019"

print("")
print("Puissance version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":
        print("")
        print("Type de puissance à calculer")
        print(" - 10 première puissance (1)")
        print("")

        op = float(input("Qu'elle volume voulez vous calculez ? : "))

        if op == 1:
            print("")
            print("- 10 première puissance :")
            print("")
            a = eval(input("Valeur 1 : "))
            print("")

            for (p=0, p++, p<10):
                calc = a**p

                print("")
                print(calc)
                print("")
        else:
            print("")
            print("erreur type de volume non trouvés")
            print("")
    elif option == "2":
        print("")
        print("Infos :")
        print(" - Nom : Puissance")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
        print("")
    elif option == "3":
        print("")
        print("Fin du programme")
        print("")
        break