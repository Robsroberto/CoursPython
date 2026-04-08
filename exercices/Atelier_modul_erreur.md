---
marp: false
size: 4:3
style: |  
  h2, h3, p {
    font-size: 20px;
  }
  li {
    font-size:20px
  }
headingDivider: 1
header: 
paginate: true
# footer: Licence 2 Informatique &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ISI (Institut Supérieur D'Informatique) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RD
---
<img src="../isi.png" alt="ISI" width="100px">

# Atelier Python — Modularite, Gestion des Erreurs et Slicing


## Par Robert DIASSÉ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="../python.jpeg" alt="ISI" width="50px">
---

### Ecrire du code robuste, organise et expressif

---

> **Niveau** : Debutant ayant les bases (variables, listes, fonctions, boucles)

> **Duree estimee** : 2h30 a 3h30

> **Prerequis** : Python 3.8+, un editeur de texte (VS Code, Thonny, PyCharm)

> **Objectif** : Comprendre comment structurer un projet, anticiper les erreurs et manipuler les donnees avec elegance

---

## Plan de l'atelier

| Partie | Theme | Duree |
|---|---|---|
| **Partie 1** | Le Slicing — decouper les donnees | ~40 min |
| **Partie 2** | La Gestion des erreurs — ecrire du code qui resiste | ~50 min |
| **Partie 3** | La Modularite — organiser un projet | ~60 min |
| **Partie 4** | Projet de synthese — tout assembler | ~40 min |

---

# PARTIE 1 — Le Slicing
## Decouper, extraire, inverser en une ligne

---

## Qu'est-ce que le slicing ?

En Python, les **listes**, les **chaines de caracteres** et les **tuples** sont des sequences ordonnees.
Le **slicing** (decoupage) permet d'extraire une portion de ces sequences avec une syntaxe tres concise.

La syntaxe de base est :

```
sequence[debut : fin : pas]
```

- `debut` : indice du premier element a inclure (inclus)
- `fin` : indice du premier element a **exclure** (non inclus)
- `pas` : le saut entre chaque element (par defaut : 1)

> Chacun de ces parametres est **optionnel**. S'il est omis, Python utilise la valeur par defaut adaptee.

---

## 1.1 — Les indices en Python

Creez un fichier `slicing.py` et executez chaque bloc au fur et a mesure.

```python
# Une liste de fruits
fruits = ["pomme", "banane", "cerise", "datte", "figue", "mangue"]
#   indice :   0        1         2        3        4        5
# indice negatif: -6      -5        -4       -3       -2       -1

# Acces classique par indice positif
print(fruits[0])    # pomme  (premier element)
print(fruits[2])    # cerise (troisieme element)

# Acces par indice negatif : -1 = dernier, -2 = avant-dernier...
print(fruits[-1])   # mangue
print(fruits[-2])   # figue
```

> **Notion cle — Indices negatifs**
>
> Les indices negatifs comptent a partir de la fin.
> `liste[-1]` est toujours le dernier element, quelle que soit la taille de la liste.
> C'est une alternative elegante a `liste[len(liste) - 1]`.

---

## 1.2 — Slicing de base

```python
fruits = ["pomme", "banane", "cerise", "datte", "figue", "mangue"]

# Extraire les elements de l'indice 1 (inclus) a 4 (exclu)
print(fruits[1:4])    # ['banane', 'cerise', 'datte']

# Debut omis : part du premier element
print(fruits[:3])     # ['pomme', 'banane', 'cerise']

# Fin omise : va jusqu'au dernier element (inclus)
print(fruits[3:])     # ['datte', 'figue', 'mangue']

# Les deux omis : copie toute la liste
print(fruits[:])      # ['pomme', 'banane', 'cerise', 'datte', 'figue', 'mangue']
```

> **A retenir** : Le slicing **ne modifie jamais** la liste d'origine.
> Il retourne toujours une **nouvelle** liste contenant les elements extraits.

---

## 1.3 — Le parametre de pas (step)

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pas de 2 : un element sur deux
print(nombres[::2])     # [0, 2, 4, 6, 8]

# Pas de 3 : un element sur trois
print(nombres[::3])     # [0, 3, 6, 9]

# De l'indice 1 a 8, un sur deux
print(nombres[1:8:2])   # [1, 3, 5, 7]

