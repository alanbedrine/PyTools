from math import *

versionprog = "1.0"
majdate = "23/09/2019"

print("")
print("varevol version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":

        print("")
        varinitial = eval(input("Valeur initiale : "))
        print("")
        varfinal = eval(input("Valeur finale : "))
        print("")
        varevol = ( ( varfinal - varinitial ) / varinitial ) * 100
        print("Variation de l'évolution :", varevol, "%")

    elif option == "2":
        print("")
        print("Infos :")
        print(" - Nom : Varevol")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
        print(" - Contribuer / source  : https://github.com/alanbedrine/PyTools")
        print("")
    elif option == "3":
        print("")
        print("Fin du programme")
        break