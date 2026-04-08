# Exercices Progressifs — Les Dictionnaires en Python
### De la decouverte a la maitrise

---

> **Niveau** : Debutant ayant les bases (variables, listes, boucles, fonctions)
> **Objectif** : Comprendre et maitriser les dictionnaires Python par la pratique
> **Consigne generale** : Essayez chaque exercice avant de consulter la correction.

---

## Rappel syntaxique rapide

```python
# Creer un dictionnaire
etudiant = {"nom": "Alice", "age": 20, "note": 15}

# Acceder a une valeur
print(etudiant["nom"])          # Alice
print(etudiant.get("age"))      # 20
print(etudiant.get("ville", "inconnue"))  # inconnue (valeur par defaut)

# Ajouter ou modifier une entree
etudiant["ville"] = "Dakar"
etudiant["note"]  = 16

# Supprimer une entree
del etudiant["ville"]
note = etudiant.pop("note")     # Supprime et retourne la valeur

# Parcourir un dictionnaire
for cle, valeur in etudiant.items():
    print(cle, "->", valeur)

# Verifier si une cle existe
if "nom" in etudiant:
    print("La cle 'nom' existe")

# Nombre d'entrees
print(len(etudiant))
```

---

# NIVEAU 1 — Decouverte
## Lire, ecrire et parcourir un dictionnaire

---

### Exercice 1.1 — Creer et afficher un profil

Creez un dictionnaire `personne` contenant les informations suivantes :
- Nom : "Moussa"
- Prenom : "Diallo"
- Age : 22
- Ville : "Dakar"
- Etudiant : True

Puis affichez chaque information sous cette forme :
```
nom      : Moussa
prenom   : Diallo
age      : 22
ville    : Dakar
etudiant : True
```

---

**Correction 1.1**

```python
personne = {
    "nom":      "Moussa",
    "prenom":   "Diallo",
    "age":      22,
    "ville":    "Dakar",
    "etudiant": True
}

for cle, valeur in personne.items():
    print(f"{cle:<10}: {valeur}")
```

> **Point cle** : `.items()` retourne les paires (cle, valeur) du dictionnaire.
> `{cle:<10}` aligne le texte sur 10 caracteres vers la gauche pour un affichage propre.

---

### Exercice 1.2 — Modifier et enrichir un dictionnaire

Partez du dictionnaire suivant :

```python
produit = {"nom": "Cahier", "prix": 1200, "stock": 50}
```

Effectuez ces operations dans l'ordre :
1. Augmentez le prix de 200 FCFA
2. Ajoutez une cle `"categorie"` avec la valeur `"Fourniture"`
3. Retirez 10 unites du stock
4. Ajoutez une cle `"disponible"` qui vaut `True` si le stock est superieur a 0, `False` sinon
5. Affichez le dictionnaire final

---

**Correction 1.2**

```python
produit = {"nom": "Cahier", "prix": 1200, "stock": 50}

# 1. Augmenter le prix
produit["prix"] += 200

# 2. Ajouter la categorie
produit["categorie"] = "Fourniture"

# 3. Retirer du stock
produit["stock"] -= 10

# 4. Calculer la disponibilite
produit["disponible"] = produit["stock"] > 0

# 5. Afficher
for cle, valeur in produit.items():
    print(f"{cle} : {valeur}")
```

Resultat attendu :
```
nom        : Cahier
prix       : 1400
stock      : 40
categorie  : Fourniture
disponible : True
```

---

### Exercice 1.3 — Acceder sans risque avec `.get()`

Soit le dictionnaire suivant representant une fiche eleve incomplete :

```python
eleve = {"nom": "Fatou", "note_maths": 14, "note_francais": 16}
```

Affichez les informations suivantes. Si une information est absente, affichez `"Non renseigne"` :
- nom
- note_maths
- note_anglais
- note_informatique
- classe

---

**Correction 1.3**

```python
eleve = {"nom": "Fatou", "note_maths": 14, "note_francais": 16}

champs = ["nom", "note_maths", "note_anglais", "note_informatique", "classe"]

for champ in champs:
    valeur = eleve.get(champ, "Non renseigne")
    print(f"{champ} : {valeur}")
```

Resultat attendu :
```
nom                : Fatou
note_maths         : 14
note_anglais       : Non renseigne
note_informatique  : Non renseigne
classe             : Non renseigne
```

> **Point cle** : `.get(cle, valeur_par_defaut)` ne provoque jamais de `KeyError`.
> C'est la methode a privilegier quand on n'est pas certain qu'une cle existe.

---

### Exercice 1.4 — Compter les occurrences

Soit la liste suivante representant les resultats d'un sondage :

```python
reponses = ["Oui", "Non", "Oui", "Oui", "Non", "Peut-etre",
            "Oui", "Non", "Oui", "Peut-etre", "Non", "Oui"]
```

Construisez un dictionnaire `comptage` qui associe chaque reponse a son nombre d'occurrences, puis affichez le resultat.

