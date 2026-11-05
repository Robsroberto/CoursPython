<div class="bandeau"><img src="../images/python-bandeau.png" alt="Python" /></div>

# Atelier 4 : nettoyer les relevés régionaux

<p class="auteur">Par <strong>Robert DIASSÉ</strong>, Ingénieur Logiciel et Data</p>

> **Cours** : Python pour la science des données · **Chapitre** : 4, Manipuler et nettoyer avec pandas · **Version** : 2026-10-23

## Avant de commencer

| | |
|---|---|
| **Ce que vous allez construire** | Un notebook qui nettoie un classeur Excel de 4 537 relevés de prix de 2024 envoyés par les régions, vérifie le résultat en le comparant aux relevés officiels, et enregistre le classeur propre avec un bilan |
| **Durée** | 🟢 Débutant : 4 h · 🔵 Standard : 3 h · 🟣 Expert : 2 h (sans les défis) |
| **Prérequis** | Avoir lu le chapitre 4 ; votre dépôt `prix-marches` |
| **Fichiers fournis** | `releves_regionaux_2024.xlsx` (le classeur à nettoyer), `wfp_food_prices_sen.csv` (déjà fourni), le notebook de départ |
| **Rendu** | Le notebook `atelier4_nettoyage.ipynb` dans votre dépôt `prix-marches`, avec l'étiquette `atelier-4` |

**Le scénario.** Chaque région a recopié à la main ses relevés de prix de 2024 dans un classeur commun (feuille `releves_2024`), avec cinq colonnes : `date`, `region`, `marche`, `denree`, `prix_fcfa_kg`. Les prix et les marchés viennent des vrais relevés du PAM ; les défauts de saisie ont été ajoutés pour l'exercice. Votre mission : un classeur **propre**, et la **preuve** qu'il est propre.

> 📍 **Point de départ** : le notebook de départ fourni, une section par étape. Envoyez le classeur et le fichier du PAM dans Colab.

### Comment travailler

Mêmes règles que les ateliers précédents. **Règle de cet atelier** : avant de corriger quoi que ce soit, **regardez** (`value_counts`, `unique`, `isna`) ; après chaque correction, **vérifiez** par un chiffre.

---

## Étape 1 : charger le classeur (15 min)

🛠️ **A faire** : lisez la feuille `releves_2024` avec `pd.read_excel(..., sheet_name="releves_2024")` dans `brut` ; affichez sa taille, ses types, ses premières lignes et le nombre de valeurs manquantes par colonne.

✅ **Vérification** : 4 537 lignes et 5 colonnes ; `date` et `prix_fcfa_kg` sont de type `object` (des types mélangés) ; 5 marchés et 23 prix manquants.

💡 **A comprendre** : pourquoi `prix_fcfa_kg` n'est-il pas de type `float64` ? Et `date`, pas de type `datetime64` ? Regardez les premières lignes : quelle région est mal écrite dès la cinquième ligne ?

---

## Étape 2 : les doublons (10 min)

🛠️ **A faire** : comptez les lignes en double, puis supprimez-les dans un nouveau tableau `releves` (avec `.copy()`).

✅ **Vérification** : 35 doublons ; 4 502 lignes après suppression.

💡 **A comprendre** : pourquoi supprimer les doublons **en premier**, avant les autres corrections ?

---

## Étape 3 : les noms de régions (25 min)

🛠️ **A faire**

1. Combien de façons différentes d'écrire les régions ? Affichez la liste triée.
2. Uniformisez : retirez les espaces au début et à la fin (`str.strip()`), mettez une majuscule au début de chaque mot (`str.title()`), puis remplacez les variantes restantes avec un dictionnaire de corrections et `.replace(...)`, pour retrouver l'écriture du PAM (sans accents : `Thies`, `Kedougou`, `Sedhiou`, `Saint Louis`).

✅ **Vérification** : 21 façons d'écrire avant, **14** régions après.

💡 **A comprendre** : que deviennent `" thies "` et `"THIES"` après `strip()` puis `title()` ? Pourquoi faut-il quand même un dictionnaire pour `Thiès` ou `St Louis` ?

---

## Étape 4 : les prix en texte (20 min)

🛠️ **A faire** : convertissez `prix_fcfa_kg` en nombres : transformez d'abord toute la colonne en texte (`.astype(str)`), retirez `" F"`, remplacez la virgule par un point, puis `pd.to_numeric(..., errors="coerce")`.

✅ **Vérification** : type `float64` ; 31 prix manquants.

💡 **A comprendre** : il y avait 23 prix vides au départ. D'où viennent les 8 de plus ? (Regardez les valeurs qui n'ont pas pu être converties, **avant** la conversion.)

---

## Étape 5 : les prix au sac (30 min)

🎯 **Objectif** : repérer les prix saisis pour un **sac de 50 kg** au lieu du kilo.

Un prix du riz à 18 150 F le kilo est absurde ; à 18 150 F le sac de 50 kg, il fait 363 F le kilo, un prix normal.

🛠️ **A faire**

