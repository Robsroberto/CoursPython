# n = int(input("Donner un entier :"))
# cpt= 0
# som=0
# for i in range(1,n+1):
#     if n % i ==0:
#         cpt+=1

# if cpt == 2:
#     print(f" {n} est premier ")
# else:
#     print(f" {n} n'est pas premier ")

# som =0
# for i in range(1,n):
#     if n % i ==0:
#         som+=i

# if som == n:
#     print(f" {n} est parfait ")
# else:
#     print(f" {n} n'est pas parfait ")

# for i in range(1,n+1):
#     if n % i == 0:
#         cpt+=1
#         som+=i
# if cpt == 2:
#     print(f" {n} est premier ")
# else:
#     print(f" {n} n'est pas premier ")
# if som - n == n:
#      print(f" {n} est parfait ")
# else:
#     print(f" {n} n'est pas parfait ")

# Ecrire un programme qui permet de remplir aléatoirement  une liste de 10 entiers
# le programme creer une liste ne contenant que les nombre paire et une autre contenant uniquement les multiples de 3
import random


# list_ent = []

# for i in range(10):
#     m = random.randint(1,100)
#     list_ent.append(m)
# print(list_ent)
# list_ent_pair=[]
# list_ent_mult3=[]

# for ent in list_ent:
#     if ent % 2 == 0:
#         list_ent_pair.append(ent)
#     if ent % 3 == 0:
#         list_ent_mult3.append(ent)

# print(f"Liste de nombres paires : {list_ent_pair}")
# print(f"Liste de multiple de 3  : {list_ent_mult3}")

list_ent = [random.randint(1,100) for _ in range(10)]
print(list_ent)
list_ent_pair = [val for val in list_ent if val % 2 ==0]
list_ent_mult3 = [val for val in list_ent if val % 3 ==0]
print(list_ent_pair)
print(list_ent_mult3)