from math import *

versionprog = "1.0"
majdate = "08/10/2019"

print("")
print("distance version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":

        print("")
        def dist(xa,ya,xb,yb):
            d = sqrt((xb-xa)**2+(yb-ya)**2)
            return d




    elif option == "2":
        print("Infos :")
        print(" - Nom : Distance")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
    elif option == "3":
        print("")
        print("Fin du programme")
        break