Resultat attendu :
```
Oui       : 6
Non       : 4
Peut-etre : 2
```

---

**Correction 1.4**

```python
reponses = ["Oui", "Non", "Oui", "Oui", "Non", "Peut-etre",
            "Oui", "Non", "Oui", "Peut-etre", "Non", "Oui"]

comptage = {}

for reponse in reponses:
    # Si la cle existe, on incremente. Sinon, on part de 0.
    comptage[reponse] = comptage.get(reponse, 0) + 1

for reponse, nombre in comptage.items():
    print(f"{reponse:<12}: {nombre}")
```

> **Point cle** : Le patron `d[cle] = d.get(cle, 0) + 1` est l'une des utilisations
> les plus classiques et les plus utiles des dictionnaires en Python.

---

### Verification — Niveau 1

- [ ] Je sais creer un dictionnaire avec des cles et des valeurs de types varies
- [ ] Je sais acceder a une valeur par sa cle avec `dict["cle"]` et `.get()`
- [ ] Je sais ajouter, modifier et supprimer des entrees
- [ ] Je sais parcourir un dictionnaire avec `.items()`
- [ ] Je sais compter des occurrences avec un dictionnaire

---

# NIVEAU 2 — Manipulation
## Filtrer, trier et transformer des donnees

---

### Exercice 2.1 — Inverser un dictionnaire

Soit le dictionnaire suivant qui associe chaque etudiant a son numero d'identifiant :

```python
identifiants = {
    "Alice":  1001,
    "Bob":    1002,
    "Clara":  1003,
    "David":  1004,
}
```

Construisez le dictionnaire inverse `par_id` qui associe chaque identifiant a son etudiant.

Puis, affichez le nom de l'etudiant ayant l'identifiant `1003` en utilisant `par_id`.

---

**Correction 2.1**

```python
identifiants = {
    "Alice":  1001,
    "Bob":    1002,
    "Clara":  1003,
    "David":  1004,
}

# Inversion : les valeurs deviennent les cles, et inversement
par_id = {id_: nom for nom, id_ in identifiants.items()}

print(par_id)
# {1001: 'Alice', 1002: 'Bob', 1003: 'Clara', 1004: 'David'}

print(par_id[1003])
# Clara
```

> **Point cle** : La comprehension de dictionnaire `{v: k for k, v in d.items()}`
> est la facon pythonique d'inverser un dictionnaire.
> Elle fonctionne a condition que les valeurs d'origine soient toutes uniques.

---

    ### Exercice 2.2 — Filtrer un dictionnaire

    Soit le catalogue de prix suivant :

    ```python
    prix = {
        "Stylo":      500,
        "Cahier":    1200,
        "Regle":      800,
        "Calculette": 8500,
        "Compas":     950,
        "Equerre":    600,
        "Rapporteur": 700,
    }
    ```

    1. Creez un dictionnaire `abordables` contenant uniquement les produits dont le prix est inferieur ou egal a 800 FCFA.
    2. Creez un dictionnaire `chers` contenant les produits dont le prix depasse 1000 FCFA.
    3. Affichez les deux dictionnaires.

---

**Correction 2.2**

```python
prix = {
    "Stylo":      500,
    "Cahier":    1200,
    "Regle":      800,
    "Calculette": 8500,
    "Compas":     950,
    "Equerre":    600,
    "Rapporteur": 700,
}

# Comprehension de dictionnaire avec condition
abordables = {produit: p for produit, p in prix.items() if p <= 800}
chers       = {produit: p for produit, p in prix.items() if p > 1000}

print("Produits abordables :")
for produit, p in abordables.items():
    print(f"  {produit} : {p} FCFA")

print("\nProduits chers :")
for produit, p in chers.items():
    print(f"  {produit} : {p} FCFA")
```

---

### Exercice 2.3 — Trier par valeur

Reprenez le dictionnaire `prix` de l'exercice precedent.

1. Affichez les produits tries par prix croissant
2. Affichez les produits tries par prix decroissant
3. Affichez uniquement le produit le moins cher et le produit le plus cher

---

**Correction 2.3**

```python
prix = {
    "Stylo": 500, "Cahier": 1200, "Regle": 800,
    "Calculette": 8500, "Compas": 950, "Equerre": 600, "Rapporteur": 700,
}

# Tri par valeur croissante
# sorted() sur .items() retourne une liste de tuples (cle, valeur)
# key=lambda item: item[1] signifie "trier selon la valeur (index 1)"
tries_asc  = sorted(prix.items(), key=lambda item: item[1])
tries_desc = sorted(prix.items(), key=lambda item: item[1], reverse=True)

print("Du moins cher au plus cher :")
for produit, p in tries_asc:
    print(f"  {produit:<12} : {p} FCFA")

print("\nDu plus cher au moins cher :")
for produit, p in tries_desc:
    print(f"  {produit:<12} : {p} FCFA")

# Moins cher et plus cher
moins_cher = min(prix, key=prix.get)
plus_cher  = max(prix, key=prix.get)
print(f"\nMoins cher : {moins_cher} ({prix[moins_cher]} FCFA)")
print(f"Plus cher  : {plus_cher} ({prix[plus_cher]} FCFA)")
```

