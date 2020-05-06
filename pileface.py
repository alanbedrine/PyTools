from random import *

versionprog = "1.0"
majdate = "15/09/2019"

print("")
print("pileface version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":
        a = randint(1, 2)

        if a == 1:
            print("")
            print("pile")
        else:
            print("")
            print("face")
    elif option == "2":
        print("Infos :")
        print(" - Nom : Formule")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
    elif option == "3":
        print("")
        print("Fin du programme")
        break