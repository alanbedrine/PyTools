from math import *

versionprog = "7.0"
majdate = "16/12/2019"

print("")
print("SES version ", versionprog)
print("")

while 1:

    print("")
    option = input("continuer (1) / infos (2) / quitter (3) : ")
    print("")

    if option == "1":
        print("")
        print("Type de formule à calculer :")
        print(" - Varation de l'evolution (1)")
        print(" - Pourcentage de répartition (2)")
        print(" - CA (Chiffre d'Affaire) (3)")
        print(" - VA (Valeurs Ajoutées) (4)")
        print(" - Bénéfice (5)")
        print("")

        print("")
        op = float(input("Qu'elle formule voulez vous calculez ? : "))
        print("")

        if op == 1:
            print("")
            print("- Pourcentage de variation :")
            print("((varfinal - varinitial )/varinitial)*100")
            print("")
        elif op == 2:
            print("")
            print("- Pourcentage de répartition :")
            print("valeurinitial * 100 / valeur total")
            print("")
        elif op == 3:
            print("")
            print("- CA (Chiffre d'Affaire) :")
            print("CA = p x Q")
            print("CA = prix x Quantité")
            print("")
        elif op == 4:
            print("")
            print("- VA (Valeurs Ajoutées) :")
            print("VA = CA - CI")
            print("VA = Chiffre d'Affaire - Cosnomation Intérmédiaire")
            print("")
        elif op == 5:
            print("")
            print("- Bénéfice :")
            print("Bénéfice = VA - Cout du travail")
            print("Bénéfice = Valeurs Ajoutées - Cout du travail")
            print("")
        else:
            print("")
            print("erreur type de formule non trouvés")
            print("")
    elif option == "2":
        print("")
        print("Infos :")
        print(" - Nom : SES")
        print(" - Auteur : Alan Bédrine")
        print(" - Version du programme :", versionprog)
        print(" - Dernière mise a jour :", majdate)
        print("")
    elif option == "3":
        print("")
        print("Fin du programme")
        break