> **Point cle** : `min(dict, key=dict.get)` retourne la **cle** dont la valeur est minimale.
> C'est une syntaxe tres utile pour trouver rapidement le minimum ou le maximum.

---

### Exercice 2.4 — Fusionner deux dictionnaires

Vous avez deux sources de donnees sur des etudiants :

```python
notes_s1 = {"Alice": 14, "Bob": 11, "Clara": 17}
notes_s2 = {"Alice": 16, "Bob": 13, "David": 15}
```

Construisez un dictionnaire `bilan` qui associe chaque etudiant a sa moyenne entre S1 et S2.
Si un etudiant n'a de notes que dans un seul semestre, sa moyenne est celle de ce semestre.

Resultat attendu :
```
Alice : 15.0
Bob   : 12.0
Clara : 17.0
David : 15.0
```

---

**Correction 2.4**

```python
notes_s1 = {"Alice": 14, "Bob": 11, "Clara": 17}
notes_s2 = {"Alice": 16, "Bob": 13, "David": 15}

# Reunir tous les noms d'etudiants (union des cles)
tous_les_etudiants = set(notes_s1.keys()) | set(notes_s2.keys())

bilan = {}
for nom in tous_les_etudiants:
    n1 = notes_s1.get(nom)   # None si absent du S1
    n2 = notes_s2.get(nom)   # None si absent du S2

    if n1 is not None and n2 is not None:
        bilan[nom] = (n1 + n2) / 2
    elif n1 is not None:
        bilan[nom] = float(n1)
    else:
        bilan[nom] = float(n2)

# Affichage trie par nom
for nom in sorted(bilan):
    print(f"{nom:<8}: {bilan[nom]}")
```

---

### Exercice 2.5 — Comprehension de dictionnaire

Transformez chaque liste en dictionnaire en une seule ligne (comprehension) :

```python
# Liste 1 : associer chaque mot a sa longueur
mots = ["python", "dictionnaire", "liste", "boucle", "fonction"]
# Resultat attendu : {"python": 6, "dictionnaire": 12, "liste": 5, ...}

# Liste 2 : associer chaque nombre a son carre
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Resultat attendu : {1: 1, 2: 4, 3: 9, 4: 16, ...}

# Liste 3 : associer chaque nombre pair a son cube (uniquement les pairs)
# Resultat attendu : {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}
```

---

**Correction 2.5**

```python
mots    = ["python", "dictionnaire", "liste", "boucle", "fonction"]
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Liste 1 : mot -> longueur
longueurs = {mot: len(mot) for mot in mots}
print(longueurs)

# Liste 2 : nombre -> carre
carres = {n: n ** 2 for n in nombres}
print(carres)

# Liste 3 : nombre pair -> cube
cubes_pairs = {n: n ** 3 for n in nombres if n % 2 == 0}
print(cubes_pairs)
```

> **Syntaxe de la comprehension** : `{cle: valeur for element in iterable if condition}`
> La condition `if` est facultative.

---

### Verification — Niveau 2

- [ ] Je sais filtrer un dictionnaire avec une comprehension et une condition
- [ ] Je sais trier un dictionnaire par ses valeurs avec `sorted()` et `key=`
- [ ] Je sais inverser un dictionnaire
- [ ] Je sais fusionner plusieurs sources de donnees dans un seul dictionnaire
- [ ] Je sais ecrire une comprehension de dictionnaire en une ligne

---

# NIVEAU 3 — Structures imbriquees
## Dictionnaires de listes et dictionnaires de dictionnaires

---

### Exercice 3.1 — Dictionnaire de listes

Vous gerez les notes de plusieurs etudiants. Chaque etudiant est associe a une liste de notes.

```python
notes = {
    "Alice": [14, 16, 12, 18],
    "Bob":   [9, 11, 8, 13],
    "Clara": [17, 19, 15, 20],
}
```

Ecrivez une fonction `rapport_classe(notes)` qui affiche pour chaque etudiant :
- Sa liste de notes
- Sa moyenne arrondie a 2 decimales
- Sa note maximale et minimale
- La mention correspondante (Tres Bien >= 16, Bien >= 14, Assez Bien >= 12, Passable >= 10, Insuffisant)

---

**Correction 3.1**

