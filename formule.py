from math import *

versionprog = "7.0"
majdate = "16/12/2019"

print("")
print("formule version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":
        print("")
        print("Type de matière :")
        print(" - Science Physique (1)")
        print(" - Mathématique (2)")
        print(" - SES (3)")
        print("")

        print("")
        opmatiere = input("Qu'elle matières voulez vous acceder ? : ")
        print("")

        if opmatiere == "1":
            print("")
            print("Type de volume à calculer :")
            print(" - Masse volumique (1)")
            print(" - Densités (2)")
            print(" - Concentration massique (3)")
            print(" - Lois des tensions (4)")
            print(" - Lois d'ohm (5)")
            print(" - Lois des tensions (en serie) (6)")
            print(" - Lois des tensions (en derivation) (7)")
            print(" - Lois des noeuds (8)")
            print(" - Masse atome par des constituant (9)")
            print(" - Notation atomique (10)")
            print(" - Configuration éléctronique (11)")
            print("")

            op = float(input("Qu'elle volume voulez vous calculez ? : "))

            if op == 1:
                print("")
                print("- Masse volumique :")
                print("p = m/V")
                print("m = p x V")
                print("V = m/p")
                print("")
            elif op == 2:
                print("")
                print("- Densités :")
                print("d = p/p eau")
                print("")
            elif op == 3:
                print("")
                print("- Concentration massique :")
                print("m = solutés")
                print("V = solution")
                print("Cm = m/V")
                print("m = Cm x V")
                print("V = m/Cm")
                print("")
            elif op == 4:
                print("")
                print("- Lois des tensions :")
                print("Uad - Uab - Uac = 0")
                print("")
            elif op == 5:
                print("")
                print("- Lois d'ohm :")
                print("U = R x I")
                print("I = U / R")
                print("R = U / I")
                print("")
            elif op == 6:
                print("")
                print("- Lois des tensions (en serie) :")
                print("Ug = U1 + U2")
                print("")
            elif op == 7:
                print("")
                print("- Lois des tensions (en derivation) :")
                print("Ug = U1 = U2")
                print("")
            elif op == 8:
                print("")
                print("- Lois des noeuds :")
                print("I1 + I2 = I3 + I4")
                print("")
            elif op == 9:
                print("")
                print("- Masse atome par des constituant (en kg) :")
                print("Proton : 1,6726x10**-27")
                print("Neutron : 1,6749x10**-27")
                print("Electron : 9,1094x10**-31")
                print("")
            elif op == 10:
                print("")
                print("- Notation atomique :")
                print("X : le symbole de l'atome considéré")
                print("A : le nombre de nucléons du noyau (nb de proton + neutrons)")
                print("Z : le numero atomique (nb de proton)")
                print("")
            elif op == 11:
                print("")
                print("- Configuration éléctronique :")
                print("1s2 2s2 2p6 3s2 3p6")
                print("")
            else:
                print("")
                print("erreur type de formule non trouvés")
                print("")
        elif opmatiere == "2":
            print("")
            print("Type de volume à calculer :")
            print(" - Cube (1)")
            print(" - Parallélépipède rectangle (2)")
            print(" - Pyramide à base carrée (3)")
            print(" - Sphère (4)")
            print(" - Cylindre (5)")
            print(" - Prisme (6)")
            print("")

            print("")
            op = float(input("Qu'elle formule voulez vous calculez ? : "))
            print("")

            if op == 1:
                print("")
                print("- Cube :")
                print("coter³")
                print("")
            elif op == 2:
                print("")
                print("- Parallélépipède rectangle :")
                print("longueur x largeur x hauteur")
                print("")
            elif op == 3:
                print("")
                print("- Pyramide à base carrée :")
                print("(base x hauteur) / 3 ")
                print("")
            elif op == 4:
                print("")
                print("- Sphère :")
                print("4 / 3 x pi x rayon³")
                print("")
            elif op == 5:
                print("")
                print("- Cylindre :")
                print("pi * rayon² * hauteur")
                print("")
            elif op == 6:
                print("")
                print("- Prisme:")
                print("1 / 2 * longueur * largeur * hauteur")
                print("")
        else:
            print("")
            print("erreur matière non trouvés")
            print("")
    elif option == "2":
        print("")
        print("Infos :")
        print(" - Nom : Formule")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
        print("")
    elif option == "3":
        print("")
        print("Fin du programme")
        break