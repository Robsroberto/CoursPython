<div class="bandeau"><img src="../images/python-bandeau.png" alt="Python" /></div>

# Atelier 1 : un premier notebook reproductible sur les prix des marchés

<p class="auteur">Par <strong>Robert DIASSÉ</strong>, Ingénieur Logiciel et Data</p>

> **Cours** : Python pour la science des données · **Chapitre** : 1, L'environnement de travail · **Version** : 2026-10-18

## Avant de commencer

| | |
|---|---|
| **Ce que vous allez construire** | Un notebook propre, commenté et reproductible, qui charge le jeu de données des prix des marchés et en fait la première description : taille, période, marchés, régions, denrées |
| **Durée** | 🟢 Débutant : 3 h · 🔵 Standard : 2 h · 🟣 Expert : 1 h 30 (sans les défis) |
| **Prérequis** | Avoir lu le chapitre 1 ; un compte Google ; un compte GitHub |
| **Fichiers fournis** | `wfp_food_prices_sen.csv` (les relevés de prix) |
| **Rendu** | Le notebook `atelier1_prix_marches.ipynb`, dans votre dépôt GitHub `prix-marches`, avec l'étiquette `atelier-1` |

> 📍 **Point de départ : un nouveau notebook.** Le dépôt GitHub `prix-marches` que vous créez ici accueillera **tous** les notebooks du cours.
>
> **La suite du fil rouge** : atelier 1 (décrire les données) → atelier 2 (les lire en Python pur et rejeter les lignes abîmées) → ateliers 3 à 5 (calculer, nettoyer, agréger) → mini-projet (l'analyse complète).

### Comment travailler

L'atelier est découpé en **8 étapes** (0 à 7). Chaque étape suit le même plan : 🎯 **Objectif** · 🛠️ **A faire** · 🔎 **A chercher** · 💡 **A comprendre** (répondez **dans une cellule de texte** du notebook) · ✅ **Vérification** · ➕ **Vous pouvez ajouter** (facultatif).

**Deux règles pour tout l'atelier**

1. **Une cellule de texte avant chaque cellule de code** : ce que vous allez faire.
2. **Une cellule de texte après chaque résultat important** : ce que vous observez.

---

## Étape 0 : le notebook et ses données (15 min)

🎯 **Objectif** : un notebook Colab nommé `atelier1_prix_marches.ipynb`, avec le fichier de données importé.

🛠️ **A faire**

1. Dans Colab : **Fichier > Nouveau notebook** ; renommez-le `atelier1_prix_marches.ipynb`.
2. Importez le fichier fourni `wfp_food_prices_sen.csv` dans le panneau **Fichiers** (chapitre 1, section 4).

💡 **A comprendre**

- Où votre notebook est-il enregistré ? Et le fichier de données ? Que deviendra le fichier demain ?

✅ **Vérification** : le fichier apparaît dans le panneau Fichiers.

---

## Étape 1 : l'en-tête (15 min)

🎯 **Objectif** : une première cellule de **texte** qui présente le notebook.

🛠️ **A faire**

1. Écrivez, en Markdown : un titre de niveau 1 ; une ligne avec votre nom et la date (en gras « Auteur » et « Date ») ; l'**objectif** du notebook ; la **source** des données et leur **licence** (« World Food Programme, via Humanitarian Data Exchange (HDX), jeu "Senegal - Food Prices", licence CC BY-IGO »).

🔎 **A chercher** : chapitre 1, sections 6 et 7 ; pour comprendre la licence : « CC BY-IGO » (que doit faire celui qui réutilise les données ?).

✅ **Vérification** : la cellule s'affiche mise en forme quand vous l'exécutez.

---

## Étape 2 : les imports et les versions (10 min)

🎯 **Objectif** : la première cellule de code importe tout ce dont le notebook a besoin et affiche les versions.

🛠️ **A faire**

1. Importez `sys` et `pandas` (avec l'abréviation conventionnelle).
2. Affichez sur une ligne la version de Python (seulement le numéro : `sys.version.split()[0]`) et celle de pandas.

💡 **A comprendre**

- Que fait `.split()[0]` sur le texte de `sys.version` ?
- Pourquoi noter les versions au début d'un notebook ?

✅ **Vérification** : une ligne comme `Python 3.12.13 | pandas 3.0.6` s'affiche (vos numéros peuvent différer).

---

## Étape 3 : charger les données (15 min)

🎯 **Objectif** : les relevés sont chargés dans un DataFrame `releves`, et leur taille est affichée.

🛠️ **A faire**

1. Rangez le nom du fichier dans une variable `FICHIER` (règle 4 de la section 7).
2. Chargez-le avec `pd.read_csv(FICHIER)` dans `releves`.
3. Affichez : `Lignes : ... | colonnes : ...` avec `releves.shape[0]` et `releves.shape[1]`.

💡 **A comprendre**

- Que contient `releves.shape` ? Que désignent `[0]` et `[1]` ?

✅ **Vérification** : `Lignes : 52021 | colonnes : 16`.

---

## Étape 4 : regarder les données (20 min)

🎯 **Objectif** : voir le début et la fin du tableau, et comprendre chaque colonne.

🛠️ **A faire**

1. Affichez les 5 premières lignes (`releves.head()`) et les 2 dernières (`releves.tail(2)`).
2. Dans une cellule de texte, faites un tableau Markdown des colonnes `date`, `admin1`, `market`, `commodity`, `unit`, `currency` et `price`, avec ce que chacune contient, **en français** (aidez-vous du tableau de la section 8 du chapitre).

🔎 **A chercher** : « Markdown tableau » (la syntaxe avec des `|`).

💡 **A comprendre**

- Quel est le dernier relevé du fichier : quelle date, quel marché, quelle denrée, quel prix ?
- Les numéros de la colonne de gauche vont-ils de 1 à 52 021 ?

✅ **Vérification** : la dernière ligne est un relevé du 2026-07-15 au marché Saint-Maur (Ziguinchor), pour des pastèques (*Watermelons*), à 600 F le kilo ; son index est 52020.

---

## Étape 5 : décrire le jeu de données (30 min)

🎯 **Objectif** : répondre, avec du code puis par écrit, aux questions que l'on se pose toujours face à un nouveau jeu de données.

Voici quatre outils de pandas que vous étudierez au chapitre 4. Utilisez-les tels quels :

| Morceau | Ce qu'il veut dire |
|---|---|
| `releves["date"]` | La **colonne** `date` (on la désigne par son nom, entre crochets) |
| `.min()`, `.max()` | La plus petite et la plus grande valeur de la colonne. Les dates sont écrites `AAAA-MM-JJ` : l'ordre alphabétique est aussi l'ordre chronologique |
| `.nunique()` | Le nombre de valeurs **différentes** |
| `.unique().tolist()` | La liste des valeurs différentes |
| `.value_counts().head(5)` | Les 5 valeurs les plus fréquentes, avec leur nombre d'apparitions |

🛠️ **A faire** : une cellule de code par question, puis la réponse dans une cellule de texte.

1. Quelle **période** couvrent les relevés ?
2. Combien de **marchés** différents ? Combien de **régions** ? Lesquelles (triées avec `sorted`) ?
3. Quelles sont les **5 denrées** les plus relevées ?
4. Combien de **monnaies**, d'**unités** et de **types de prix** différents ? Lesquels ?

💡 **A comprendre**

- Pourquoi la question 4 est-elle importante avant de comparer des prix ? Que faudrait-il faire si une partie des prix était en kilos et une autre en sacs de 50 kg ?
- Une unité est `Head` (« par tête ») : à quelle sorte de denrée correspond-elle, à votre avis ? Notez votre hypothèse : vous la vérifierez au chapitre 4.

✅ **Vérification** : du 2000-01-15 au 2026-07-15 ; 67 marchés ; 14 régions (de Dakar à Ziguinchor) ; Millet 9484, Rice (imported) 9308, Maize (local) 7489, Sorghum 6689, Maize (imported) 4836 ; une seule monnaie (`XOF`), deux unités (`KG`, `Head`), un seul type de prix (`Retail`).

---

## Étape 6 : une première question à vous (20 min)

🎯 **Objectif** : poser et traiter une question simple.

🛠️ **A faire**

1. Le marché de Tilène (`"Tilene"`) est un grand marché de Dakar. Combien de relevés y ont été faits ? Utilisez `releves[releves["market"] == "Tilene"].shape[0]` (vous comprendrez ce filtre au chapitre 4 : il garde seulement les lignes où la condition est vraie).
2. Choisissez un autre marché de votre région (`releves["market"].unique().tolist()` donne la liste) et faites de même.
3. Écrivez **trois questions** que vous aimeriez poser à ces données d'ici la fin du cours (par exemple sur le riz, le mil, une région, une année). Vous y répondrez dans le mini-projet.

✅ **Vérification** : 1502 relevés à Tilène.

---

## Étape 7 : reproductible, puis sur GitHub (20 min)

🎯 **Objectif** : un notebook qui passe « Redémarrer et tout exécuter », publié sur GitHub.

🛠️ **A faire**

1. Relisez votre notebook avec la liste des 8 règles de la section 7 du chapitre. Ajoutez une cellule de texte finale « Conclusions » : en 4 ou 5 phrases, ce que vous savez maintenant de ces données.
2. **Exécution > Redémarrer la session et tout exécuter** : aucune erreur ne doit apparaître.
3. Créez sur GitHub un dépôt `prix-marches` (avec un fichier README). Dans Colab : **Fichier > Enregistrer une copie dans GitHub**, choisissez le dépôt, et validez.
4. Sur la page GitHub du dépôt, créez l'étiquette `atelier-1` : bouton **Releases** (à droite), puis **Create a new release**, tapez `atelier-1` dans *Choose a tag*, puis **Create new tag** et **Publish release**.

💡 **A comprendre**

- Le fichier de données doit-il être envoyé sur GitHub ? (Pensez à sa taille, et à la licence : que faut-il écrire dans le README ?)

✅ **Vérification** : sur GitHub, le notebook s'affiche avec ses résultats ; l'étiquette `atelier-1` existe.

---

## 🏆 Défis (facultatifs)

1. **La table des marchés.** Chargez aussi `wfp_markets_sen.csv` (si l'enseignant vous le fournit) : combien de marchés contient-elle ? Est-ce le même nombre que dans les relevés ? Formulez une hypothèse.
2. **Le prix le plus élevé.** Avec `releves["price"].max()`, trouvez le prix le plus élevé du fichier. Puis trouvez la ligne correspondante (cherchez « pandas idxmax »). Ce prix vous paraît-il plausible pour un kilo ?
3. **Le notebook en local.** Refaites l'atelier dans JupyterLab sur votre ordinateur, dans un environnement virtuel, avec un `requirements.txt` dans le dépôt.

---

## Grille d'autoévaluation

| Je sais... | Oui | Pas encore |
|---|---|---|
| créer un notebook dans Colab, y importer un fichier, exécuter des cellules | ☐ | ☐ |
| écrire du texte en Markdown (titres, gras, listes, tableau) | ☐ | ☐ |
| expliquer pourquoi l'ordre d'exécution des cellules compte | ☐ | ☐ |
| charger un CSV avec pandas et afficher sa taille, son début et sa fin | ☐ | ☐ |
| décrire un nouveau jeu de données (période, valeurs différentes, unités) | ☐ | ☐ |
| rendre un notebook reproductible et le vérifier avec « Redémarrer et tout exécuter » | ☐ | ☐ |
| publier un notebook sur GitHub et poser une étiquette | ☐ | ☐ |
