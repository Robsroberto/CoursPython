couleurs = ("rouge", "vert", "bleu", "rouge","vert")


# print(couleurs[4])
print(couleurs.index("vert"))
print(couleurs.count("rouge"))

list_couleur  =  list(couleurs) # tuple pour convertir en tuple
print(couleurs)
print(list_couleur)


# Les ensembles  set
nombres = {1, 2, 3, 1}
print(nombres)
# ajout
nombres.add(10)
print(nombres)
#supprimer
nombres.remove(1)
print(nombres)
nombres.discard(1)
# Extrait
N = nombres.pop()
print(nombres)
print(N)

import random
A = set()
B = set()
for _ in range(10):
    A.add(random.randint(1,100))
    B.add(random.randint(1,100))
print(A)
print(B)

print(f"Union {A.union(B)}")
print(f"Intersection {A.intersection(B)}")
print(f"Différence {A.difference(B)}")
print(f"Différence {B.difference(A)}")
