   ### **1. Solutions pour les Listes**

#### **Exercice 1 : Compter les occurrences dans une liste**
```python
# Solution
nombres = [4, 2, 7, 4, 2, 4, 9]
valeur = 4

# Compte les occurrences de la valeur
occurrences = nombres.count(valeur)
print(f"La valeur {valeur} apparaît {occurrences} fois.")
```

#### **Exercice 2 : Trier une liste**
```python
# Solution
nombres = [9, 2, 4, 7, 1, 8]
nombres_triés = sorted(nombres)
print("Liste triée :", nombres_triés)
```

#### **Exercice 3 : Suppression des doublons**
```python
# Solution
nombres = [4, 2, 7, 4, 2, 9]
nombres_sans_doublons = list(set(nombres))
print("Liste sans doublons :", nombres_sans_doublons)
```

#### **Exercice 4 : Fusionner deux listes sans doublons**
```python
# Solution
liste1 = [1, 2, 3]
liste2 = [3, 4, 5]
fusion_sans_doublons = list(set(liste1 + liste2))
print("Fusion des listes :", fusion_sans_doublons)
```

---

### **2. Solutions pour les Tuples**

#### **Exercice 1 : Accéder aux éléments d’un tuple**
```python
# Solution
tuple_exemple = (10, 20, 30, 40)
print("Premier élément :", tuple_exemple[0])
print("Dernier élément :", tuple_exemple[-1])
```

#### **Exercice 2 : Conversion tuple <-> liste**
```python
# Solution
tuple_exemple = (1, 2, 3, 4)
liste = list(tuple_exemple)  # Conversion en liste
liste.append(5)
nouveau_tuple = tuple(liste)  # Conversion en tuple
print("Nouveau tuple :", nouveau_tuple)
```

#### **Exercice 3 : Compter les éléments d’un tuple**
```python
# Solution
tuple_exemple = (1, 2, 3, 1, 4, 1)
nombre_occurrences = tuple_exemple.count(1)
print("Le nombre 1 apparaît", nombre_occurrences, "fois.")
```

---

### **3. Solutions pour les Dictionnaires**

#### **Exercice 1 : Rechercher une clé dans un dictionnaire**
```python
# Solution
mon_dictionnaire = {"nom": "Alice", "âge": 25, "ville": "Paris"}
clé = "âge"
if clé in mon_dictionnaire:
    print(f"La clé '{clé}' existe avec la valeur :", mon_dictionnaire[clé])
else:
    print(f"La clé '{clé}' n'existe pas.")
```

#### **Exercice 2 : Fusionner deux dictionnaires**
```python
# Solution
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
fusion_dictionnaires = {**dict1, **dict2}  # dict2 écrase les clés existantes
print("Dictionnaire fusionné :", fusion_dictionnaires)
```

#### **Exercice 3 : Trier un dictionnaire par clé**
```python
# Solution
mon_dictionnaire = {"z": 3, "a": 1, "c": 2}
dictionnaire_tri = dict(sorted(mon_dictionnaire.items()))
print("Dictionnaire trié :", dictionnaire_tri)
```

---

### **4. Solutions pour les Ensembles**

#### **Exercice 1 : Opérations ensemblistes**
```python
# Solution
ensemble1 = {1, 2, 3}
ensemble2 = {3, 4, 5}

# Union
union = ensemble1 | ensemble2
print("Union :", union)

# Intersection
intersection = ensemble1 & ensemble2
print("Intersection :", intersection)

# Différence
difference = ensemble1 - ensemble2
print("Différence :", difference)
```

#### **Exercice 2 : Vérifier une inclusion**
```python
# Solution
ensemble1 = {1, 2, 3}
ensemble2 = {1, 2}
print("ensemble2 est un sous-ensemble de ensemble1 :", ensemble2.issubset(ensemble1))
```

#### **Exercice 3 : Éliminer les doublons d’une liste**
```python
# Solution
liste = [1, 2, 2, 3, 4, 4, 5]
ensemble_sans_doublons = set(liste)
print("Liste sans doublons :", list(ensemble_sans_doublons))
```

---

### **5. Exercices combinatoires sur les collections**

#### **Exercice 1 : Trouver les éléments communs entre deux collections**
```python
# Solution
liste1 = [1, 2, 3, 4]
liste2 = [3, 4, 5, 6]
intersection = list(set(liste1) & set(liste2))
print("Éléments communs :", intersection)
```

#### **Exercice 2 : Compter la fréquence des éléments dans une liste**
```python
# Solution
liste = [1, 2, 2, 3, 4, 4, 4, 5]
fréquence = {}
for element in liste:
    fréquence[element] = fréquence.get(element, 0) + 1
print("Fréquence des éléments :", fréquence)
```

#### **Exercice 3 : Regrouper des données avec un dictionnaire**
```python
# Solution
données = [("Alice", "Maths"), ("Bob", "Physique"), ("Alice", "Physique")]
groupement = {}
for nom, matière in données:
    groupement.setdefault(nom, []).append(matière)
print("Données regroupées :", groupement)
```

#### **Exercice 4 : Trier un dictionnaire par valeurs**
```python
# Solution
mon_dictionnaire = {"Alice": 25, "Bob": 22, "Charlie": 30}
dictionnaire_tri_par_valeur = dict(sorted(mon_dictionnaire.items(), key=lambda x: x[1]))
print("Dictionnaire trié par valeurs :", dictionnaire_tri_par_valeur)
```
