# Exercices et Projet de Recherche : Tuples et Sets en Python


## **Partie I : Exercices sur les Tuples (7 exercices)**

### **Exercice 1 : Découverte de l'immuabilité**
**Objectif :** Comprendre la différence fondamentale entre listes et tuples.

**Énoncé :** Créez un tuple `coordonnees = (10, 20)` représentant un point sur un plan. Affichez les coordonnées, puis essayez de modifier la première valeur. Observez et expliquez l'erreur.

**Correction :**
```python
coordonnees = (10, 20)
print(f"Point : x={coordonnees[0]}, y={coordonnees[1]}")

# Tentative de modification (génère une erreur)
# coordonnees[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Explication : Les tuples sont immuables, contrairement aux listes
# Cela garantit que les données ne peuvent pas être modifiées accidentellement
```

### **Exercice 2 : Méthodes spécifiques des tuples**
**Objectif :** Maîtriser `count()` et `index()`.

**Énoncé :** Soit le tuple `temperatures = (22, 25, 22, 28, 22, 30, 25)` représentant les températures d'une semaine.
1. Combien de fois la température 22°C apparaît-elle ?
2. À quelle position se trouve la première occurrence de 28°C ?
3. Quelle est la température du mercredi (indice 2) ?

**Correction :**
```python
temperatures = (22, 25, 22, 28, 22, 30, 25)

# 1. Comptage des occurrences
nb_22 = temperatures.count(22)
print(f"La température 22°C apparaît {nb_22} fois")  # 3 fois

# 2. Position de la première occurrence
pos_28 = temperatures.index(28)
print(f"28°C se trouve à l'indice {pos_28}")  # indice 3

# 3. Température du mercredi
temp_mercredi = temperatures[2]
print(f"Mercredi : {temp_mercredi}°C")  # 22°C
```

### **Exercice 3 : Unpacking (déballage) de tuples**
**Objectif :** Utiliser l'unpacking pour extraire les valeurs.

**Énoncé :** Créez un tuple `etudiant = ("Marie", 20, "Informatique")`. Utilisez l'unpacking pour extraire ces informations dans trois variables distinctes, puis affichez une phrase complète.

**Correction :**
```python
etudiant = ("Marie", 20, "Informatique")

# Unpacking en une seule ligne
nom, age, filiere = etudiant

print(f"{nom} a {age} ans et étudie en {filiere}")
# Sortie : Marie a 20 ans et étudie en Informatique
```

### **Exercice 4 : Calcul avec coordonnées 3D**
**Objectif :** Appliquer les tuples à des calculs mathématiques.

**Énoncé :** Créez un tuple `point = (3, 4, 5)` représentant un point en 3D. Calculez sa distance par rapport à l'origine en utilisant la formule : $$\text{distance} = \sqrt{x^2 + y^2 + z^2}$$

**Correction :**
```python
import math

point = (3, 4, 5)
x, y, z = point

distance = math.sqrt(x**2 + y**2 + z**2)
print(f"Point : ({x}, {y}, {z})")
print(f"Distance à l'origine : {distance:.2f}")  # 7.07
```

### **Exercice 5 : Tuple de tuples (structures imbriquées)**
**Objectif :** Manipuler des structures de données complexes.

**Énoncé :** Créez un tuple représentant trois étudiants avec leurs notes :
```python
classe = (
    ("Alice", 15, 18),
    ("Bob", 12, 14),
    ("Charlie", 16, 19)
)
```
Calculez et affichez la moyenne de chaque étudiant.

**Correction :**
```python
classe = (
    ("Alice", 15, 18),
    ("Bob", 12, 14),
    ("Charlie", 16, 19)
)

for nom, note1, note2 in classe:
    moyenne = (note1 + note2) / 2
    print(f"{nom} : moyenne = {moyenne}")

# Sortie :
# Alice : moyenne = 16.5
# Bob : moyenne = 13.0
# Charlie : moyenne = 17.5
```

### **Exercice 6 : Couleurs RGB avec tuples**
**Objectif :** Comprendre l'usage des tuples pour des données constantes.

**Énoncé :** Définissez trois couleurs sous forme de tuples RGB : rouge `(255, 0, 0)`, vert `(0, 255, 0)`, bleu `(0, 0, 255)`. Créez une fonction qui affiche les composantes d'une couleur.

**Correction :**
```python
# Définition des couleurs (constantes)
rouge = (255, 0, 0)
vert = (0, 255, 0)
bleu = (0, 0, 255)

def afficher_couleur(couleur, nom):
    r, g, b = couleur
    print(f"{nom} : Rouge={r}, Vert={g}, Bleu={b}")

afficher_couleur(rouge, "Rouge")
afficher_couleur(vert, "Vert")
afficher_couleur(bleu, "Bleu")
```

### **Exercice 7 : Conversion et sécurisation de données**
**Objectif :** Comprendre quand convertir une liste en tuple.

