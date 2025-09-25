from db import produits,prix
#Qst1
combiner = list(zip(produits,prix))
print(combiner)
#Qst2
def filter_fonction():
 filtrer = list(filter(lambda x:x >=30,prix))
 return filtrer
print(filter_fonction())

# #Qst3
def affichage_fonction():
 chaine = ""
 for p,pr in combiner :
   chaine += f"{p} coute {pr} DH\n"
 return chaine
print(affichage_fonction())

#Qst4
def sort_fonction():
    combiner.sort(key=lambda x:x[1])
    return combiner
print(sort_fonction())

#Qst6
def tuple_fonction():
    return tuple(combiner)
    print (tuple)
tuple_fonction()

#Qst7
def max_fonction():
  combiner.sort(key=lambda x:x[1],reverse=True)
  print(combiner[0])


def min_fonction():
  combiner.sort(key=lambda x:x[1])
  print(combiner[0])
min_fonction()
   