# Solutions des exercices sur les collections Python

## Solutions des exercices combinatoires

### 1. Conversion entre collections
```python
liste = [1, 2, 3, 4, 5, 6]

# Conversion en tuple
tuple_converti = tuple(liste)
print("Tuple:", tuple_converti)

# Conversion en ensemble
ensemble_converti = set(liste)
print("Ensemble:", ensemble_converti)

# Conversion en dictionnaire (clé : élément, valeur : carré)
dictionnaire_converti = {x: x**2 for x in liste}
print("Dictionnaire:", dictionnaire_converti)
```

### 2. Comparaison entre deux collections
```python
liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7, 8]

# Conversion en ensembles
ensemble1 = set(liste1)
ensemble2 = set(liste2)

# Opérations sur les ensembles
elements_communs = ensemble1.intersection(ensemble2)
elements_uniques_liste1 = ensemble1.difference(ensemble2)
union_ensembles = ensemble1.union(ensemble2)

# Résultats
print("Éléments communs:", elements_communs)
print("Éléments uniques à liste1:", elements_uniques_liste1)
print("Union des ensembles:", sorted(union_ensembles))
```

### 3. Extraction et regroupement des données
```python
etudiants = {
    "Alice": 18,
    "Bob": 15,
    "Charlie": 20,
    "Diana": 12
}

# Étudiants admis
admis = [nom for nom, note in etudiants.items() if note >= 15]
print("Étudiants admis:", admis)

# Regroupement des étudiants
regroupement = {
    "Admis": {nom: note for nom, note in etudiants.items() if note >= 15},
    "Ajourné": {nom: note for nom, note in etudiants.items() if note < 15}
}
print("Regroupement:", regroupement)
```

### 4. Création d’une matrice imbriquée
```python
temperatures = {
    "Lundi": [12, 15, 14],
    "Mardi": [14, 16, 13],
    "Mercredi": [11, 13, 10],
}

# Moyennes des températures
moyennes = {jour: sum(temp) / len(temp) for jour, temp in temperatures.items()}
print("Moyennes des températures:", moyennes)

# Liste des tuples
temp_tuples = [(jour, temp) for jour, temp in temperatures.items()]
print("Liste des tuples:", temp_tuples)

# Jour avec la température moyenne la plus élevée
jour_max = max(moyennes, key=moyennes.get)
print("Jour avec la température moyenne la plus élevée:", jour_max)
```

### 5. Filtrage et compréhension
```python
produits = [
    ("Pomme", 100),
    ("Banane", 150),
    ("Cerise", 50),
    ("Orange", 200)
]

# Filtrage des produits coûtant moins de 100
produits_filtrés = [produit for produit in produits if produit[1] < 100]
print("Produits filtrés:", produits_filtrés)

# Conversion en dictionnaire
produits_dictionnaire = {nom: prix for nom, prix in produits_filtrés}
print("Dictionnaire des produits filtrés:", produits_dictionnaire)

# Produit le plus cher
produit_max = max(produits, key=lambda x: x[1])
print("Produit le plus cher:", produit_max)
```

---

## Solutions des exercices sur les méthodes des collections

### 6. Méthodes des listes
```python
liste = [5, 3, 8, 6, 2, 10, 1]

# Ajouter 12 à la fin
liste.append(12)
print("Après ajout de 12:", liste)

# Insérer 7 entre 6 et 8
liste.insert(liste.index(8), 7)
print("Après insertion de 7:", liste)

# Supprimer 3
liste.remove(3)
print("Après suppression de 3:", liste)

# Tri croissant et décroissant
liste.sort()
print("Tri croissant:", liste)

liste.sort(reverse=True)
print("Tri décroissant:", liste)
```

### 7. Méthodes des ensembles
```python
A = {2, 4, 6, 8, 10}
B = {1, 3, 6, 9, 10}

# Opérations sur les ensembles
union = A.union(B)
intersection = A.intersection(B)
difference = A.difference(B)
symmetric_difference = A.symmetric_difference(B)

print("Union:", union)
print("Intersection:", intersection)
print("Différence:", difference)
print("Différence symétrique:", symmetric_difference)

# Ajout et suppression
def ajouter_supprimer(ensemble):
    ensemble.add(12)
    print("Après ajout de 12:", ensemble)
    ensemble.discard(9)
    print("Après suppression de 9:", ensemble)

ajouter_supprimer(B)
```

### 8. Méthodes des dictionnaires
```python
voiture = {
    "marque": "Toyota",
    "modele": "Corolla",
    "annee": 2020,
    "prix": 20000
}

# Clés et valeurs
print("Clés:", voiture.keys())
print("Valeurs:", voiture.values())

# Modification
voiture["prix"] *= 0.9
print("Prix après réduction:", voiture["prix"])

# Suppression
del voiture["annee"]
print("Dictionnaire après suppression:", voiture)
```

### 9. Combinaison des méthodes
```python
stock = {
    "Pomme": 50,
    "Banane": 30,
    "Cerise": 20
}

# Clés triées
cles_tries = sorted(stock.keys())
print("Clés triées:", cles_tries)

# Augmentation des quantités
for produit in stock:
    stock[produit] += 10
print("Stock mis à jour:", stock)

# Produit avec la plus grande quantité
produit_max = max(stock.items(), key=lambda x: x[1])
print("Produit avec la plus grande quantité:", produit_max)
