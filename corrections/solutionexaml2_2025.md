##   **EXERCICE 1 – Structures conditionnelles** (6 points)

### **1.1 Classification par âge**

```python
age = int(input("Entrez votre âge : "))

if age < 18:
    print("Mineur")
elif age <= 60:
    print("Majeur")
else:
    print("Senior")
```

**Explication :**

* On transforme l'entrée en entier (`int`).
* Si âge < 18 → Mineur.
* Si entre 18 et 60 inclus → Majeur.
* Sinon (donc > 60) → Senior.

---

### **1.2 Trouver le plus grand de 3 nombres (sans max)**

```python
a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))
c = int(input("Entrez le troisième nombre : "))

plus_grand = a

if b > plus_grand:
    plus_grand = b
if c > plus_grand:
    plus_grand = c

print("Le plus grand est :", plus_grand)
```

---

### **1.3 Vérification d’année bissextile**

```python
annee = int(input("Entrez une année : "))

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("Année bissextile")
else:
    print("Année non bissextile")
```

---

##   **EXERCICE 2 – Boucles et listes** (6 points)

### **2.1 Moyenne des 5 notes**

```python
notes = []

for i in range(5):
    note = float(input(f"Note {i+1} : "))
    notes.append(note)

moyenne = sum(notes) / len(notes)

print("Moyenne :", moyenne)

if moyenne >= 10:
    print("Validé")
else:
    print("Ajourné")
```

---

### **2.2 Affichage des impairs jusqu’à un multiple de 7**

```python
for i in range(1, 51):
    if i % 2 != 0:
        if i % 7 == 0:
            break
        print(i)
```

**Explication :**

* On boucle de 1 à 50.
* On vérifie si le nombre est impair (`% 2 != 0`).
* Si c’est un multiple de 7, on quitte avec `break`.

---

##   **EXERCICE 3 – Fonctions et tuples** (6 points)

### **3.1 Fonction `analyse_tuple`**

```python
def analyse_tuple(t):
    print("Longueur :", len(t))
    print("Somme :", sum(t))
    print("Max :", max(t))

# Test
analyse_tuple((3, 8, 1, 14, 6))
```

---

### **3.2 Fonction `contient(valeur, liste)` sans `in`**

```python
def contient(valeur, liste):
    for elt in liste:
        if elt == valeur:
            return True
    return False

# Test
print(contient(5, [1, 2, 3, 4, 5]))  # True
print(contient(9, [1, 2, 3]))        # False
```

---

##   **EXERCICE 4 – Dictionnaires** (6 points)

```python
etudiants = {
    "Ali": 12.5,
    "Fatou": 8.5,
    "Samba": 15.0,
    "Maimouna": 17.5,
    "Ousmane": 9.0
}

# 1. Afficher les étudiants validés
print("Étudiants validés :")
for nom, note in etudiants.items():
    if note >= 10:
        print(nom)

# 2. Moyenne générale
somme = sum(etudiants.values())
moyenne = somme / len(etudiants)
print("Moyenne générale :", moyenne)

# 3. Ajouter Awa
etudiants["Awa"] = 13.5
print("Étudiant ajouté :", etudiants)
```
