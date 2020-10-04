from math import *

versionprog = "7.0"
majdate = "16/12/2019"

print("")
print("Physique version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":
        print("")
        print("Type de volume à calculer :")
        print(" - Def elec (1)")
        print(" - Puissance moyenne (2)")
        print(" - Rendement (3)")
        print(" - Fréquence (4)")
        print(" - Valeur efficace (5)")
        print(" - Valeur moyenne tension (6)")
        print(" - Position voltemètres (7)")
        print(" - Tension sinusoidale u(t) (8)")
        print("")

        op = float(input("Qu'elle volume voulez vous calculez ? : "))

        if op == 1:
            print("")
            print("- Def elec :")
            print("intensite => I1 => A")
            print("tentions => U1 => V")
            print("puissance => W")
            print("")
        elif op == 2:
            print("")
            print("- Puissance moyenne :")
            print("P = E/t")
            print("P = en What")
            print("E = joule")
            print("1W = 3600J")
            print("")
        elif op == 3:
            print("")
            print("- Rendement :")
            print("n (en %) = (E utile/E absorbee)*100")
            print("")
        elif op == 4:
            print("")
            print("- Fréquence :")
            print("f = 1/t")
            print("t en sec")
            print("")
        elif op == 5:
            print("")
            print("- Valeur efficace :")
            print("Ueff = Umax/racine(2)")
            print("t en sec")
            print("")
        elif op == 6:
            print("")
            print("- Valeur moyenne tension :")
            print("<u(t)> = ((Aire+)-(Aire-))/t")
            print("t en sec")
            print("")
        elif op == 7:
            print("")
            print("- Position voltemètres :")
            print("AC = valeur moyenne null (continu)")
            print("AC/DC = valeur moyenne non null (alternatif)")
            print("")
        elif op == 8:
            print("")
            print("- Tension sinusoidale u(t) :")
            print("u(t) = Ueff x racine(2) x sin(w x t)")
            print("x (en rad s^-1) = 2pi x f")
            print("")
        else:
            print("")
            print("erreur type de formule non trouvés")
            print("")
    elif option == "2":
        print("")
        print("Infos :")
        print(" - Nom : Physique")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
        print(" - Contribuer / source  : https://github.com/alanbedrine/PyTools")
        print("")
    elif option == "3":
        print("")
        print("Fin du programme")
        break