```python
notes = {
    "Alice": [14, 16, 12, 18],
    "Bob":   [9, 11, 8, 13],
    "Clara": [17, 19, 15, 20],
}

def calculer_mention(moy):
    if moy >= 16: return "Tres Bien"
    if moy >= 14: return "Bien"
    if moy >= 12: return "Assez Bien"
    if moy >= 10: return "Passable"
    return "Insuffisant"

def rapport_classe(notes):
    print("=" * 45)
    print("RAPPORT DE CLASSE")
    print("=" * 45)
    for nom, liste_notes in notes.items():
        moy     = sum(liste_notes) / len(liste_notes)
        mention = calculer_mention(moy)
        print(f"\nEtudiant  : {nom}")
        print(f"Notes     : {liste_notes}")
        print(f"Moyenne   : {moy:.2f} / 20")
        print(f"Max / Min : {max(liste_notes)} / {min(liste_notes)}")
        print(f"Mention   : {mention}")
    print("=" * 45)

rapport_classe(notes)
```

---

### Exercice 3.2 — Ajouter des donnees dynamiquement

Reprenez la structure de l'exercice precedent et ecrivez deux fonctions :

1. `ajouter_etudiant(notes, nom)` — ajoute un nouvel etudiant avec une liste vide
2. `ajouter_note(notes, nom, note)` — ajoute une note a un etudiant existant

Gerez les cas suivants :
- Tentative d'ajouter un etudiant qui existe deja
- Tentative d'ajouter une note a un etudiant inexistant
- Note invalide (hors de [0, 20])

---

**Correction 3.2**

```python
notes = {
    "Alice": [14, 16, 12, 18],
    "Bob":   [9, 11, 8, 13],
}

def ajouter_etudiant(notes, nom):
    """Ajoute un nouvel etudiant avec une liste de notes vide."""
    nom = nom.strip()
    if not nom:
        print("Erreur : le nom ne peut pas etre vide.")
        return False
    if nom in notes:
        print(f"Erreur : l'etudiant '{nom}' existe deja.")
        return False
    notes[nom] = []
    print(f"Etudiant '{nom}' ajoute.")
    return True


def ajouter_note(notes, nom, note):
    """Ajoute une note a un etudiant existant."""
    if nom not in notes:
        print(f"Erreur : l'etudiant '{nom}' est introuvable.")
        return False
    try:
        note = float(note)
    except (ValueError, TypeError):
        print(f"Erreur : '{note}' n'est pas un nombre valide.")
        return False
    if not 0 <= note <= 20:
        print(f"Erreur : la note {note} doit etre entre 0 et 20.")
        return False
    notes[nom].append(note)
    print(f"Note {note} ajoutee pour {nom}.")
    return True


# Tests
ajouter_etudiant(notes, "Clara")
ajouter_etudiant(notes, "Alice")    # Deja existant
ajouter_note(notes, "Clara", 15)
ajouter_note(notes, "Clara", 25)    # Note invalide
ajouter_note(notes, "David", 12)    # Etudiant inexistant
print(notes)
```

---

### Exercice 3.3 — Dictionnaire de dictionnaires

Vous gerez un repertoire de contacts. Chaque contact est lui-meme un dictionnaire.

Construisez le repertoire suivant, puis repondez aux questions :

```python
repertoire = {
    "Amadou": {"telephone": "77-123-45-67", "email": "amadou@isi.sn",  "ville": "Dakar"},
    "Bineta": {"telephone": "70-234-56-78", "email": "bineta@isi.sn",  "ville": "Thies"},
    "Cheikh": {"telephone": "76-345-67-89", "email": "cheikh@isi.sn",  "ville": "Dakar"},
    "Dieynaba":{"telephone": "78-456-78-90","email": "dieynaba@isi.sn","ville": "Ziguinchor"},
}
```

1. Affichez le telephone de "Bineta"
2. Affichez tous les contacts qui habitent "Dakar"
3. Ajoutez un champ `"actif": True` a tous les contacts
4. Affichez la liste de tous les emails

---

**Correction 3.3**

```python
repertoire = {
    "Amadou":   {"telephone": "77-123-45-67", "email": "amadou@isi.sn",   "ville": "Dakar"},
    "Bineta":   {"telephone": "70-234-56-78", "email": "bineta@isi.sn",   "ville": "Thies"},
    "Cheikh":   {"telephone": "76-345-67-89", "email": "cheikh@isi.sn",   "ville": "Dakar"},
    "Dieynaba": {"telephone": "78-456-78-90", "email": "dieynaba@isi.sn", "ville": "Ziguinchor"},
}

# 1. Telephone de Bineta
print(repertoire["Bineta"]["telephone"])   # 70-234-56-78

# 2. Contacts de Dakar
print("\nContacts a Dakar :")
for nom, infos in repertoire.items():
    if infos["ville"] == "Dakar":
        print(f"  {nom} — {infos['telephone']}")

# 3. Ajouter le champ "actif" a tous les contacts
for infos in repertoire.values():
    infos["actif"] = True

# 4. Liste de tous les emails
print("\nListe des emails :")
for nom, infos in repertoire.items():
    print(f"  {nom} : {infos['email']}")
```