# Pas negatif : parcours en sens inverse
print(nombres[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Les 3 derniers elements en sens inverse
print(nombres[-1:-4:-1])  # [9, 8, 7]
```

---

## 1.4 — Slicing sur les chaines de caracteres

Le slicing fonctionne **exactement pareil** sur les chaines :

```python
message = "Bonjour le monde !"
#   index :  0123456789...

# Extraire les 7 premiers caracteres
print(message[:7])      # "Bonjour"

# Extraire a partir du caractere 11
print(message[11:])     # "monde !"

# Extraire du caractere 8 au 10 (inclus)
print(message[8:10])    # "le"

# Inverser une chaine
print(message[::-1])    # "! ednom el ruojnoB"

# Un caractere sur deux
print(message[::2])     # "Bnore od!"
```

> **Astuce** : `chaine[::-1]` est la facon pythonique d'inverser une chaine.
> C'est beaucoup plus court qu'une boucle `for`.

---

## 1.5 — Utilisations pratiques

```python
# -- Verifier si une chaine est un palindrome ------------------------------------
def est_palindrome(mot):
    """Retourne True si le mot se lit pareil dans les deux sens."""
    mot = mot.lower()               # Ignorer la casse
    return mot == mot[::-1]         # Comparer avec l'inverse

print(est_palindrome("radar"))      # True
print(est_palindrome("kayak"))      # True
print(est_palindrome("python"))     # False


# -- Extraire les N premiers et N derniers elements ------------------------------
notes = [12, 8, 15, 9, 17, 11, 6, 14, 13, 10]

trois_premiers = notes[:3]          # [12, 8, 15]
trois_derniers = notes[-3:]         # [14, 13, 10]
sans_extremes  = notes[1:-1]        # Sans le premier et le dernier

print(f"3 premieres notes : {trois_premiers}")
print(f"3 dernieres notes : {trois_derniers}")
print(f"Notes sans extremes : {sans_extremes}")


# -- Decouper un message encode (un caractere sur deux) --------------------------
message_cache = "pByotmhmonene"
message_reel  = message_cache[::2]  # "python"
print(f"Message decode : {message_reel}")


# -- Diviser une liste en deux moities egales ------------------------------------
equipe = ["Alice", "Bob", "Clara", "David", "Eva", "Farid"]
milieu = len(equipe) // 2
equipe_a = equipe[:milieu]          # ['Alice', 'Bob', 'Clara']
equipe_b = equipe[milieu:]          # ['David', 'Eva', 'Farid']
print(f"Equipe A : {equipe_a}")
print(f"Equipe B : {equipe_b}")
```

---

## Exercices — Partie 1

### Exercice 1.A — Manipulation de liste

Soit la liste suivante :
```python
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```
Sans utiliser de boucle, repondez a ces questions en une ligne chacune :

1. Extraire les elements de 30 a 70 inclus
2. Extraire les 3 derniers elements
3. Extraire tous les elements de position paire (indice 0, 2, 4...)
4. Inverser completement la liste
5. Extraire les elements du milieu (sans le premier et le dernier)

---

### Exercice 1.B — Traitement de chaine

```python
texte = "L'informatique est une science fascinante"
```

1. Extraire le mot `"informatique"` (indices 2 a 14)
2. Extraire les 3 derniers caracteres
3. Verifier si `"laval"` est un palindrome avec une seule expression
4. Creer une version "sur deux lettres" de `texte` (un caractere sur deux)

---

### Exercice 1.C — Defi palindrome avance

Ecrivez une fonction `nettoyer_et_verifier(phrase)` qui :
- Supprime les espaces et la ponctuation
- Ignore les majuscules et minuscules
- Retourne `True` si la phrase est un palindrome

```python
# Tests attendus :
nettoyer_et_verifier("Engage le jeu que je le gagne")  # True
nettoyer_et_verifier("Bonjour")                         # False
```

> **Indice** : `"".join(c for c in phrase if c.isalpha())` filtre les lettres uniquement.

---

### Verification — Partie 1

Avant de continuer, vous devez maitriser ces points :

- [ ] Je sais extraire une portion de liste ou de chaine avec `[debut:fin]`
- [ ] Je sais utiliser les indices negatifs
- [ ] Je sais utiliser le pas (step) avec `[::pas]`
- [ ] Je sais inverser une sequence avec `[::-1]`
- [ ] Je comprends que le slicing ne modifie pas l'original

---

# PARTIE 2 — La Gestion des Erreurs
## Ecrire du code qui resiste aux imprevus

---

## Pourquoi gerer les erreurs ?

Sans gestion d'erreurs, un programme s'arrete brutalement a la moindre anomalie.
Un programme **robuste** anticipe les problemes et y repond de facon controlee.

```python
# Sans gestion d'erreur : le programme plante
notes = [15, 12, 18]
print(notes[5])      # IndexError: list index out of range
# Tout s'arrete ici, la suite du code ne s'execute pas
```

```python
# Avec gestion d'erreur : le programme continue
notes = [15, 12, 18]
try:
    print(notes[5])
except IndexError:
    print("Cet indice n'existe pas.")
print("Le programme continue normalement.")
```

---

## 2.1 — La structure try / except

Creez un fichier `erreurs.py`.

```python
# Structure de base
try:
    # Code qui POURRAIT provoquer une erreur
    resultat = 10 / 0
except ZeroDivisionError:
    # Code execute SI cette erreur precise se produit
    print("Erreur : division par zero !")


# -- Plusieurs except pour gerer differentes erreurs ----------------------------
def diviser(a, b):
    """Divise a par b avec gestion d'erreurs."""
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        print("Impossible de diviser par zero.")
        return None
    except TypeError:
        print(f"Types invalides : {type(a)} et {type(b)}")
        return None

print(diviser(10, 2))     # 5.0
print(diviser(10, 0))     # Impossible de diviser par zero. -> None
print(diviser(10, "a"))   # Types invalides -> None
```

---

## 2.2 — Les clauses else et finally

```python
def lire_age(texte):
    """Convertit un texte en age valide."""
    try:
        age = int(texte)                    # Peut lever ValueError
        if age < 0 or age > 130:
            raise ValueError("Age hors limites")  # On leve nous-memes une erreur
    except ValueError as e:
        # 'as e' permet de recuperer le message de l'erreur
        print(f"Valeur invalide : {e}")
        return None
    else:
        # S'execute UNIQUEMENT si aucune exception n'a ete levee dans try
        print(f"Age valide : {age} ans")
        return age
    finally:
        # S'execute TOUJOURS, qu'il y ait eu erreur ou non
        # Ideal pour fermer des fichiers, liberer des ressources...
        print("--- Fin de la verification ---")

lire_age("25")      # Age valide + finally
lire_age("abc")     # ValueError + finally
lire_age("-5")      # ValueError (hors limites) + finally
lire_age("200")     # ValueError (hors limites) + finally
```

> **Recapitulatif try / except / else / finally**
>
> | Clause | Quand s'execute-t-elle ? |
> |---|---|
> | `try` | Toujours (c'est le code a surveiller) |
> | `except` | Uniquement si une erreur du type precise se produit |
> | `else` | Uniquement si **aucune** erreur ne s'est produite |
> | `finally` | **Toujours**, avec ou sans erreur |

---

## 2.3 — Les erreurs les plus courantes

```python
# -- IndexError : acces hors des limites d'une liste ----------------------------
fruits = ["pomme", "banane"]
try:
    print(fruits[10])
except IndexError as e:
    print(f"IndexError : {e}")


# -- KeyError : cle inexistante dans un dictionnaire ----------------------------
etudiant = {"nom": "Alice", "note": 15}
try:
    print(etudiant["age"])
except KeyError as e:
    print(f"KeyError : la cle {e} n'existe pas")
    # Alternative sans try/except : utiliser dict.get()
    age = etudiant.get("age", "non renseigne")
    print(f"Age : {age}")


# -- ValueError : valeur de mauvais type ou format ------------------------------
try:
    nombre = int("bonjour")
except ValueError as e:
    print(f"ValueError : {e}")


# -- FileNotFoundError : fichier introuvable ------------------------------------
try:
    with open("fichier_inexistant.txt", "r") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Le fichier demande n'existe pas.")


# -- TypeError : operation sur un type incorrect --------------------------------
try:
    resultat = "5" + 3
except TypeError as e:
    print(f"TypeError : {e}")
```

---

## 2.4 — Creer ses propres exceptions

Pour les applications plus serieuses, on cree des exceptions personnalisees qui decrivent precisement le probleme metier.

```python
# -- Definir des exceptions personnalisees --------------------------------------
# Une exception est une classe qui herite d'Exception
class NoteInvalideError(Exception):
    """Levee quand une note n'est pas dans l'intervalle [0, 20]."""
    pass

class EtudiantIntrouvableError(Exception):
    """Levee quand un etudiant n'est pas trouve dans la base."""
    pass


# -- Utiliser les exceptions personnalisees -------------------------------------
def ajouter_note(etudiant, note):
    """Ajoute une note a un etudiant avec validation."""
    if not isinstance(note, (int, float)):
        raise TypeError(f"La note doit etre un nombre, pas {type(note).__name__}")
    if not 0 <= note <= 20:
        raise NoteInvalideError(f"Note {note} invalide — doit etre entre 0 et 20")
    etudiant["notes"].append(note)
    print(f"Note {note} ajoutee pour {etudiant['nom']}")


def trouver_etudiant(liste, nom):
    """Recherche un etudiant dans une liste."""
    for etudiant in liste:
        if etudiant["nom"].lower() == nom.lower():
            return etudiant
    raise EtudiantIntrouvableError(f"Aucun etudiant nomme '{nom}' trouve")


# -- Test des exceptions personnalisees -----------------------------------------
etudiants = [
    {"nom": "Alice", "notes": [14, 16]},
    {"nom": "Bob",   "notes": [11, 13]},
]

try:
    alice = trouver_etudiant(etudiants, "Alice")
    ajouter_note(alice, 18)       # OK
    ajouter_note(alice, 25)       # NoteInvalideError
except NoteInvalideError as e:
    print(f"Erreur de note : {e}")
except EtudiantIntrouvableError as e:
    print(f"Erreur de recherche : {e}")

try:
    trouver_etudiant(etudiants, "Clara")   # EtudiantIntrouvableError
except EtudiantIntrouvableError as e:
    print(f"Erreur de recherche : {e}")
```

> **Bonne pratique**
> Utilisez des exceptions personnalisees des que votre programme gere un domaine precis (notes, budgets, utilisateurs...).
> Elles rendent le code beaucoup plus lisible : `except NoteInvalideError` est plus clair que `except ValueError`.

---

## 2.5 — Saisie securisee avec boucle

Un cas tres courant : demander une saisie a l'utilisateur jusqu'a ce qu'elle soit valide.

```python
def saisir_entier(message, minimum=None, maximum=None):
    """
    Demande un entier a l'utilisateur en boucle jusqu'a saisie valide.
    Respecte optionnellement des bornes min et max.
    """
    while True:
        try:
            valeur = int(input(message))

            if minimum is not None and valeur < minimum:
                print(f"  La valeur doit etre >= {minimum}")
                continue    # Retourne au debut du while

            if maximum is not None and valeur > maximum:
                print(f"  La valeur doit etre <= {maximum}")
                continue

            return valeur   # Saisie valide : on sort de la boucle

        except ValueError:
            print("  Saisie invalide, entrez un nombre entier.")


# Utilisation
age   = saisir_entier("Votre age : ", minimum=0, maximum=130)
note  = saisir_entier("Une note sur 20 : ", minimum=0, maximum=20)
print(f"Age : {age}, Note : {note}")
```

---

## Exercices — Partie 2

### Exercice 2.A — Convertisseur securise

Ecrivez une fonction `convertir_temperature(valeur, unite)` qui :
- Convertit de Celsius en Fahrenheit (`"C"`) ou l'inverse (`"F"`)
- Leve une `ValueError` si l'unite est autre que `"C"` ou `"F"`
- Leve une `TypeError` si la valeur n'est pas un nombre
- Retourne le resultat arrondi a 2 decimales

```python
# Tests attendus :
convertir_temperature(100, "C")    # 212.0
convertir_temperature(32, "F")     # 0.0
convertir_temperature(20, "X")     # ValueError
convertir_temperature("chaud","C") # TypeError
```

---

### Exercice 2.B — Lecteur de fichier robuste

Ecrivez une fonction `lire_notes_depuis_fichier(chemin)` qui :
- Ouvre un fichier texte contenant une note par ligne (ex : `"14\n16\n..."`)
- Retourne la liste des notes sous forme de nombres flottants
- Gere proprement : fichier introuvable, ligne non numerique, note hors [0, 20]
- Affiche un message d'avertissement pour chaque ligne ignoree, sans arreter le programme

---

### Exercice 2.C — Exception personnalisee

Creez une classe `BudgetDepasseError` et une fonction `retirer_argent(solde, montant)` qui :
- Leve `BudgetDepasseError` si le montant depasse le solde
- Leve `ValueError` si le montant est negatif ou nul
- Retourne le nouveau solde si tout va bien

---

### Verification — Partie 2

- [ ] Je sais ecrire un bloc `try/except` et attraper une erreur precise
- [ ] Je connais la difference entre `else` et `finally`
- [ ] Je sais utiliser `raise` pour lever une erreur moi-meme
- [ ] Je sais creer une classe d'exception personnalisee
- [ ] Je sais ecrire une boucle de saisie utilisateur robuste

---

# PARTIE 3 — La Modularite
## Organiser son code en fichiers et en modules

---

## Pourquoi modulariser ?

Imaginez un programme de 2 000 lignes dans un seul fichier : difficile a lire, difficile a corriger, impossible a reutiliser dans un autre projet.

La **modularite** consiste a decouper le programme en **modules** : des fichiers `.py` autonomes, chacun responsable d'une tache precise.

> **Principe de responsabilite unique**
> Chaque fichier (module) doit avoir une seule raison d'exister.
> `calculs.py` fait des calculs. `affichage.py` affiche des donnees. `fichiers.py` lit et ecrit des fichiers.

---

## 3.1 — Creer et importer un module

Creez cette structure de dossiers :

```
projet_notes/
|-- main.py          <- Point d'entree du programme
|-- calculs.py       <- Fonctions mathematiques
|-- affichage.py     <- Fonctions d'affichage
|-- fichiers.py      <- Lecture et ecriture de donnees
```

---

**Fichier `calculs.py`** — Fonctions de calcul :

```python
# calculs.py
# Ce module contient toutes les fonctions de calcul sur les notes.

def moyenne(notes):
    """Calcule la moyenne d'une liste de notes.

    Parametre : notes — liste de nombres
    Retourne  : float ou None si la liste est vide
    """
    if not notes:
        return None
    return sum(notes) / len(notes)


def note_max(notes):
    """Retourne la note maximale. Leve ValueError si la liste est vide."""
    if not notes:
        raise ValueError("La liste de notes est vide.")
    return max(notes)


def note_min(notes):
    """Retourne la note minimale. Leve ValueError si la liste est vide."""
    if not notes:
        raise ValueError("La liste de notes est vide.")
    return min(notes)


def mention(moyenne):
    """Retourne la mention correspondant a une moyenne.

    Parametre : moyenne — float entre 0 et 20
    Retourne  : str — la mention
    """
    if moyenne is None:
        return "Sans note"
    if moyenne >= 16:
        return "Tres Bien"
    elif moyenne >= 14:
        return "Bien"
    elif moyenne >= 12:
        return "Assez Bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Insuffisant"


def statistiques(notes):
    """Retourne un dictionnaire complet des statistiques d'une liste de notes."""
    if not notes:
        return {}
    moy = moyenne(notes)
    return {
        "moyenne":            round(moy, 2),
        "maximum":            note_max(notes),
        "minimum":            note_min(notes),
        "mention":            mention(moy),
        "nb_notes":           len(notes),
        "au_dessus_moyenne":  len([n for n in notes if n >= moy])
    }
```

---

**Fichier `affichage.py`** — Fonctions d'affichage :

```python
# affichage.py
# Ce module gere tout ce qui concerne l'affichage dans le terminal.

# On importe les fonctions dont on a besoin depuis notre propre module
from calculs import statistiques

LARGEUR = 50   # Largeur des cadres affiches


def ligne_separateur(caractere="-"):
    """Affiche une ligne de separation."""
    print(caractere * LARGEUR)


def afficher_titre(titre):
    """Affiche un titre encadre."""
    print()
    ligne_separateur("=")
    print(f"  {titre.upper()}")
    ligne_separateur("=")


def afficher_etudiant(etudiant):
    """Affiche le profil complet d'un etudiant."""
    stats = statistiques(etudiant["notes"])

    afficher_titre(f"Profil — {etudiant['nom']}")

    if not stats:
        print("  Aucune note enregistree.")
        return

    notes = etudiant["notes"]
    print(f"  Toutes les notes  : {notes}")
    print(f"  3 dernieres notes : {notes[-3:]}")   # Slicing
    print()
    print(f"  Moyenne  : {stats['moyenne']} / 20")
    print(f"  Maximum  : {stats['maximum']}")
    print(f"  Minimum  : {stats['minimum']}")
    print(f"  Mention  : {stats['mention']}")
    print(f"  Au-dessus de la moyenne : {stats['au_dessus_moyenne']} note(s)")
    ligne_separateur()


def afficher_classement(etudiants):
    """Affiche le classement des etudiants par moyenne decroissante."""
    afficher_titre("Classement general")

    tries = sorted(
        etudiants,
        key=lambda e: statistiques(e["notes"]).get("moyenne", 0),
        reverse=True
    )

    for rang, etudiant in enumerate(tries, start=1):
        stats      = statistiques(etudiant["notes"])
        moy        = stats.get("moyenne", 0)
        mention_txt = stats.get("mention", "Sans note")
        print(f"  {rang:>2}. {etudiant['nom']:<15} {moy:>5.2f}/20  — {mention_txt}")

    ligne_separateur()
```

---

**Fichier `fichiers.py`** — Lecture et ecriture :

```python
# fichiers.py
# Ce module gere la persistance des donnees (lecture et sauvegarde).

import json
import os


def sauvegarder(etudiants, chemin="etudiants.json"):
    """
    Sauvegarde la liste des etudiants dans un fichier JSON.
    Retourne True en cas de succes, False sinon.
    """
    try:
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(etudiants, f, ensure_ascii=False, indent=2)
        print(f"  Donnees sauvegardees dans '{chemin}'")
        return True
    except PermissionError:
        print(f"  Permission refusee pour ecrire dans '{chemin}'")
        return False
    except Exception as e:
        print(f"  Erreur inattendue lors de la sauvegarde : {e}")
        return False


def charger(chemin="etudiants.json"):
    """
    Charge les etudiants depuis un fichier JSON.
    Retourne une liste vide si le fichier n'existe pas.
    """
    if not os.path.exists(chemin):
        print(f"  Aucun fichier '{chemin}' trouve. Demarrage a vide.")
        return []

    try:
        with open(chemin, "r", encoding="utf-8") as f:
            donnees = json.load(f)
        print(f"  {len(donnees)} etudiant(s) charge(s) depuis '{chemin}'")
        return donnees
    except json.JSONDecodeError:
        print(f"  Le fichier '{chemin}' est corrompu ou mal formate.")
        return []
    except Exception as e:
        print(f"  Erreur inattendue lors du chargement : {e}")
        return []
```

---

**Fichier `main.py`** — Point d'entree du programme :

```python
# main.py
# Point d'entree : orchestre les autres modules.
# Ce fichier ne contient que la logique principale, pas les details.

# -- Imports des modules du projet -----------------------------------------------
from calculs   import statistiques, mention
from affichage import afficher_etudiant, afficher_classement, afficher_titre
from fichiers  import sauvegarder, charger


# -- Exception personnalisee pour ce module -------------------------------------
class NoteInvalideError(Exception):
    pass


# -- Fonctions de gestion des etudiants -----------------------------------------
def ajouter_note(etudiant, note):
    """Ajoute une note validee a un etudiant."""
    try:
        note = float(note)
    except (ValueError, TypeError):
        raise NoteInvalideError(f"'{note}' n'est pas un nombre valide.")
    if not 0 <= note <= 20:
        raise NoteInvalideError(f"La note {note} doit etre entre 0 et 20.")
    etudiant["notes"].append(note)


def creer_etudiant(nom):
    """Cree et retourne un nouvel etudiant."""
    if not nom or not nom.strip():
        raise ValueError("Le nom de l'etudiant ne peut pas etre vide.")
    return {"nom": nom.strip(), "notes": []}


# -- Programme principal --------------------------------------------------------
if __name__ == "__main__":
    # Ce bloc ne s'execute QUE si on lance directement main.py
    # (pas si on l'importe depuis un autre module)

    afficher_titre("Gestionnaire de Notes ISI")

    # Charger les donnees existantes
    etudiants = charger()

    # Si aucune donnee, creer des etudiants de demonstration
    if not etudiants:
        print("\n  Creation de donnees de demonstration...")
        donnees_demo = [
            ("Alice",  [14, 16, 12, 18, 15]),
            ("Bob",    [9,  11, 8,  13, 10]),
            ("Clara",  [17, 19, 16, 18, 20]),
            ("David",  [7,  9,  11, 8,  6 ]),
            ("Eva",    [13, 15, 14, 12, 16]),
        ]
        for nom, notes in donnees_demo:
            e = creer_etudiant(nom)
            for note in notes:
                try:
                    ajouter_note(e, note)
                except NoteInvalideError as err:
                    print(f"  Note ignoree pour {nom} : {err}")
            etudiants.append(e)

        sauvegarder(etudiants)

    # Afficher le profil de chaque etudiant
    for etudiant in etudiants:
        afficher_etudiant(etudiant)

    # Afficher le classement general
    afficher_classement(etudiants)

    # Slicing : afficher le podium (top 3)
    afficher_titre("Podium — Top 3")
    tries = sorted(
        etudiants,
        key=lambda e: statistiques(e["notes"]).get("moyenne", 0),
        reverse=True
    )
    podium = tries[:3]   # Slicing pour extraire les 3 premiers
    rangs  = ["1er", "2eme", "3eme"]
    for rang, etudiant in zip(rangs, podium):
        stats = statistiques(etudiant["notes"])
        print(f"  {rang}  {etudiant['nom']} — {stats['moyenne']}/20")
```

---

## 3.2 — La regle `if __name__ == "__main__"`

```python
# Pourquoi cette ligne ?

# Cas 1 : vous lancez directement main.py
#   -> __name__ vaut "__main__"
#   -> le bloc s'execute

# Cas 2 : un autre fichier fait "import main"
#   -> __name__ vaut "main" (le nom du module)
#   -> le bloc NE s'execute PAS

# Sans cette protection, importer un module declencherait son execution !
if __name__ == "__main__":
    print("Ce code s'execute uniquement si on lance ce fichier directement.")
```

---

## 3.3 — Les differentes formes d'import

```python
# -- Importer tout un module -----------------------------------------------------
import calculs
resultat = calculs.moyenne([14, 16, 18])

# -- Importer des fonctions precises ---------------------------------------------
from calculs import moyenne, mention
resultat = moyenne([14, 16, 18])     # Pas besoin de "calculs." devant

# -- Importer avec un alias ------------------------------------------------------
import calculs as calc
resultat = calc.moyenne([14, 16, 18])

# -- A EVITER en production : importer tout avec * --------------------------------
from calculs import *   # Risque de conflits de noms, code moins lisible
```

> **Bonne pratique**
> Preferez `from module import fonction` pour les fonctions que vous utilisez souvent.
> Utilisez `import module` si vous faites appel a de nombreuses fonctions du module.

---

## Exercices — Partie 3

### Exercice 3.A — Reorganiser un code existant

Voici un code monolithique (tout dans un seul fichier). Reorganisez-le en 3 modules :

```python
produits = [
    {"nom": "Stylo",      "prix": 500,  "stock": 30},
    {"nom": "Cahier",     "prix": 1200, "stock": 15},
    {"nom": "Regle",      "prix": 800,  "stock": 0 },
    {"nom": "Calculette", "prix": 8500, "stock": 5 },
]

def prix_moyen(produits):
    if not produits:
        return 0
    return sum(p["prix"] for p in produits) / len(produits)

def produits_en_stock(produits):
    return [p for p in produits if p["stock"] > 0]

def afficher_produit(p):
    statut = "En stock" if p["stock"] > 0 else "Rupture"
    print(f"  {p['nom']:<15} {p['prix']:>6} FCFA  — {statut}")

def afficher_catalogue(produits):
    print("=== CATALOGUE ===")
    for p in produits:
        afficher_produit(p)
    print(f"Prix moyen : {prix_moyen(produits):.0f} FCFA")

import json
def sauvegarder_catalogue(produits, chemin="catalogue.json"):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(produits, f, ensure_ascii=False, indent=2)

afficher_catalogue(produits)
sauvegarder_catalogue(produits)
```

**Consigne** : Creez `calculs_boutique.py`, `affichage_boutique.py`, `fichiers_boutique.py` et `main_boutique.py`.

---

### Exercice 3.B — Module utilitaires

Creez un module `utils.py` contenant des fonctions generiques reutilisables :

1. `valider_chaine(texte, min_len=1, max_len=100)` — verifie qu'une chaine est valide
2. `saisir_choix(message, options)` — demande a l'utilisateur de choisir parmi une liste
3. `formater_nombre(n, separateur=" ")` — formate `1500000` en `"1 500 000"`

Ces fonctions doivent pouvoir etre importees par n'importe quel autre module.

---

### Verification — Partie 3

- [ ] Je sais creer un module Python (un fichier `.py` avec des fonctions)
- [ ] Je sais importer un module avec `import` et `from ... import`
- [ ] Je comprends la difference entre les formes d'import
- [ ] Je comprends le role de `if __name__ == "__main__"`
- [ ] Je sais organiser un projet en plusieurs fichiers par responsabilite

---

# PARTIE 4 — Projet de Synthese
## Les trois concepts en action

---

## Enonce — Mini-bibliotheque de traitement de texte

Vous allez creer un outil d'analyse de texte en 3 modules.
Cet outil permettra d'analyser n'importe quel texte et d'en extraire des statistiques.

### Structure attendue

```
analyseur_texte/
|-- main.py           <- Menu et orchestration
|-- traitement.py     <- Fonctions d'analyse (slicing utilise ici)
|-- affichage.py      <- Affichage des resultats
|-- textes/
    |-- exemple.txt   <- Fichier texte de test
```

---

### Module `traitement.py`

Implementez ces fonctions (toutes avec gestion d'erreurs) :

```python
# traitement.py

def compter_mots(texte):
    """Retourne le nombre de mots dans le texte."""
    # texte.split() decoupe sur les espaces
    ...

def compter_caracteres(texte, ignorer_espaces=True):
    """Retourne le nombre de caracteres (espaces optionnellement exclus)."""
    ...

def mots_les_plus_frequents(texte, n=5):
    """Retourne les n mots les plus frequents sous forme de liste de tuples.
    Utilise le slicing pour limiter aux n premiers resultats.
    """
    # Indice : dict pour compter, sorted() pour trier, [:n] pour limiter
    ...

def extraire_debut_fin(texte, nb_mots=10):
    """Retourne les nb_mots premiers et derniers mots du texte.
    Utilise obligatoirement le slicing.
    """
    mots  = texte.split()
    debut = mots[:nb_mots]     # Slicing
    fin   = mots[-nb_mots:]    # Slicing avec indice negatif
    return debut, fin

def est_palindrome_phrase(phrase):
    """Verifie si une phrase est un palindrome (ignore casse et ponctuation).
    Utilise le slicing pour comparer avec l'inverse.
    """
    ...

def inverser_mots(texte):
    """Retourne le texte avec l'ordre des mots inverse.
    Utilise le slicing pour inverser la liste de mots.
    """
    mots = texte.split()
    return " ".join(mots[::-1])   # Slicing inverse
```

---

### Module `affichage.py`

```python
# affichage.py

def afficher_stats(texte, stats):
    """Affiche un rapport d'analyse formate."""
    ...

def afficher_frequences(frequences):
    """Affiche un mini-histogramme en barres ASCII des frequences.

    Exemple d'affichage :
      le       : ############ (12)
      de       : ######### (9)
      python   : ###### (6)
    """
    ...
```

---

### Module `main.py` — Menu interactif

```python
# main.py
from traitement import (compter_mots, compter_caracteres,
                         mots_les_plus_frequents, extraire_debut_fin,
                         est_palindrome_phrase, inverser_mots)
from affichage import afficher_stats, afficher_frequences

def menu():
    """Affiche un menu et retourne le choix de l'utilisateur."""
    print("\n=== ANALYSEUR DE TEXTE ===")
    print("1. Analyser un texte saisi")
    print("2. Analyser un fichier texte")
    print("3. Verifier un palindrome")
    print("4. Inverser les mots d'un texte")
    print("0. Quitter")
    return input("Votre choix : ").strip()


if __name__ == "__main__":
    while True:
        choix = menu()
        try:
            if choix == "0":
                print("Au revoir !")
                break
            elif choix == "1":
                texte = input("Entrez votre texte : ")
                if not texte.strip():
                    raise ValueError("Le texte ne peut pas etre vide.")
                # ... appels aux fonctions de traitement
            elif choix == "2":
                chemin = input("Chemin du fichier : ")
                # ... lecture et analyse du fichier
            elif choix == "3":
                phrase = input("Entrez une phrase : ")
                # ... verification palindrome
            elif choix == "4":
                texte = input("Entrez votre texte : ")
                # ... inversion des mots
            else:
                print("Choix invalide.")
        except ValueError as e:
            print(f"Erreur : {e}")
        except FileNotFoundError:
            print("Fichier introuvable.")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
```

---

## Correction guidee — `traitement.py` complet

```python
# traitement.py — Solution complete

def compter_mots(texte):
    if not isinstance(texte, str):
        raise TypeError("Le texte doit etre une chaine de caracteres.")
    return len(texte.split())


def compter_caracteres(texte, ignorer_espaces=True):
    if not isinstance(texte, str):
        raise TypeError("Le texte doit etre une chaine de caracteres.")
    if ignorer_espaces:
        return len(texte.replace(" ", ""))
    return len(texte)


def mots_les_plus_frequents(texte, n=5):
    if not texte.strip():
        raise ValueError("Le texte est vide.")

    # Nettoyage : minuscules et ponctuation retiree
    mots = texte.lower().split()
    mots_nettoyes = ["".join(c for c in mot if c.isalpha()) for mot in mots]
    mots_nettoyes = [m for m in mots_nettoyes if m]   # Retirer les chaines vides

    # Comptage des occurrences
    frequences = {}
    for mot in mots_nettoyes:
        frequences[mot] = frequences.get(mot, 0) + 1

    # Tri decroissant et slicing pour les n premiers
    tries = sorted(frequences.items(), key=lambda x: x[1], reverse=True)
    return tries[:n]   # Slicing : garder uniquement les n premiers


def extraire_debut_fin(texte, nb_mots=10):
    if not texte.strip():
        raise ValueError("Le texte est vide.")
    mots = texte.split()
    if len(mots) < nb_mots * 2:
        nb_mots = len(mots) // 2
    debut = mots[:nb_mots]       # Slicing debut
    fin   = mots[-nb_mots:]      # Slicing fin (indice negatif)
    return debut, fin


def est_palindrome_phrase(phrase):
    if not isinstance(phrase, str):
        raise TypeError("La phrase doit etre une chaine.")
    propre = "".join(c.lower() for c in phrase if c.isalpha())
    return propre == propre[::-1]   # Slicing inverse


def inverser_mots(texte):
    if not texte.strip():
        raise ValueError("Le texte est vide.")
    mots = texte.split()
    return " ".join(mots[::-1])     # Slicing inverse sur liste
```

---

## Verification — Projet de synthese

| Critere | Description |
|---|---|
| Slicing | Utilise dans au moins 3 fonctions differentes |
| try/except | Chaque fonction valide ses parametres |
| Modules separes | 3 fichiers avec responsabilites distinctes |
| Bloc principal protege | `if __name__ == "__main__"` present dans main.py |
| Fonctionnalite | L'application tourne sans erreur sur un texte test |

---

# Recapitulatif General

## Slicing — Antisèche

```python
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

s[2:5]       # [2, 3, 4]                       de l'indice 2 a 4 (5 exclu)
s[:4]        # [0, 1, 2, 3]                    du debut a l'indice 3
s[6:]        # [6, 7, 8, 9]                    de l'indice 6 a la fin
s[:]         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] copie complete
s[-3:]       # [7, 8, 9]                       3 derniers elements
s[:-3]       # [0, 1, 2, 3, 4, 5, 6]           tout sauf les 3 derniers
s[::2]       # [0, 2, 4, 6, 8]                 un sur deux
s[::-1]      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] inverse
s[1:8:2]     # [1, 3, 5, 7]                    de 1 a 7, un sur deux
```

---

## Gestion des erreurs — Antisèche

```python
try:
    # Code a surveiller
    ...
