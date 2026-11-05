<div class="bandeau"><img src="../images/python-bandeau.png" alt="Python" /></div>

# Atelier 5 : les indicateurs par région et par denrée

<p class="auteur">Par <strong>Robert DIASSÉ</strong>, Ingénieur Logiciel et Data</p>

> **Cours** : Python pour la science des données · **Chapitre** : 5, Agréger et restructurer avec pandas · **Version** : 2026-10-23

## Avant de commencer

| | |
|---|---|
| **Ce que vous allez construire** | Un notebook qui calcule, à partir des relevés du PAM, les indicateurs de prix de 2025 par région et par denrée : un résumé par région, une grille des prix, un indice de cherté, l'évolution depuis 2019, l'effet de la soudure et la couverture des marchés ; puis un classeur Excel de plusieurs feuilles et une courte note |
| **Durée** | 🟢 Débutant : 4 h · 🔵 Standard : 3 h · 🟣 Expert : 2 h (sans les défis) |
| **Prérequis** | Avoir lu le chapitre 5 ; votre dépôt `prix-marches` |
| **Fichiers fournis** | Le notebook de départ ; les relevés et le fichier des marchés du PAM (déjà fournis) |
| **Rendu** | Le notebook `atelier5_indicateurs.ipynb` et le classeur `indicateurs_2025.xlsx` dans votre dépôt `prix-marches`, avec l'étiquette `atelier-5` |

**Le scénario.** Le Commissariat à la sécurité alimentaire prépare sa note annuelle sur les prix. Il vous demande des réponses chiffrées à six questions : quelles régions sont suivies et comment ; où chaque denrée est la plus chère ; quelles régions sont globalement chères ; comment les céréales ont évolué depuis 2019 ; où la soudure fait le plus monter le mil ; quels marchés ne sont plus suivis. Chaque réponse doit être **vérifiable** : on doit pouvoir refaire vos calculs.

> 📍 **Point de départ** : le notebook de départ fourni, une section par étape. Envoyez-y les deux fichiers du PAM.

### Comment travailler

Mêmes règles que les ateliers précédents. **Règle de cet atelier** : chaque tableau d'indicateurs est suivi d'**une phrase** qui dit ce qu'il montre, dans une cellule de texte, avec les chiffres. Un tableau sans phrase ne compte pas.

---

## Étape 1 : préparer les relevés et les noms français (25 min)

🎯 **Objectif** : un tableau de travail propre, avec des noms de denrées en français.

🛠️ **A faire**

1. Chargez les relevés, gardez les prix au kilo, renommez `admin1`, `market`, `commodity` et `price` en `region`, `marche`, `denree`, `prix` ; convertissez la date ; ajoutez les colonnes `annee` et `mois` (`.dt.month`).
2. Écrivez une table de correspondance `noms` pour les **huit** denrées de base, avec trois colonnes : `denree` (le nom du PAM), `nom_fr` et `groupe`.

| `denree` | `nom_fr` | `groupe` |
|---|---|---|
| Millet | Mil | céréale |
| Sorghum | Sorgho | céréale |
| Maize (local) | Maïs local | céréale |
| Rice (imported) | Riz importé | céréale |
| Rice (local) | Riz local | céréale |
| Beans (niebe) | Niébé | légumineuse |
| Groundnuts (shelled) | Arachide décortiquée | oléagineux |
| Groundnuts (unshelled) | Arachide en coque | oléagineux |

3. Joignez-la aux relevés dans `base`, avec `validate="many_to_one"`. Comptez les lignes avant et après, et le nombre de relevés par denrée.
4. Gardez l'année 2025 dans `an` (avec `.copy()`), et affichez sa première et sa dernière date.

✅ **Vérification**

```text
51854 -> 42856
2931 relevés en 2025 ; 2025-01-15 au 2025-12-15
```

Le mil a 9 484 relevés, l'arachide en coque 1 667.

💡 **A comprendre** : quelles lignes ont été retirées par la jointure, et pourquoi est-ce voulu ici ? Que se passerait-il si vous écriviez deux fois `Millet` dans la table `noms` sans `validate` ?

---

## Étape 2 : le résumé par région (20 min)

🎯 **Objectif** : savoir **sur quoi** reposent les chiffres de chaque région.

🛠️ **A faire** : avec une agrégation nommée sur `an`, une ligne par région : `releves` (nombre de relevés), `marches` (marchés différents), `denrees` (denrées différentes), `premier` et `dernier` (première et dernière date). Triez par nombre de relevés.

✅ **Vérification** : 14 régions ; Sédhiou a le moins de relevés (38, un seul marché), Fatick le plus (351, six marchés).

