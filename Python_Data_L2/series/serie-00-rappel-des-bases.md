<div class="bandeau"><img src="../images/python-bandeau.png" alt="Python" /></div>

# Série 0 : rappel des bases de Python, jusqu'aux collections

<p class="auteur">Par <strong>Robert DIASSÉ</strong>, Ingénieur Logiciel et Data</p>

> **Thèmes** : types et opérateurs, saisie et affichage, conditions, boucles, chaînes, listes, tuples, ensembles, dictionnaires · **Version** : 2026-10-19

## Avant de commencer

| | |
|---|---|
| **Objectif** | Vérifier, en début d'année, que les bases de Python de L1 sont solides, avant d'aller plus loin |
| **Contenu** | 17 exercices en 5 parties, du plus simple (★) au plus complet (★★★) |
| **Durée** | Environ 4 h ; 🟢 Débutant : les ★ et les ★★ ; 🟣 Expert : les ★★★ en priorité |
| **Matériel** | Python 3.12 ou plus récent, VS Code (ou un notebook) |

**Comment travailler** : un fichier par exercice. Pour les exercices « Que produit ce programme ? », écrivez votre réponse **sur papier avant** de lancer le programme, puis comparez : chaque écart est une notion à revoir. Pour les autres, testez **toutes** les valeurs du tableau d'exemples.

---

## Partie 1 : types, opérateurs, saisie et affichage

**Exercice 1 ★ : que produit ce programme ?** Écrivez ligne par ligne ce qui s'affiche. Attention aux pièges des lignes 5 et 6.

```python
print(7 // 2, 7 % 2, 2 ** 10, 7 / 2)
print(type(6 / 3), type(6 // 3))
print(int("12") + 3, "12" + "3")
print("ab" * 3, str(4) + "2")
print(round(2.5), round(3.5), round(2.675, 2))
print(bool(""), bool("0"), bool(0), bool([]))
print(10 > 3 and 2 > 5, not 10 > 3 or 2 < 5)
x = 5
x += 3
x *= 2
print(x)
```

**Exercice 2 ★ : la température.** Lire une température en degrés Celsius (avec un point **ou** une virgule) et l'afficher en Fahrenheit (F = C × 9 / 5 + 32), avec une f-string : 1 décimale pour les °C, 2 pour les °F.

| Saisie | `36,6` | `-40` |
|---|---|---|
| Affichage | `36.6 °C = 97.88 °F` | `-40.0 °C = -40.00 °F` |

**Exercice 3 ★ : la facture.** Lire un prix unitaire et une quantité (des entiers, en F). Si le total dépasse 50 000 F, une remise de 10 % est accordée (en nombre entier de francs). Afficher le total brut, la remise et le montant à payer, alignés.

| Saisie | 1500 et 40 | 2500 et 10 |
|---|---|---|
| A payer | Total 60 000, remise 6 000, **54 000 F** | Total 25 000, remise 0, **25 000 F** |

## Partie 2 : les conditions

**Exercice 4 ★ : la mention.** Lire une note sur 20 et afficher la mention : 16 et plus « Très bien », 14 « Bien », 12 « Assez bien », 10 « Passable », moins de 10 « Ajourné », et « Note invalide » hors de 0 à 20. Tests : 15,5 → Bien ; 9,99 → Ajourné ; 21 → Note invalide. Testez aussi 16, 14, 12 et 10.

**Exercice 5 ★★ : la facture d'électricité par tranches.** Une compagnie (imaginaire) facture l'électricité par tranches : les 150 premiers kWh à 90 F, de 151 à 250 kWh à 105 F, au-delà de 250 kWh à 120 F. Chaque tranche n'est facturée **que** pour les kWh qu'elle contient.

| Consommation | 120 kWh | 200 kWh | 310 kWh |
|---|---|---|---|
| Montant | 10 800 F | 18 750 F | 31 200 F |