**Énoncé :** Vous avez une liste de configuration système `config = ["localhost", 8080, True]`. Une fois la configuration validée, elle ne doit plus être modifiée. Convertissez-la en tuple et vérifiez l'immuabilité.

**Correction :**
```python
# Configuration initiale (modifiable)
config_liste = ["localhost", 8080, True]
print(f"Configuration initiale : {config_liste}")

# Validation et sécurisation
config_finale = tuple(config_liste)
print(f"Configuration sécurisée : {config_finale}")
print(f"Type : {type(config_finale)}")

# Vérification de l'immuabilité
# config_finale[1] = 9000  # Génère une erreur
```

---

## **Partie II : Exercices sur les Sets (7 exercices)**

### **Exercice 8 : Suppression automatique des doublons**
**Objectif :** Comprendre la propriété d'unicité des sets.

**Énoncé :** Une liste d'emails contient des doublons dus à des erreurs de saisie : `emails = ["alice@mail.com", "bob@mail.com", "alice@mail.com", "charlie@mail.com", "bob@mail.com"]`. Créez un set pour obtenir la liste unique.

**Correction :**
```python
emails = ["alice@mail.com", "bob@mail.com", "alice@mail.com", "charlie@mail.com", "bob@mail.com"]

# Suppression automatique des doublons
emails_uniques = set(emails)
print(f"Emails uniques : {emails_uniques}")
print(f"Nombre d'emails uniques : {len(emails_uniques)}")  # 3

# Reconversion en liste si nécessaire
liste_finale = list(emails_uniques)
```

### **Exercice 9 : Opérations d'ajout et de suppression**
**Objectif :** Maîtriser `add()`, `remove()`, et `discard()`.

**Énoncé :** Créez un set vide `participants`. Ajoutez "Alice", "Bob", "Charlie". Supprimez "Bob". Essayez de supprimer "David" avec `remove()` puis avec `discard()`. Observez la différence.

**Correction :**
```python
participants = set()

# Ajouts
participants.add("Alice")
participants.add("Bob")
participants.add("Charlie")
print(f"Participants : {participants}")

# Suppression existante
participants.remove("Bob")
print(f"Après suppression de Bob : {participants}")

# Tentative de suppression inexistante
# participants.remove("David")  # Génère KeyError
participants.discard("David")   # Ne génère pas d'erreur
print(f"Après discard de David : {participants}")
```

### **Exercice 10 : Intersection - éléments communs**
**Objectif :** Trouver les éléments partagés entre deux ensembles.

**Énoncé :** Le groupe A suit les cours `{"Python", "Java", "SQL"}`. Le groupe B suit `{"Python", "C++", "SQL", "JavaScript"}`. Quels cours sont suivis par les deux groupes ?

**Correction :**
```python
groupe_a = {"Python", "Java", "SQL"}
groupe_b = {"Python", "C++", "SQL", "JavaScript"}

# Intersection
cours_communs = groupe_a.intersection(groupe_b)
print(f"Cours suivis par les deux groupes : {cours_communs}")  # {'Python', 'SQL'}

# Méthode alternative avec l'opérateur &
cours_communs_alt = groupe_a & groupe_b
print(f"Vérification : {cours_communs_alt}")
```

### **Exercice 11 : Union - fusion de données**
**Objectif :** Combiner plusieurs ensembles de données.

**Énoncé :** Vous gérez deux bases de données clients. Base 1 : `{101, 102, 103}`, Base 2 : `{103, 104, 105}`. Créez une base globale contenant tous les clients uniques.

**Correction :**
```python
base1 = {101, 102, 103}
base2 = {103, 104, 105}

# Union
base_globale = base1.union(base2)
print(f"Base globale : {base_globale}")  # {101, 102, 103, 104, 105}

# Méthode alternative avec l'opérateur |
base_globale_alt = base1 | base2
print(f"Vérification : {base_globale_alt}")
```

### **Exercice 12 : Différence - éléments exclusifs**
**Objectif :** Identifier les éléments présents dans un set mais pas dans l'autre.

**Énoncé :** Les étudiants inscrits sont `inscrits = {"Alice", "Bob", "Charlie", "David"}`. Les présents aujourd'hui sont `presents = {"Alice", "Charlie"}`. Qui est absent ?

**Correction :**
```python
inscrits = {"Alice", "Bob", "Charlie", "David"}
presents = {"Alice", "Charlie"}

# Différence
absents = inscrits.difference(presents)
print(f"Étudiants absents : {absents}")  # {'Bob', 'David'}

# Méthode alternative
absents_alt = inscrits - presents
print(f"Vérification : {absents_alt}")
```

### **Exercice 13 : Test d'appartenance rapide**
**Objectif :** Utiliser les sets pour des vérifications efficaces.