> **Point cle** : Pour acceder a une valeur dans un dictionnaire imbrique,
> on enchaîne les crochets : `dict["cle1"]["cle2"]`.
> Pour modifier tous les sous-dictionnaires, on itere sur `.values()`.

---

### Exercice 3.4 — Regrouper des donnees par categorie

Soit la liste de transactions suivante :

```python
transactions = [
    {"description": "Salaire",       "montant": 250000, "type": "revenu"},
    {"description": "Loyer",         "montant": 80000,  "type": "depense"},
    {"description": "Courses",       "montant": 25000,  "type": "depense"},
    {"description": "Freelance",     "montant": 75000,  "type": "revenu"},
    {"description": "Transport",     "montant": 15000,  "type": "depense"},
    {"description": "Electricite",   "montant": 12000,  "type": "depense"},
    {"description": "Vente article", "montant": 30000,  "type": "revenu"},
]
```

1. Construisez un dictionnaire `par_type` qui regroupe les transactions par type (`"revenu"` et `"depense"`), chaque type contenant la liste des descriptions correspondantes.
2. Calculez le total des revenus et le total des depenses.
3. Calculez et affichez le solde (revenus - depenses).

---

**Correction 3.4**

```python
transactions = [
    {"description": "Salaire",       "montant": 250000, "type": "revenu"},
    {"description": "Loyer",         "montant": 80000,  "type": "depense"},
    {"description": "Courses",       "montant": 25000,  "type": "depense"},
    {"description": "Freelance",     "montant": 75000,  "type": "revenu"},
    {"description": "Transport",     "montant": 15000,  "type": "depense"},
    {"description": "Electricite",   "montant": 12000,  "type": "depense"},
    {"description": "Vente article", "montant": 30000,  "type": "revenu"},
]

# 1. Regrouper par type
par_type = {"revenu": [], "depense": []}
for t in transactions:
    par_type[t["type"]].append(t["description"])

print("Revenus  :", par_type["revenu"])
print("Depenses :", par_type["depense"])

# 2. Totaux
total_revenus  = sum(t["montant"] for t in transactions if t["type"] == "revenu")
total_depenses = sum(t["montant"] for t in transactions if t["type"] == "depense")

print(f"\nTotal revenus  : {total_revenus:>10,} FCFA")
print(f"Total depenses : {total_depenses:>10,} FCFA")

# 3. Solde
solde = total_revenus - total_depenses
statut = "excedentaire" if solde > 0 else "deficitaire" if solde < 0 else "equilibre"
print(f"Solde          : {solde:>10,} FCFA  ({statut})")
```

---

### Verification — Niveau 3

- [ ] Je sais creer et parcourir un dictionnaire dont les valeurs sont des listes
- [ ] Je sais creer et naviguer dans un dictionnaire de dictionnaires
- [ ] Je sais modifier les sous-dictionnaires en iterant sur `.values()`
- [ ] Je sais regrouper des donnees par categorie dans un dictionnaire
- [ ] Je sais combiner dictionnaires et comprehensions pour des transformations complexes

---

# NIVEAU 4 — Fonctions et cas pratiques
## Ecrire des fonctions generiques qui travaillent sur des dictionnaires

---

### Exercice 4.1 — Fonction de recherche