Pour 200 kWh : 150 × 90 + 50 × 105. Écrivez le calcul de 310 kWh à la main avant de coder.

## Partie 3 : les boucles

**Exercice 6 ★ : jusqu'au zéro.** Lire des entiers jusqu'à ce que l'utilisateur tape 0 (le 0 ne compte pas), puis afficher leur nombre, leur somme et leur moyenne (2 décimales). Si le premier nombre est 0, afficher « Aucune valeur saisie ». Avec 12, 7, -4, 15, 0 : `4 valeurs, somme 30, moyenne 7.50`. Quelle boucle convient, `for` ou `while` ? Pourquoi ?

**Exercice 7 ★★ : les nombres premiers.** Écrivez la fonction `est_premier(n)` (un nombre premier a exactement deux diviseurs, 1 et lui-même ; il suffit de tester les diviseurs jusqu'à la racine carrée de `n`). Testez : 1 → False, 2 → True, 91 → False (91 = 7 × 13), 97 → True. Puis construisez la liste des premiers inférieurs à 50 : il y en a 15, de 2 à 47.

**Exercice 8 ★★ : les chiffres d'un nombre.** Lire un entier positif et afficher, **sans le transformer en chaîne**, la somme de ses chiffres et le nombre écrit à l'envers (avec `% 10` et `// 10` dans une boucle `while`). Avec 4072 : somme 13, à l'envers 2704.

**Exercice 9 ★★ : que produit ce programme ?**

```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        if i == 3:
            break
        print(i, j)
print("fin")
k = 10
while k > 0:
    k -= 3
print(k)
```

## Partie 4 : les chaînes de caractères

**Exercice 10 ★ : que produit ce programme ?**

```python
texte = "Programmation"
print(len(texte), texte.upper(), texte.lower())
print(texte[0], texte[-1], texte[3:7], texte[:4], texte[-5:])
print(texte[::-1], texte[::2])
print(texte.count("m"), texte.find("gram"), "mm" in texte)
print(texte.replace("m", "M", 1))
```

Puis ajoutez une ligne qui compte les voyelles du texte (réponse : 5).

**Exercice 11 ★★ : nettoyer un nom.** A partir de `nom = "  awa   ndiaye fall "` (espaces en trop, minuscules), obtenez `"Awa Ndiaye Fall"` et les initiales `"A.N.F."`. Indices : `split()` sans argument coupe sur **tous** les espaces, même multiples ; `capitalize()` ; `" ".join(...)`.

## Partie 5 : les collections

**Exercice 12 ★ : les listes.** A partir de `notes = [12, 8.5, 15, 10, 6]` : ajoutez 17 à la fin, 9 au début, retirez 8,5, puis affichez la liste, sa longueur, le minimum, le maximum, la somme et la moyenne (2 décimales). Triez-la, affichez les 3 plus petites et les 2 plus grandes (tranches), la liste des notes ≥ 10 (une **compréhension de liste**) et la liste triée dans l'ordre décroissant **sans modifier** `notes`.

| Résultats attendus | |
|---|---|
| Après les modifications | `[9, 12, 15, 10, 6, 17]` ; 6 notes, min 6, max 17, somme 69, moyenne 11.50 |
| Après le tri | `[6, 9, 10, 12, 15, 17]` ; `[6, 9, 10]` et `[15, 17]` ; admis `[10, 12, 15, 17]` ; décroissant `[17, 15, 12, 10, 9, 6]` |

Quelle est la différence entre `notes.sort()` et `sorted(notes)` ?

**Exercice 13 ★ : les tuples.** Que produit ce programme ? Expliquez la dernière ligne.

```python
point = (14.69, -17.44)
lat, lon = point
print(lat, lon)
a, b = 3, 8
a, b = b, a
print(a, b)
semaine = ("lun", "mar", "mer", "jeu", "ven")
print(semaine[1:3], semaine.index("jeu"), len(semaine))
semaine[0] = "dim"
```

**Exercice 14 ★★ : les ensembles.** Les inscrits au club de football : `{"Awa", "Moussa", "Fatou", "Ibou", "Moussa"}` ; au club de théâtre : `{"Fatou", "Khady", "Ibou", "Lamine"}`. Affichez (triés) : le nombre d'inscrits au football (pourquoi 4 et non 5 ?), ceux qui sont dans les deux clubs, dans au moins un club, seulement au football, dans un seul des deux clubs. Testez si Khady est au football et au théâtre.

| Attendu | |
|---|---|
| Les deux clubs | `['Fatou', 'Ibou']` |
| Au moins un | `['Awa', 'Fatou', 'Ibou', 'Khady', 'Lamine', 'Moussa']` |
| Seulement au football | `['Awa', 'Moussa']` |
| Un seul des deux | `['Awa', 'Khady', 'Lamine', 'Moussa']` |

**Exercice 15 ★★ : le stock de la boutique.** Avec `stock = {"riz": 40, "huile": 12, "sucre": 25}` et `prix = {"riz": 450, "huile": 1300, "sucre": 700}` : ajoutez le lait (8 unités à 3200 F), retirez 5 sacs de riz, supprimez le sucre. Affichez le stock, la quantité de sucre avec `get` (sans erreur, puis avec 0 par défaut), une ligne alignée par produit (`riz     35 x   450 F`) et la valeur totale du stock. Attendu : `{'riz': 35, 'huile': 12, 'lait': 8}`, `None 0`, valeur **56 950 F**. Que se passerait-il avec `stock["sucre"]` ?

**Exercice 16 ★★★ : compter les mots.** Pour le texte `"le riz le mil et le maïs sont des céréales le mil pousse ici"`, construisez un dictionnaire mot → nombre d'apparitions, trouvez le mot le plus fréquent, puis les 3 mots les plus fréquents (tri des paires `(mot, nombre)` par nombre décroissant, avec `sorted` et `key`). Attendu : « le » 4 fois ; `[('le', 4), ('mil', 2), ('riz', 1)]`. Pourquoi « riz » et pas « et », qui apparaît aussi une fois ?

**Exercice 17 ★★★ : le carnet de notes.** Un carnet est un dictionnaire nom → liste de notes : `{"Awa": [12, 15, 14], "Moussa": [9, 11, 8], "Fatou": [17, 16, 18]}`.
1. Écrivez `moyenne(notes)` et `ajouter_note(carnet, nom, note)`, qui refuse une note hors de 0 à 20 (avec un message) et crée la liste si l'étudiant n'existe pas encore (cherchez `setdefault`).
2. Ajoutez 13 à Moussa, 10 à Ibou (nouveau), 25 à Awa (refusée).
3. Construisez le dictionnaire des moyennes arrondies à 2 décimales (une **compréhension de dictionnaire**), le classement par moyenne décroissante avec le rang (`enumerate(..., start=1)`) et la liste des admis (moyenne ≥ 10).

Attendu : `{'Awa': 13.67, 'Moussa': 10.25, 'Fatou': 17.0, 'Ibou': 10.0}` ; classement 1 Fatou, 2 Awa, 3 Moussa, 4 Ibou ; tous admis.

---

## Grille d'autoévaluation

| Je sais... | Oui | Pas encore |
|---|---|---|
| prévoir le résultat de `//`, `%`, `**`, `round` et des conversions | ☐ | ☐ |
| écrire une suite de `if` / `elif` / `else` et la tester aux valeurs limites | ☐ | ☐ |
| choisir entre `for` et `while`, utiliser `break` et `continue` | ☐ | ☐ |
| découper une chaîne avec les tranches et ses méthodes | ☐ | ☐ |
| modifier, trier et filtrer une liste | ☐ | ☐ |
| expliquer la différence entre liste, tuple, ensemble et dictionnaire | ☐ | ☐ |
| parcourir un dictionnaire et compter avec `get` | ☐ | ☐ |
