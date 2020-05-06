from math import *

versionprog = "1.1.2"
majdate = "16/09/2019"

print("")
print("pythag version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":
        print("")
        x = eval(input("Valeur longueur premier coter : "))
        print("")
        y = eval(input("Valeur longueur deuxième coter : "))
        print("")
        longHypCarre = (x**2) + (y**2)
        longHyp = sqrt(longHypCarre)
        print("Longueur de l'hypothénuse au carré:")
        print(longHypCarre)
        print("")
        print("Longueur de l'hypothénuse :")
        print(longHyp)
    elif option == "2":
        print("Infos :")
        print(" - Nom : Pythag")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
    elif option == "3":
        print("")
        print("Fin du programme")
        break