Ecrivez une fonction `rechercher(repertoire, champ, valeur)` qui recherche dans un dictionnaire de dictionnaires (comme l'exercice 3.3) tous les contacts dont un champ precis correspond a une valeur donnee.

```python
# Exemples d'appel :
rechercher(repertoire, "ville", "Dakar")
# Doit retourner : {"Amadou": {...}, "Cheikh": {...}}

rechercher(repertoire, "actif", True)
# Doit retourner tous les contacts actifs
```

---

**Correction 4.1**

```python
def rechercher(repertoire, champ, valeur):
    """
    Retourne un dictionnaire contenant tous les contacts
    dont le champ 'champ' est egal a 'valeur'.
    """
    resultats = {}
    for nom, infos in repertoire.items():
        # .get() evite un KeyError si le champ n'existe pas chez certains contacts
        if infos.get(champ) == valeur:
            resultats[nom] = infos
    return resultats


# Test
repertoire = {
    "Amadou":   {"telephone": "77-123-45-67", "email": "amadou@isi.sn",   "ville": "Dakar",       "actif": True},
    "Bineta":   {"telephone": "70-234-56-78", "email": "bineta@isi.sn",   "ville": "Thies",       "actif": False},
    "Cheikh":   {"telephone": "76-345-67-89", "email": "cheikh@isi.sn",   "ville": "Dakar",       "actif": True},
    "Dieynaba": {"telephone": "78-456-78-90", "email": "dieynaba@isi.sn", "ville": "Ziguinchor",  "actif": True},
}

dakarois = rechercher(repertoire, "ville", "Dakar")
print("Contacts a Dakar :")
for nom in dakarois:
    print(f"  {nom}")

actifs = rechercher(repertoire, "actif", True)
print(f"\nNombre de contacts actifs : {len(actifs)}")
```

---

### Exercice 4.2 — Statistiques sur un dictionnaire

Ecrivez une fonction `statistiques_notes(notes)` qui prend un dictionnaire `{nom: [liste de notes]}` et retourne un dictionnaire de statistiques contenant :

- `"nb_etudiants"` : nombre d'etudiants
- `"moyenne_classe"` : moyenne generale de toute la classe
- `"meilleur"` : nom de l'etudiant avec la meilleure moyenne
- `"a_ameliorer"` : liste des noms des etudiants en dessous de 10 de moyenne

```python
notes = {
    "Alice":   [14, 16, 12, 18],
    "Bob":     [9, 7, 8, 6],
    "Clara":   [17, 19, 15, 20],
    "David":   [11, 9, 10, 8],
    "Eva":     [13, 15, 14, 12],
}
```

---

**Correction 4.2**

```python
def statistiques_notes(notes):
    """Calcule des statistiques globales sur un dictionnaire de notes."""
    if not notes:
        return {}

    # Calculer la moyenne de chaque etudiant
    moyennes = {}
    for nom, liste in notes.items():
        if liste:
            moyennes[nom] = sum(liste) / len(liste)

    # Moyenne generale de la classe
    moyenne_classe = sum(moyennes.values()) / len(moyennes)

    # Meilleur etudiant
    meilleur = max(moyennes, key=moyennes.get)

    # Etudiants en dessous de 10
    a_ameliorer = [nom for nom, moy in moyennes.items() if moy < 10]

    return {
        "nb_etudiants":   len(notes),
        "moyenne_classe": round(moyenne_classe, 2),
        "meilleur":       meilleur,
        "a_ameliorer":    a_ameliorer,
    }


notes = {
    "Alice": [14, 16, 12, 18],
    "Bob":   [9, 7, 8, 6],
    "Clara": [17, 19, 15, 20],
    "David": [11, 9, 10, 8],
    "Eva":   [13, 15, 14, 12],
}

stats = statistiques_notes(notes)
print(f"Nombre d'etudiants   : {stats['nb_etudiants']}")
print(f"Moyenne de la classe : {stats['moyenne_classe']}")
print(f"Meilleur etudiant    : {stats['meilleur']}")
print(f"A ameliorer          : {stats['a_ameliorer']}")
```

Resultat attendu :
```
Nombre d'etudiants   : 5
Moyenne de la classe : 12.25
Meilleur etudiant    : Clara
A ameliorer          : ['Bob']
```

---

### Exercice 4.3 — Gestionnaire de stock

Vous gerez le stock d'une petite boutique. Ecrivez les fonctions suivantes :

```python
stock = {
    "Stylo":      {"prix": 500,  "quantite": 30},
    "Cahier":     {"prix": 1200, "quantite": 15},
    "Calculette": {"prix": 8500, "quantite": 5},
    "Regle":      {"prix": 800,  "quantite": 0},
}
```

1. `valeur_totale_stock(stock)` — retourne la valeur totale du stock (prix * quantite pour chaque produit)
2. `produits_en_rupture(stock)` — retourne la liste des produits dont la quantite est 0
3. `vendre(stock, produit, quantite)` — retire la quantite vendue du stock, affiche un message d'erreur si stock insuffisant ou produit inexistant
4. `reapprovisionner(stock, produit, quantite, prix=None)` — ajoute de la quantite, et met a jour le prix si fourni

---

**Correction 4.3**

```python
stock = {
    "Stylo":      {"prix": 500,  "quantite": 30},
    "Cahier":     {"prix": 1200, "quantite": 15},
    "Calculette": {"prix": 8500, "quantite": 5},
    "Regle":      {"prix": 800,  "quantite": 0},
}


def valeur_totale_stock(stock):
    """Calcule la valeur totale de tous les articles en stock."""
    return sum(
        infos["prix"] * infos["quantite"]
        for infos in stock.values()
    )


def produits_en_rupture(stock):
    """Retourne la liste des produits dont le stock est a zero."""
    return [produit for produit, infos in stock.items()
            if infos["quantite"] == 0]


def vendre(stock, produit, quantite):
    """Retire la quantite vendue du stock."""
    if produit not in stock:
        print(f"Erreur : le produit '{produit}' n'existe pas.")
        return False
    if quantite <= 0:
        print("Erreur : la quantite doit etre positive.")
        return False
    if stock[produit]["quantite"] < quantite:
        disponible = stock[produit]["quantite"]
        print(f"Erreur : stock insuffisant pour '{produit}' "
              f"(disponible : {disponible}, demande : {quantite}).")
        return False
    stock[produit]["quantite"] -= quantite
    print(f"Vente enregistree : {quantite} x {produit}.")
    return True


def reapprovisionner(stock, produit, quantite, prix=None):
    """Ajoute de la quantite au stock. Cree le produit s'il n'existe pas."""
    if quantite <= 0:
        print("Erreur : la quantite doit etre positive.")
        return False
    if produit not in stock:
        if prix is None:
            print(f"Erreur : prix obligatoire pour creer '{produit}'.")
            return False
        stock[produit] = {"prix": prix, "quantite": 0}
        print(f"Nouveau produit '{produit}' cree.")
    stock[produit]["quantite"] += quantite
    if prix is not None:
        stock[produit]["prix"] = prix
    print(f"Stock mis a jour : {produit} -> {stock[produit]['quantite']} unites.")
    return True


# Tests
print(f"Valeur totale du stock : {valeur_totale_stock(stock):,} FCFA")
print(f"Ruptures de stock : {produits_en_rupture(stock)}")

vendre(stock, "Stylo", 5)
vendre(stock, "Calculette", 10)   # Stock insuffisant
vendre(stock, "Gomme", 3)         # Produit inexistant

reapprovisionner(stock, "Regle", 20)
reapprovisionner(stock, "Gomme", 50, prix=300)   # Nouveau produit
print(f"\nValeur totale apres operations : {valeur_totale_stock(stock):,} FCFA")
```

---

### Verification — Niveau 4

- [ ] Je sais ecrire des fonctions qui prennent un dictionnaire en parametre et le modifient
- [ ] Je sais ecrire des fonctions qui retournent un dictionnaire de resultats
- [ ] Je sais combiner dictionnaires, boucles et conditions dans des fonctions utiles
- [ ] Je sais gerer les cas limites (cle absente, valeur invalide, stock vide)

---

# NIVEAU 5 — Defi de synthese
## Un projet complet en autonomie

---

### Enonce — Systeme de gestion de bibliotheque

Vous allez construire un mini-systeme de gestion de bibliotheque.
Chaque livre est represente par un dictionnaire. La bibliotheque est un dictionnaire de livres.

**Structure d'un livre :**
```python
{
    "titre":     "Le Petit Prince",
    "auteur":    "Antoine de Saint-Exupery",
    "annee":     1943,
    "disponible": True
}
```

**Structure de la bibliotheque :**
```python
bibliotheque = {
    "isbn-001": { ... },
    "isbn-002": { ... },
}
```

---

Implementez les fonctions suivantes :

```python
def ajouter_livre(biblio, isbn, titre, auteur, annee):
    """Ajoute un nouveau livre. Erreur si l'ISBN existe deja."""
    ...

def emprunter(biblio, isbn):
    """Marque un livre comme non disponible. Erreur si deja emprunte ou inexistant."""
    ...

def retourner(biblio, isbn):
    """Marque un livre comme disponible. Erreur si deja disponible ou inexistant."""
    ...

def rechercher_par_auteur(biblio, auteur):
    """Retourne un dictionnaire des livres de cet auteur."""
    ...

def livres_disponibles(biblio):
    """Retourne un dictionnaire des livres disponibles."""
    ...

def rapport(biblio):
    """Affiche un rapport : nombre total, disponibles, empruntes, liste complete."""
    ...
```

---

**Correction — Systeme de gestion de bibliotheque**

```python
bibliotheque = {}


def ajouter_livre(biblio, isbn, titre, auteur, annee):
    """Ajoute un nouveau livre. Erreur si l'ISBN existe deja."""
    if isbn in biblio:
        print(f"Erreur : l'ISBN '{isbn}' existe deja.")
        return False
    biblio[isbn] = {
        "titre":      titre,
        "auteur":     auteur,
        "annee":      annee,
        "disponible": True
    }
    print(f"Livre ajoute : '{titre}'")
    return True


def emprunter(biblio, isbn):
    """Marque un livre comme non disponible."""
    if isbn not in biblio:
        print(f"Erreur : ISBN '{isbn}' introuvable.")
        return False
    if not biblio[isbn]["disponible"]:
        print(f"Erreur : '{biblio[isbn]['titre']}' est deja emprunte.")
        return False
    biblio[isbn]["disponible"] = False
    print(f"Emprunt enregistre : '{biblio[isbn]['titre']}'")
    return True


def retourner(biblio, isbn):
    """Marque un livre comme disponible."""
    if isbn not in biblio:
        print(f"Erreur : ISBN '{isbn}' introuvable.")
        return False
    if biblio[isbn]["disponible"]:
        print(f"Erreur : '{biblio[isbn]['titre']}' n'est pas emprunte.")
        return False
    biblio[isbn]["disponible"] = True
    print(f"Retour enregistre : '{biblio[isbn]['titre']}'")
    return True


def rechercher_par_auteur(biblio, auteur):
    """Retourne un dictionnaire des livres d'un auteur (insensible a la casse)."""
    return {
        isbn: infos
        for isbn, infos in biblio.items()
        if infos["auteur"].lower() == auteur.lower()
    }


def livres_disponibles(biblio):
    """Retourne un dictionnaire des livres disponibles."""
    return {
        isbn: infos
        for isbn, infos in biblio.items()
        if infos["disponible"]
    }


def rapport(biblio):
    """Affiche un rapport complet de la bibliotheque."""
    total       = len(biblio)
    disponibles = sum(1 for infos in biblio.values() if infos["disponible"])
    empruntes   = total - disponibles

    print("=" * 55)
    print("RAPPORT DE LA BIBLIOTHEQUE")
    print("=" * 55)
    print(f"Total de livres  : {total}")
    print(f"Disponibles      : {disponibles}")
    print(f"Empruntes        : {empruntes}")
    print("-" * 55)

    for isbn, infos in biblio.items():
        statut = "disponible" if infos["disponible"] else "emprunte  "
        print(f"[{isbn}] {infos['titre']:<30} {infos['auteur']:<25} ({statut})")

    print("=" * 55)


# --- Tests complets ---
ajouter_livre(bibliotheque, "isbn-001", "Le Petit Prince",          "Antoine de Saint-Exupery", 1943)
ajouter_livre(bibliotheque, "isbn-002", "L'Etranger",               "Albert Camus",             1942)
ajouter_livre(bibliotheque, "isbn-003", "Soundjata",                "Djibril Tamsir Niane",     1960)
ajouter_livre(bibliotheque, "isbn-004", "La Chute",                 "Albert Camus",             1956)
ajouter_livre(bibliotheque, "isbn-005", "Les Bouts de Bois de Dieu","Ousmane Sembene",          1960)

emprunter(bibliotheque, "isbn-001")
emprunter(bibliotheque, "isbn-003")
emprunter(bibliotheque, "isbn-001")   # Deja emprunte

retourner(bibliotheque, "isbn-001")
retourner(bibliotheque, "isbn-002")   # Pas emprunte

livres_camus = rechercher_par_auteur(bibliotheque, "Albert Camus")
print(f"\nLivres de Camus : {len(livres_camus)}")
for isbn, infos in livres_camus.items():
    print(f"  {infos['titre']}")

dispos = livres_disponibles(bibliotheque)
print(f"\nLivres disponibles actuellement : {len(dispos)}")

rapport(bibliotheque)
```

---

# Recapitulatif — Methodes essentielles des dictionnaires

| Methode / Syntaxe | Description | Exemple |
|---|---|---|
| `d["cle"]` | Acceder a une valeur (KeyError si absente) | `d["nom"]` |
| `d.get("cle", defaut)` | Acceder sans risque d'erreur | `d.get("age", 0)` |
| `d["cle"] = valeur` | Ajouter ou modifier une entree | `d["ville"] = "Dakar"` |
| `del d["cle"]` | Supprimer une entree | `del d["age"]` |
| `d.pop("cle")` | Supprimer et retourner la valeur | `val = d.pop("age")` |
| `"cle" in d` | Tester l'existence d'une cle | `if "nom" in d:` |
| `d.keys()` | Retourne toutes les cles | `for cle in d.keys()` |
| `d.values()` | Retourne toutes les valeurs | `for val in d.values()` |
| `d.items()` | Retourne les paires (cle, valeur) | `for k, v in d.items()` |
| `len(d)` | Nombre d'entrees | `len(d)` |
| `d.update(d2)` | Fusionne d2 dans d (ecrase les doublons) | `d.update({"age": 21})` |
| `{k: v for ...}` | Comprehension de dictionnaire | `{n: n**2 for n in range(5)}` |

---

## Pour aller plus loin

### Niveau intermediaire

1. **`collections.defaultdict`** — dictionnaire avec valeur par defaut automatique, evite les verifications `if cle not in dict`
2. **`collections.Counter`** — specialise dans le comptage, remplace le patron `dict.get(cle, 0) + 1`
3. **`collections.OrderedDict`** — dictionnaire ordonne (utile avant Python 3.7)
4. **Fusion avec `|`** — depuis Python 3.9 : `d3 = d1 | d2` fusionne deux dictionnaires

### Niveau avance

5. **`dict.setdefault(cle, defaut)`** — insere la valeur par defaut si la cle est absente et la retourne
6. **Dictionnaires comme structures de dispatch** — remplacer de longues chaines `if/elif` par un dictionnaire de fonctions
7. **JSON et dictionnaires** — serialisation et deserialization avec `json.dumps()` et `json.loads()`
8. **Dictionnaires et classes** — `__dict__` d'un objet, `vars()`, `dataclasses`

---

> **Ce que vous avez maitrise dans ces exercices**
>
> Les dictionnaires sont la structure de donnees la plus polyvalente de Python.
> Vous savez maintenant les creer, les parcourir, les filtrer, les trier et les imbriquer.
> La maitrise des dictionnaires est une condition necessaire pour aborder serieusement
> la manipulation de fichiers JSON, les API web, les bases de donnees et la programmation orientee objet.