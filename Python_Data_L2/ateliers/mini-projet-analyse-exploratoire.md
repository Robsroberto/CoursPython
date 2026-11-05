<div class="bandeau"><img src="../images/python-bandeau.png" alt="Python" /></div>

# Mini-projet : une analyse exploratoire complète

<p class="auteur">Par <strong>Robert DIASSÉ</strong>, Ingénieur Logiciel et Data</p>

> **Cours** : Python pour la science des données · **Chapitres** : 1 à 6 · **Version** : 2026-10-31

## Avant de commencer

| | |
|---|---|
| **Ce que vous allez construire** | Un notebook qui répond à **une** question sur les prix des marchés du Sénégal, avec toute la démarche du cours : préparation, contrôle de la couverture, statistiques, graphiques, corrélations, conclusions chiffrées et limites ; puis une présentation orale |
| **Travail** | En **binôme** (les deux membres présentent et répondent aux questions) |
| **Durée** | 🟢 Débutant : 12 h · 🔵 Standard : 9 h · 🟣 Expert : 7 h |
| **Prérequis** | Les chapitres 1 à 6 et leurs ateliers |
| **Fichiers fournis** | `mini_projet_depart.ipynb` (le plan du notebook) ; `wfp_food_prices_sen.csv` et `wfp_markets_sen.csv` (déjà utilisés) |
| **Rendu** | Le notebook exécuté (`.ipynb`, toutes les cellules affichées) et 5 diapositives au plus (PDF), puis un oral de 8 minutes |

## Les sujets

Choisissez un sujet (deux binômes d'un même groupe ne prennent pas le même), ou proposez votre propre question à l'enseignant **avant** de commencer.

| Sujet | Question | Pistes |
|---|---|---|
| **1. La soudure** | Les prix des céréales locales montent-ils avant la récolte, et dans quelles régions le plus ? | Profil mensuel du mil, du sorgho et du maïs local ; écart entre le mois le plus cher et le moins cher, par région |
| **2. Le choc de 2022** | Quelles denrées et quelles régions ont le plus augmenté en 2022-2023, et les prix sont-ils redescendus ? | Évolution 2019-2025 ; hausse en % par denrée et par région ; indice base 100 en 2021 |
| **3. Le bassin arachidier** | Les céréales sont-elles moins chères là où elles sont cultivées (Kaolack, Kaffrine, Fatick) ? | Comparaison bassin / reste du pays ; dispersion ; évolution de l'écart |
| **4. Loin de Dakar** | Les régions de l'est et du sud (Kédougou, Tambacounda, Kolda, Ziguinchor, Sédhiou) paient-elles plus cher, et pour quelles denrées ? | Écart à Dakar par denrée ; boîtes par région ; denrées importées contre locales |
| **5. Niébé et arachide** | Comment ont évolué les prix du niébé et de l'arachide depuis 2020, et avec quelle dispersion ? | Évolution ; coefficient de variation ; écart coque / décortiquée (attention à l'anomalie signalée au chapitre 5) |
| **6. Les légumes de 2026** (🟣) | Que disent les premiers relevés de légumes (tomate, oignon, chou...) de 2026 ? | Une seule année : prudence ; couverture ; dispersion entre marchés |

## Ce que doit contenir le notebook

Le notebook de départ (`mini_projet_depart.ipynb`) donne le plan en dix parties. Exigences :

| Partie | Exigences |
|---|---|
| 1-2. Données et préparation | Source et licence citées ; chaque filtre justifié ; le nombre de lignes gardées |
| 3. Couverture | Relevés par année et par région (et par marché si utile) ; les périodes ou régions trop peu suivies sont **écartées ou signalées** |
| 4. Statistiques | `describe` commenté ; médiane justifiée ; valeurs atypiques repérées et discutées |
| 5-7. Analyse | Au moins **six** graphiques de **quatre** types différents (distribution, évolution, comparaison, relation), chacun avec titre, unités et source, et suivi d'une phrase chiffrée ; au moins **une** corrélation, avec la prudence du chapitre 6 (section 7.2) |
| 8. Conclusions | Cinq phrases au plus, chiffrées, qui **répondent** à la question |
| 9. Limites | Au moins trois limites réelles de **votre** analyse |
| 10. Usage de l'IA | Ce qui a été demandé, gardé, corrigé et vérifié (ou « aucun ») |

**Le notebook doit s'exécuter de bout en bout** (Colab : **Exécution > Tout exécuter**) sans erreur, sur un environnement neuf.

## Les étapes conseillées

| Semaine | Ce qu'il faut avoir fini |
|---|---|
| 1 | Sujet choisi, question précise écrite ; préparation et couverture ; **montrer la question et la couverture à l'enseignant** |
| 2 | Statistiques et premiers graphiques |
| 3 | Corrélations, conclusions, limites ; relecture croisée entre binômes |
| 4 | Diapositives et répétition de l'oral |

> 💡 Une bonne question est **précise** et **vérifiable** avec les données. « Les prix au Sénégal » est trop vague ; « le mil est-il moins cher dans le bassin arachidier, et l'écart a-t-il changé depuis 2015 ? » se prête à une analyse.

## L'oral (8 minutes + questions)

1. La question, et pourquoi elle compte (1 minute).
2. Les données : ce qui a été gardé, la couverture (1 minute).
3. Trois graphiques clés, chacun avec sa phrase (4 minutes).
4. Les conclusions et les limites (2 minutes).

L'enseignant demandera à **chaque** membre d'expliquer une cellule de code et un chiffre de la conclusion, en le retrouvant dans le notebook.

## Grille de notation (sur 20)

| Critère | Points |
|---|---|
| Question précise et pertinente ; couverture contrôlée | 2 |
| Préparation propre et justifiée ; notebook qui s'exécute de bout en bout | 3 |
| Statistiques descriptives justes et commentées ; atypiques discutés | 3 |
| Graphiques : au moins six, de quatre types, propres (titre, unités, source, axes honnêtes) | 5 |
| Corrélation calculée et interprétée avec prudence | 2 |
| Conclusions chiffrées qui répondent à la question ; limites réelles | 3 |
| Oral : clarté, réponses de **chaque** membre | 2 |

## Ce qui est interdit

- Rendre une analyse dont un chiffre ne sort pas du notebook.
- Recopier le notebook d'un autre binôme.
- Faire écrire le notebook par une IA sans le comprendre : l'oral le révèle immédiatement. L'IA est permise pour **comprendre** ou retrouver une syntaxe, à déclarer dans la partie 10.