```text
             releves  marches  denrees    premier    dernier
region                                                      
Sedhiou           38        1        8 2025-01-15 2025-11-15
Kaffrine          88        3        7 2025-01-15 2025-08-15
Saint Louis      126        2        8 2025-01-15 2025-11-15
...
```

💡 **A comprendre** : regardez la ligne de Kaffrine. Quelles **deux** particularités allez-vous devoir garder en tête pour la suite ?

---

## Étape 3 : la grille des prix (30 min)

🎯 **Objectif** : le prix médian de chaque denrée dans chaque région, et les régions extrêmes.

🛠️ **A faire**

1. Avec `pivot_table` sur `an` : une ligne par région, une colonne par `nom_fr`, la **médiane** des prix dans chaque case. Affichez-la arrondie.
2. Construisez un tableau `extremes`, une ligne par denrée, avec quatre colonnes : la région la plus chère (`idxmax()`), son prix (`max()`), la moins chère (`idxmin()`), son prix (`min()`) ; ajoutez `rapport`, le prix maximal divisé par le prix minimal. Triez par rapport décroissant.
3. Combien de cases sont vides, et lesquelles ?

<details>
<summary>💡 Indice : construire `extremes` d'un coup</summary>

`grille.idxmax()` donne une `Series` (une région par denrée) ; `grille.max()` aussi (un prix par denrée). `pd.DataFrame({"plus_chere": grille.idxmax(), "prix_max": grille.max(), ...})` les réunit en colonnes, alignées sur la denrée.

</details>

✅ **Vérification**

```text
                      plus_chere  prix_max moins_chere  prix_min  rapport
nom_fr                                                                   
Arachide en coque          Dakar     975.0    Kedougou     305.0     3.20
Mil                     Kedougou     425.0    Kaffrine     200.0     2.12
Maïs local            Ziguinchor     400.0    Kaffrine     200.0     2.00
Niébé                    Sedhiou    1200.0    Kaffrine     600.0     2.00
Sorgho                Ziguinchor     500.0    Kaffrine     250.0     2.00
Riz local                  Kolda     600.0     Kaolack     350.0     1.71
Arachide décortiquée    Kedougou    1000.0    Kaffrine     700.0     1.43
Riz importé                Dakar     450.0       Kolda     350.0     1.29
```

Une seule case vide : le riz local à Kaffrine.

💡 **A comprendre**

1. Regardez la colonne « Arachide décortiquée » de la grille : Kédougou est-elle **la seule** région à 1 000 F ? Et Kolda, la seule à 350 F pour le riz importé ? Que fait `idxmax` en cas d'égalité, et que devez-vous écrire dans votre phrase ?
2. Le riz importé a le plus petit rapport (1,29), le mil un des plus grands (2,12). Proposez une explication : d'où vient le riz importé, d'où vient le mil ?
3. A Dakar, l'arachide **en coque** (975 F) serait plus chère que l'arachide **décortiquée** (850 F). Est-ce plausible ? Que faites-vous d'un tel chiffre dans une note officielle ? (On ne le corrige pas soi-même : on le **signale**.)

---

## Étape 4 : l'indice de cherté (30 min)

🎯 **Objectif** : comparer les régions **honnêtement**, denrée par denrée et mois par mois.