except TypeError as e:
    # Erreur de type — e contient le message
    ...
except (ValueError, KeyError):
    # Plusieurs types d'erreurs en une seule clause
    ...
except Exception as e:
    # Attrape toutes les autres erreurs (filet de securite)
    ...
else:
    # Execute UNIQUEMENT si aucune erreur
    ...
finally:
    # Execute TOUJOURS (nettoyage)
    ...

raise ValueError("message")     # Lever une erreur manuellement

class MonErreur(Exception):     # Creer une exception personnalisee
    pass
```

---

## Modularite — Antisèche

```python
# Creer un module : simplement un fichier .py avec des fonctions

# Importer un module entier
import calculs
calculs.moyenne([14, 16])

# Importer des fonctions specifiques
from calculs import moyenne, mention

# Importer avec alias
import calculs as calc

# Proteger le code d'execution directe
if __name__ == "__main__":
    ...   # Ne s'execute que si on lance ce fichier
```

---

## Pour aller plus loin

### Niveau intermediaire

1. **Slicing sur des tableaux 2D** — avec la bibliotheque `numpy` : `tableau[1:3, 0:2]`
2. **Exceptions enchainees** — `raise NouvelleErreur("...") from erreur_originale`
3. **Modules standard a explorer** — `collections`, `itertools`, `pathlib`
4. **Tests unitaires** — `unittest` : verifier automatiquement que vos fonctions fonctionnent

### Niveau avance

5. **Packages** — organiser des modules en dossiers avec `__init__.py`
6. **Decorateurs** — `@property`, creer ses propres decorateurs pour gerer les erreurs
7. **Context managers** — le mot-cle `with` en profondeur, creer les siens avec `__enter__` et `__exit__`
8. **Logging** — remplacer les `print()` par le module `logging` pour tracer les erreurs en production

---

> **Ce que vous avez maitrise dans cet atelier**
>
> Le **slicing** permet de manipuler les sequences avec precision et concision — c'est l'une des forces expressives de Python.
> La **gestion des erreurs** est ce qui separe un code qui fonctionne en local d'un code qui resiste au monde reel.
> La **modularite** est ce qui separe un script jetable d'un projet maintenable et evolutif.
>
> Ces trois piliers travaillent ensemble : des fonctions decoupees en modules, qui valident leurs donnees via les exceptions, et qui manipulent les sequences avec elegance grace au slicing.