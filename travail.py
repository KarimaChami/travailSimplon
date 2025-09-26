from fonctions import *
filter_fonction()
affichage_fonction()
sort_fonction()
tuple_fonction()
List_function()
max_fonction()
min_fonction()
bonus_fonction()

while True:
    print("1-Afficher la liste des produits")
    print("2-Rechercher un produit")
    print("3-Ajouter un produit")
    print("4-Quetter le programme")
    choix = int((input("vous pouvez choisir une option de 1 a 4")))
    if choix == 1 :
      List_function()
    elif choix == 2 :
        find_produit = input("saisi le nom du produit")
        index = list(filter(lambda x:x[0]==find_produit,combiner))
        print("produit n'existe pas")
    elif choix == 3 :
     add_produit = input("saisi le nom du produit a ajouter")
     add_produit = input("saisi son prix ")

    elif choix == 4 :
        print("vous avez quitter !")
        break
    else:
        print("Option invalide !!")
