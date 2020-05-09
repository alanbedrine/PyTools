from math import *

versionprog = "1.5"
majdate = "15/09/2019"

print("")
print("interval version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":
        print("")
        y = eval(input("Saisir une valeur de y (debut d'intervalle): "))

        print("")
        z = eval(input("Saisir une valeur de z (fin d'intervalle): "))

        print("")
        print("Different type d'intervalle :")
        print("- Ouvert (1)")
        print("- Semi-Ouvert (2)")
        print("- fermé (3)")

        print("")
        op = float(input("Saisir le type d'intervalle : "))

        if op == 1 or op == 2 or op == 3:
            print("")
            x = eval(input("Saisir une valeur de x (nombre à trouver): "))

            if y <= z:
                if op == 1:
                    if x >= y or x <= z or x <= y or x >= z:
                        print("")
                        print("x appartient à l'intervalle")
                    else:
                        print("")
                        print("x n'appartient pas à l'intervalle")
                elif op == 2:
                    if x >= y or x >= z:
                        print("")
                        print("x appartient à l'intervalle")
                    else:
                        print("")
                        print("x n'appartient pas à l'intervalle")
                elif op == 3:
                    if x >= y and x <= z:
                        print("")
                        print("x appartient à l'intervalle")
                    else:
                        print("")
                        print("x n'appartient pas à l'intervalle")
            else:
                print("")
                print("erreur d'intervalle")
        else:
            print("")
            print("ce type d'intervalle n'existe pas")
    elif option == "2":
        print("")
        print("Infos :")
        print(" - Nom : Interval")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
        print(" - Contribuer / source  : https://github.com/alanbedrine/PyTools")
        print("")
    elif option == "3":
        print("")
        print("Fin du programme")
        break