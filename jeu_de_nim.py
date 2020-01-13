# Faire le jeu des 3 batons, entre humain et machine
# Règle, chaque joueur retire à son tour 3, 2 ou 1 baton. Celui qui prend le dernier baton à perdu

##La machine doit apprendre : 
##	Si elle perd retirer chaque billes qu'elle à joué de chacun de ses tableaux
##	Si elle gagne ajouter une bille qu'elle a joué à chacune de ses tableaux

##Creer un graphe de son avancement de ses victoires/défaites


import random
import dessin

blue = 3
red = 5
green = 7

machine_tour = False
humain_tour = False

jouer = True

begin = str(input("Qui commence ? - Veux tu commencer ? y/n : "))
if begin == 'y':
    humain_tour = True
else:
    machine_tour = True

while jouer:
    baton = 11
    dessin.dessin(baton)

    # Jeu
    while baton >= 1:
        if machine_tour:
            #       box_$baton = [blue, red, green]
            #       bill_$baton = random.box_baton
            nbbaton = random.randrange(1, 4)
            print("La machine prend : ", nbbaton)
            baton -= nbbaton
        if humain_tour:
            nbbaton = int(input("Tu prends : "))
            baton -= nbbaton

        if baton < 1:
            if machine_tour:
                machine_victoire = 0
                print("\n\n##################\n  Machine loose !\n##################")
            if humain_tour:
                machine_victoire = 1
                print("\n\n##################\n  Machine win !\n##################")
        else:
            dessin.dessin(baton)
            machine_tour = not machine_tour
            humain_tour = not humain_tour

    # if machine_victoire == 0
    # 	you loose
    # 		foreach tour[x]
    # 			bill_$x--
    #
    # if machine_victoire == 1
    # 	you win
    # 		foreach tour[x]
    # 			bill_$x++

    # Nouvelle partie ?
    again = str(input("Autre partie ? (y/n) --> "))
    if again == 'n':
        jouer = False
    else:
        clear = "\n" * 10
        print(clear)