**Énoncé :** Créez un set de mots-clés Python : `{"if", "else", "for", "while", "def", "class", "return", "import"}`. Demandez à l'utilisateur un mot et vérifiez s'il s'agit d'un mot-clé.

**Correction :**
```python
mots_cles = {"if", "else", "for", "while", "def", "class", "return", "import"}

mot = input("Entrez un mot : ")

if mot in mots_cles:
    print(f"'{mot}' est un mot-clé Python")
else:
    print(f"'{mot}' n'est pas un mot-clé Python")

# Les tests d'appartenance dans un set sont très rapides (O(1))
```

### **Exercice 14 : Combinaison tuples et sets**
**Objectif :** Utiliser les deux structures ensemble.

**Énoncé :** Vous avez un tuple de notes d'examen : `notes = (15, 12, 18, 12, 15, 20, 18, 15)`. Créez un rapport montrant chaque note unique avec son nombre d'occurrences.

**Correction :**
```python
notes = (15, 12, 18, 12, 15, 20, 18, 15)

# Obtenir les notes uniques
notes_uniques = set(notes)
print(f"Notes uniques : {notes_uniques}")

# Créer un rapport
print("\n--- Rapport des notes ---")
for note in sorted(notes_uniques):
    occurrences = notes.count(note)
    print(f"Note {note} : {occurrences} occurrence(s)")
```

---

## **Partie III : Projets de Recherche Graphique**

### **Projet 1 : Constellation Interactive (Turtle) - Niveau Débutant**

**Objectif :** Créer une constellation d'étoiles en utilisant des tuples pour les coordonnées.

**Consigne de recherche :**
> **Mission :** Créez votre propre constellation !
> 
> 1. **Recherchez** comment utiliser le module `turtle` :
>    - `turtle.goto(x, y)` pour se déplacer
>    - `turtle.dot()` pour dessiner un point
>    - `turtle.color()` pour changer la couleur
> 
> 2. **Implémentez :**
>    - Une liste de tuples représentant les positions des étoiles
>    - Un parcours de cette liste pour dessiner chaque étoile
>    - Bonus : reliez certaines étoiles par des lignes
> 
> 3. **Exemple de structure :**
> ```python
> etoiles = [(0, 0), (50, 50), (100, 0), (50, -50)]
> # Votre code ici pour dessiner ces points
> ```

**Pourquoi ce projet ?** Il illustre parfaitement l'usage des tuples pour des coordonnées fixes et permet une visualisation immédiate des concepts.

### **Projet 2 : Générateur de Palettes de Couleurs (Tkinter) - Niveau Intermédiaire**

**Objectif :** Créer une interface graphique pour explorer des palettes de couleurs stockées dans des tuples.

**Consigne de recherche :**
> **Mission :** Créez un sélecteur de couleurs moderne !
> 
> 1. **Recherchez** `tkinter` :
>    - Création d'une fenêtre avec `Tk()`
>    - Ajout de boutons avec `Button()`
>    - Changement de couleur de fond
> 
> 2. **Implémentez :**
>    - Une liste de tuples RGB : `couleurs = [(255,0,0), (0,255,0), (0,0,255)]`
>    - Des boutons pour chaque couleur
>    - Changement de la couleur de fond au clic
> 
> 3. **Défi bonus :** Affichez le code hexadécimal de la couleur sélectionnée

**Pourquoi ce projet ?** Il montre l'usage pratique des tuples pour des données structurées (couleurs RGB) et introduit les interfaces graphiques.

### **Projet 3 : Analyseur de Texte Visuel (Tkinter + Sets) - Niveau Avancé**

**Objectif :** Créer un outil d'analyse de texte utilisant les sets pour les calculs.

**Consigne de recherche :**
> **Mission :** Créez un analyseur de texte intelligent !
> 
> 1. **Fonctionnalités à rechercher :**
>    - Zone de texte avec `Text()` widget
>    - Boutons d'analyse
>    - Affichage de résultats
> 
> 2. **Analyses à implémenter :**
>    - Nombre de mots uniques (avec un set)
>    - Lettres utilisées (set de caractères)
>    - Mots les plus fréquents
> 
> 3. **Structure suggérée :**
> ```python
> texte = "votre texte ici"
> mots_uniques = set(texte.split())
> lettres_uniques = set(texte.lower())
> ```

**Pourquoi ce projet ?** Il combine l'utilisation pratique des sets (unicité, rapidité) avec une interface utilisateur utile.

---

## **Conseils pour la Présentation en Cours**

**Pour maximiser l'engagement de vos étudiants L1 en 2026 :**

1. **Commencez par les projets** - Montrez d'abord ce qu'ils vont créer pour susciter l'intérêt
2. **Liez chaque exercice à un cas concret** - Évitez les exemples abstraits
3. **Encouragez l'expérimentation** - Laissez-les modifier les paramètres et observer les résultats
4. **Créez une émulation** - Organisez une mini-compétition sur les projets graphiques


