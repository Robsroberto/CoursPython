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

## Série  Exercice structures répétitives Algo-Python

## Par Robert DIASSÉ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="../python.jpeg" alt="ISI" width="50px">



1. **Affichage en boucle**  
    Écrire un algorithme qui affiche **10 fois** la phrase :  
    "Je suis en train d'apprendre les boucles en algorithmie."  
2. **Afficher les N premiers nombres**  
   Écrire un algorithme qui demande un nombre entier **N** à l'utilisateur, puis affiche les **N premiers entiers positifs** (de 1 à N).  

3. **Somme des N premiers nombres**  
   Écrire un algorithme qui demande un nombre entier **N** à l'utilisateur, puis **calcule la somme** des **N premiers nombres entiers** (de 1 à N).  

4. **Table de multiplication**  
   Écrire un algorithme qui demande un nombre entier à l'utilisateur et affiche sa **table de multiplication** jusqu'à 10.  

5. **Afficher les nombres pairs jusqu'à N**  
   Écrire un algorithme qui demande un nombre entier **N** et affiche tous les **nombres pairs** de **0 à N**.  
6. **Affichage des nombres impairs jusqu'à N**  
    Écrire un algorithme qui demande un nombre entier **N** et affiche tous les **nombres impairs** de **1 à N**.  
<!-- 5. **Compter les chiffres d'un nombre**  
   Écrire un algorithme qui demande un nombre entier **N** et affiche le **nombre de chiffres** qu'il contient.   -->

5. **Factorielle d’un nombre**  
   Écrire un algorithme qui demande un nombre entier **N** et affiche sa **factorielle** :  
   N! = 1 × 2 × 3 × ... × N  

6. **Deviner un nombre (Jeu interactif)**  
   Le programme choisit **un nombre aléatoire entre 1 et 100**. L'utilisateur doit essayer de **deviner le nombre**.  
   Le programme lui donne des **indications** :  
   - "Trop grand" si la tentative est supérieure.  
   - "Trop petit" si la tentative est inférieure.  
   - "Bravo !" si la tentative est correcte.  

<!-- 7. **Suite de Fibonacci**  
   Écrire un algorithme qui affiche les **N premiers termes de la suite de Fibonacci** :  
   F₀ = 0, F₁ = 1, Fₙ = Fₙ₋₁ + Fₙ₋₂   -->
7. **Afficher les diviseurs d’un nombre**  
    Écrire un algorithme qui demande un nombre **N** et affiche tous ses **diviseurs**.  

8. **Trouver un nombre premier**  
   Écrire un algorithme qui demande un nombre **N** et indique s'il est **premier** (divisible uniquement par 1 et lui-même).  

9. **Trouver un nombre parfait**  
   Écrire un algorithme qui demande un nombre **N** et indique s'il est **parfait** (la somme de ses diviseurs excepté lui même est égale a lui).  

<!-- 10. **Inverser un nombre**  
   Écrire un algorithme qui demande un nombre et affiche son **inverse**.   -->
10. **Calcul de la moyenne d'une série de nombres**  
    Écrire un algorithme qui demande un nombre **N**, puis **N** nombres, et calcule leur **moyenne**.  

<!-- 
11. **Somme des nombres pairs jusqu'à N**  
    Écrire un algorithme qui demande un nombre entier **N** et calcule la **somme des nombres pairs** compris entre 1 et N.   -->

<!-- 14. **Compter les multiples de 3 dans un intervalle**  
    Écrire un algorithme qui demande deux nombres **A** et **B** (A < B) et affiche le **nombre de multiples de 3** entre A et B.   -->

<!-- 15. **Calcul de puissance**  
    Écrire un algorithme qui demande deux nombres **X** et **N**, puis calcule **X puissance N** (Xⁿ) sans utiliser la fonction exponentielle.   -->

<!-- 16. **Trouver le plus grand nombre parmi N valeurs**  
    Écrire un algorithme qui demande à l'utilisateur **N** nombres et affiche le **plus grand nombre** parmi eux.   -->

<!-- 17. **Compter les voyelles dans une phrase**  
    Écrire un algorithme qui demande une **phrase** à l'utilisateur et compte le nombre de voyelles (`a, e, i, o, u, y`).   -->


11. **Affichage d’un triangle de nombres**  
    Écrire un algorithme en **python** qui demande un nombre **N** et affiche un **triangle** de nombres de la forme suivante (exemple pour N = 4) :  
    ```
    1  
    1 2  
    1 2 3  
    1 2 3 4  
    ```  

12. **Somme des chiffres d’un nombre**  
    Écrire un algorithme qui demande un nombre **N** et calcule la **somme de ses chiffres**.  

13. **Trouver le plus petit chiffre d’un nombre**  
    Écrire un algorithme qui demande un nombre **N** et affiche son **plus petit chiffre**.  
<!-- 
23. **Vérifier si un nombre est un palindrome**  
    Écrire un algorithme qui demande un nombre **N** et vérifie s'il se lit de la même manière de gauche à droite et de droite à gauche (ex: 121, 3443).   -->

14. **Générer un rectangle de caractères**  
    Écrire un algorithme en **python** qui demande deux nombres **L** et **H** (largeur et hauteur) et affiche un rectangle de `*` de dimensions L × H.  

15. **Série de nombres décroissants**  
    Écrire un algorithme qui demande un nombre **N** et affiche une suite décroissante de **N à 1**.  

16. **Calcul du PGCD de deux nombres**  
    Écrire un algorithme qui demande deux nombres **A** et **B** et calcule leur **PGCD (Plus Grand Commun Diviseur)** à l'aide de l'algorithme d'Euclide.  

17. **Suite de nombres avec condition d’arrêt**  
    Écrire un algorithme qui demande à l'utilisateur d'entrer des nombres jusqu'à ce qu'il saisisse **0**. Il affiche ensuite la somme des nombres saisis.  

<!-- 28. **Convertir un nombre décimal en binaire**  
    Écrire un algorithme qui demande un nombre entier **N** et affiche son **équivalent binaire**.   -->

18. **Affichage en damier**  
    Écrire un algorithme en **python** qui demande un nombre **N** et affiche un **damier de `#` et `.`** de dimensions N × N.  
    ```
    # . # . #  
    . # . # .  
    # . # . #  
    . # . # .  
    ```  

19. **Calcul de la somme des carrés des nombres jusqu'à N**  
    Écrire un algorithme qui demande un nombre **N** et calcule la **somme des carrés** de tous les nombres de 1 à N :  
    \[
    S = 1² + 2² + 3² + ... + N²
    \]  

