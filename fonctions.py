from db import produits,prix
#Qst1
def List_function():
  combiner = list(zip(produits,prix))
  print(combiner)

#Qst2
def filter_fonction():
 filtrer = list(filter(lambda x:x >=30,prix))
 print(filtrer) 


# #Qst3
def affichage_fonction():
 chaine = ""
 for p,pr in combiner :
   chaine += f"{p} coute {pr} DH\n"
 print(chaine)

# #Qst4
def sort_fonction():
    combiner.sort(key=lambda x:x[1])
    print(combiner) 

# #Qst6
def tuple_fonction():
    print (tuple(combiner))


# #Qst7
def max_fonction():
  combiner.sort(key=lambda x:x[1],reverse=True)
  print(f"Le produit le plus cher{combiner[0]}")


def min_fonction():
  combiner.sort(key=lambda x:x[1])
  print(f"Le produit le moins cher{combiner[0]}")

  
#Qst8
def bonus_fonction():
 produit_luxe = list(map(lambda x: f"{x[0]} cout {x[1]} DH(LUXE)" 
                         if x[1] > 1000 
                         else f"{x[0]} coute {x[1]} DH",combiner))
 print(produit_luxe)