Comparer les médianes de tous les prix d'une région n'a pas de sens (une région qui relève beaucoup d'arachide paraîtrait chère). On construit donc un **indice** : chaque relevé est comparé à la médiane nationale de **la même denrée le même mois** ; 100 = le prix national, 120 = 20 % plus cher.

🛠️ **A faire**

1. Colonne `reference` : la médiane des prix du groupe (`nom_fr`, `date`), recopiée sur chaque ligne avec `transform`.
2. Colonne `indice` : `prix / reference * 100`.
3. La moyenne de l'indice par région, arrondie à 0,1, triée de la plus chère à la moins chère.
4. Contrôle : la médiane de l'indice sur toutes les lignes doit valoir 100.

✅ **Vérification**

```text
region
Ziguinchor     129.6
Dakar          120.8
Kedougou       116.0
Sedhiou        115.5
Matam          113.2
Thies          105.7
Saint Louis    103.8
Diourbel       100.8
Tambacounda     99.6
Kolda           98.2
Louga           97.8
Fatick          96.1
Kaolack         86.0
Kaffrine        83.7
```

💡 **A comprendre**

1. Pourquoi `transform` et pas `agg` pour la colonne `reference` ?
2. Les quatre régions les plus chères sont-elles des régions de production ou d'éloignement ? Et les deux moins chères (Kaolack, Kaffrine) ? Situez-les sur une carte du Sénégal.
3. L'indice de Sédhiou repose sur combien de relevés (étape 2) ? Quelle prudence en tirer ?

---

## Étape 5 : l'évolution depuis 2019 (25 min)

🎯 **Objectif** : comment le prix des céréales a évolué en sept ans.

🛠️ **A faire**

1. Sur `base`, gardez les céréales (`groupe == "céréale"`) de 2019 à 2025 (`between`). Tableau croisé : une ligne par année, une colonne par céréale, la médiane des prix.
2. Pour chaque céréale : la hausse en % de 2019 à 2025 (`evolution.loc[2025] / evolution.loc[2019]`), et l'année la plus chère (`idxmax()`). Réunissez les deux `Series` côte à côte avec `pd.concat(..., axis=1)`.

✅ **Vérification**

```text
nom_fr  Maïs local    Mil  Riz importé  Riz local  Sorgho
annee                                                    
2019         210.0  225.0        300.0      300.0   250.0
2020         220.0  264.0        325.0      300.0   250.0
2021         248.0  250.0        325.0      300.0   250.0
2022         350.0  400.0        350.0      375.0   400.0
2023         350.0  425.0        350.0      400.0   400.0
2024         300.0  325.0        425.0      425.0   360.0
2025         300.0  300.0        370.0      425.0   350.0
```

Hausses de 2019 à 2025 : maïs local 42,9 %, riz local 41,7 %, sorgho 40,0 %, mil 33,3 %, riz importé 23,3 %. Années les plus chères : 2022 ou 2023 pour les céréales locales, 2024 pour le riz.

💡 **A comprendre** : le mil est **moins** cher en 2025 qu'en 2023. Peut-on dire que « les prix ont baissé » ? Comparez avec 2019. Quelle phrase, juste et complète, écririez-vous ?

---

## Étape 6 : la soudure, région par région (30 min)

🎯 **Objectif** : où le prix du mil monte le plus pendant la soudure (la période avant les récoltes, quand les greniers se vident).

🛠️ **A faire**

1. Le mil de 2019 à 2025 ; tableau croisé : une ligne par région, une colonne par mois (1 à 12), la médiane.
2. Pour chaque région : l'écart en % entre le mois le plus cher et le mois le moins cher (`max(axis=1)` et `min(axis=1)` : le maximum de chaque **ligne**), et le mois le plus cher (`idxmax(axis=1)`).
3. Les 5 régions où l'écart est le plus fort. Puis la médiane nationale du mil par mois.

✅ **Vérification**

```text
            ecart_saison_pct  mois_le_plus_cher
region                                         
Thies                   60.0                  9
Kaffrine                50.0                  8
Sedhiou                 40.1                  7
Dakar                   37.5                 10
Ziguinchor              36.2                  8
```

Au niveau national, la médiane du mil vaut 275 F de janvier à avril (272 F en mars) et 300 F de mai à décembre.

💡 **A comprendre**

1. `axis=1` : sur quoi porte `max` ici, les lignes ou les colonnes ? Rappelez-vous le chapitre 3.
2. La médiane nationale ne montre qu'un petit saut de 25 F. Pourquoi les écarts régionaux sont-ils bien plus forts ? Qu'est-ce que la médiane nationale « écrase » ?
3. Les mois les plus chers vont de juillet à octobre : est-ce cohérent avec la période de soudure au Sénégal ?

---

## Étape 7 : la couverture des marchés (20 min)

🎯 **Objectif** : quels marchés de la liste officielle ne sont plus suivis.

🛠️ **A faire**

1. Chargez la liste des marchés. Comptez les relevés de 2025 par `market_id`.
2. Jointure **gauche** de la liste des marchés avec ce compte, avec `indicator=True`. Combien de marchés ont des relevés en 2025, combien n'en ont pas ?
3. Le nombre de marchés sans relevé en 2025, par région (les 5 premières).
4. Parmi eux, combien n'ont **jamais** eu de relevé depuis 2000 ? Indice : la différence de deux ensembles Python (L1), `set(...) - set(...)`, entre les numéros de la liste des marchés et ceux de **tous** les relevés.

✅ **Vérification**

```text
_merge
both          45
left_only     34
right_only     0
```

Saint-Louis compte 7 marchés sans relevé en 2025, Diourbel 6, Kaolack 4. 34 marchés sans relevé en 2025, dont 12 sans aucun relevé depuis 2000.

💡 **A comprendre** : avec la jointure interne par défaut, qu'auriez-vous vu ? Pourquoi est-ce la question la plus importante pour la **fiabilité** des indicateurs des étapes 3 à 6 ?

---

## Étape 8 : le format long et le classeur des indicateurs (25 min)

🎯 **Objectif** : enregistrer les indicateurs dans un classeur Excel, une feuille par tableau, et une version longue de la grille.

🛠️ **A faire**

1. Passez la grille de l'étape 3 au format long (`reset_index`, puis `melt` avec `id_vars="region"`, `var_name="denree"`, `value_name="prix_median"`). Retirez la case vide.
2. Enregistrez un classeur `indicateurs_2025.xlsx` de quatre feuilles : `regions` (étape 2), `grille` (étape 3), `format_long` (sans index) et `indice` (étape 4). Pour écrire plusieurs feuilles, ouvrez le classeur avec `with pd.ExcelWriter("indicateurs_2025.xlsx") as classeur:`, puis écrivez chaque tableau avec `tableau.to_excel(classeur, sheet_name="...")`. Une `Series` (l'indice) se transforme d'abord en tableau avec `.to_frame()`.
3. Contrôle : relisez **toutes** les feuilles d'un coup avec `pd.read_excel("indicateurs_2025.xlsx", sheet_name=None)` (un dictionnaire : nom de feuille, tableau) et affichez la taille de chacune.

✅ **Vérification**

```text
(112, 3)
(111, 3)
{'regions': (14, 6), 'grille': (14, 9), 'format_long': (111, 3), 'indice': (14, 2)}
```

💡 **A comprendre** : pourquoi la feuille `grille` a-t-elle 9 colonnes alors que la grille n'a que 8 denrées ? Quel format, large ou long, donneriez-vous à quelqu'un qui veut faire ses propres calculs ? et à un directeur qui veut lire ?

---

## Étape 9 : la note (20 min)

🛠️ **A faire** : dans une cellule de texte à la fin du notebook, une note de 8 à 12 lignes au Commissariat, avec des chiffres :

- les deux régions les plus chères et les deux moins chères (étape 4), et ce qui peut l'expliquer ;
- l'évolution des céréales depuis 2019 (étape 5) ;
- où la soudure pèse le plus (étape 6) ;
- **les limites** : régions peu suivies (étape 2), égalités (étape 3), chiffre à vérifier (étape 3), marchés non suivis (étape 7).

✅ **Vérification** : chaque affirmation de la note renvoie à un tableau du notebook. Relancez **tout** le notebook (Exécution > Tout exécuter) : il doit tourner sans erreur du début à la fin.

```bash
git add atelier5_indicateurs.ipynb indicateurs_2025.xlsx
git commit -m "Atelier 5 : indicateurs régionaux 2025 et note"
git tag atelier-5
git push
git push origin atelier-5
```

---

## 🏆 Défis (facultatifs)

1. **Les deux fichiers sont-ils d'accord ?** Joignez à `an` les colonnes `market_id`, `admin1` et `admin2` du fichier des marchés. Quelles colonnes obtenez-vous, et pourquoi `admin2_x` et `admin2_y` ? Recommencez avec `suffixes=("_releve", "_liste")`, puis comptez les lignes où la région ou le département diffère entre les deux fichiers. Enfin, calculez l'indice de cherté **par département** : le plus cher est-il dans la région la plus chère ?
2. **L'indice dans le temps.** Calculez l'indice de cherté de Dakar et de Kaffrine pour chaque année de 2019 à 2025 (même méthode qu'à l'étape 4, mais avec toutes les années). L'écart entre les deux régions se creuse-t-il ?
3. **Les deux arachides.** Pour chaque région et chaque année depuis 2021, le rapport entre le prix médian de l'arachide en coque et celui de l'arachide décortiquée (un `pivot_table`, puis une division de colonnes). Dans combien de couples (région, année) la coque est-elle plus chère ? Rédigez le message que vous enverriez au PAM.
4. 🟣 **Le classeur mis en forme.** Avec `openpyxl` (déjà utilisé par pandas), élargissez les colonnes et mettez en gras la première ligne de chaque feuille du classeur. Cherchez dans la documentation de `openpyxl` : `column_dimensions` et `Font`.

---

## Grille d'autoévaluation

| Je sais... | Oui | Pas encore |
|---|---|---|
| résumer un tableau par groupe avec `groupby` et une agrégation nommée | ☐ | ☐ |
| comparer chaque ligne à son groupe avec `transform` | ☐ | ☐ |
| joindre deux tableaux et contrôler le résultat (`how`, `indicator`, `validate`) | ☐ | ☐ |
| construire et interroger un tableau croisé | ☐ | ☐ |
| passer du format large au format long, et inversement | ☐ | ☐ |
| écrire une phrase juste, avec ses limites, à partir d'un tableau | ☐ | ☐ |