1. La médiane des prix **de chaque denrée**, pour chaque ligne : `groupby("denree")["prix_fcfa_kg"].transform("median")` (chapitre 4, section 8.1).
2. Un masque `au_sac` : le prix dépasse 10 fois la médiane de sa denrée. Combien de lignes ? Affichez-en trois.
3. Corrigez ces lignes en divisant leur prix par 50 (`releves.loc[au_sac, "prix_fcfa_kg"] = ...`), et affichez le nouveau prix maximal.

✅ **Vérification** : 10 prix au sac (par exemple 17 500 F pour du sorgho importé) ; prix maximal après correction : 1 600 F.

💡 **A comprendre** : pourquoi comparer à la médiane **de la denrée** et pas à la médiane de tous les prix ? Pourquoi la médiane plutôt que la moyenne (pensez à ce que ces 10 prix font à la moyenne) ?

---

## Étape 6 : les dates (15 min)

🛠️ **A faire** : convertissez la colonne `date` avec `pd.to_datetime(..., format="mixed", dayfirst=True)` ; affichez son type, le nombre de dates manquantes, la plus ancienne et la plus récente.

✅ **Vérification** : `datetime64` ; 0 date illisible ; du 15 janvier au 15 décembre 2024.

💡 **A comprendre** : que veut dire `dayfirst=True` ? Que deviendrait `"05/03/2024"` sans lui ?

---

## Étape 7 : les valeurs manquantes (15 min)

🛠️ **A faire** : supprimez les lignes sans prix (`dropna(subset=[...])`) en comptant combien vous en retirez ; remplacez les marchés manquants par `"non renseigné"` (`fillna`) ; vérifiez qu'il ne reste **aucune** valeur manquante.

✅ **Vérification** : 31 lignes sans prix retirées ; **4 471** relevés propres ; 0 valeur manquante.

💡 **A comprendre** : pourquoi supprimer les prix manquants, mais garder les lignes sans marché ?

---

## Étape 8 : vérifier le nettoyage (25 min)

🎯 **Objectif** : prouver que le nettoyage n'a pas faussé les données.

Les relevés du classeur viennent du fichier du PAM : on peut comparer.

🛠️ **A faire**

1. Dans le fichier du PAM, les relevés au kilo de 2024 : combien y en a-t-il ?
2. Le prix moyen de chaque denrée dans votre tableau propre, et dans le fichier du PAM (`groupby(...).mean()`) ; le plus grand écart entre les deux, en valeur absolue.

✅ **Vérification** : 4 502 relevés dans le fichier du PAM (autant que votre tableau après la suppression des doublons) ; plus grand écart entre les moyennes : **0,68 F**.

💡 **A comprendre**

- Pourquoi les moyennes ne sont-elles pas **exactement** égales ? (Pensez aux 31 lignes retirées.)
- Dans un vrai projet, on n'a pas de « fichier officiel » pour comparer. Comment vérifier un nettoyage, alors ?

---

## Étape 9 : enregistrer et faire le bilan (15 min)

🛠️ **A faire**

1. Triez le tableau par région, date et marché ; enregistrez-le en Excel (`releves_regionaux_2024_propre.xlsx`) et en CSV, **sans l'index**.
2. Un dictionnaire `bilan` : lignes reçues, doublons, prix au sac corrigés, lignes sans prix, lignes propres.
3. Une cellule de texte de 6 lignes : ce que vous diriez aux responsables régionaux pour que le classeur de 2025 soit propre dès le départ.

✅ **Vérification** : `{'lignes_recues': 4537, 'doublons': 35, 'prix_au_sac_corriges': 10, 'lignes_sans_prix': 31, 'lignes_propres': 4471}`.

Puis : **Exécution > Redémarrer la session et tout exécuter**, déposez le notebook dans votre dépôt et étiquetez `atelier-4`.

---

## 🏆 Défis (facultatifs)

1. **Une fonction de nettoyage.** Rassemblez les étapes 2 à 7 dans une fonction `nettoyer(brut)` qui renvoie le tableau propre et le bilan. Pourrait-elle servir telle quelle pour le classeur de 2025 ?
2. **Les marchés.** Les noms de marchés sont-ils, eux aussi, écrits de plusieurs façons ? Comparez la liste des marchés de votre tableau propre avec celle du fichier des marchés du PAM.
3. **Les prix au sac oubliés.** Le seuil « 10 fois la médiane » a trouvé 10 lignes. Avec un seuil de 5, en trouvez-vous plus ? Regardez-les : sont-ce des erreurs ?
4. 🟣 **Le contrôle par marché.** Pour chaque marché, comparez le prix de chaque mois au prix médian du marché pour la même denrée, et listez les écarts de plus de 50 %. Combien en trouvez-vous ? Sont-ils plausibles ?

---

## Grille d'autoévaluation

| Je sais... | Oui | Pas encore |
|---|---|---|
| lire un classeur Excel et diagnostiquer ses défauts | ☐ | ☐ |
| supprimer les doublons et uniformiser des textes | ☐ | ☐ |
| convertir des prix et des dates écrits de plusieurs façons | ☐ | ☐ |
| repérer des valeurs aberrantes par rapport à leur groupe | ☐ | ☐ |
| traiter les valeurs manquantes en justifiant mes choix | ☐ | ☐ |
| vérifier un nettoyage par un chiffre, et en faire le bilan | ☐ | ☐ |
