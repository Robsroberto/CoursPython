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

---

# **Chapitre 1 : Introduction à la programmation avec Python**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 

## Par Robert DIASSÉ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="../python.jpeg" alt="ISI" width="50px">



### **Objectifs du chapitre :**
- Découvrir l'historique de Python.
- Comprendre les principaux contextes d'utilisation du langage.
- Installer Python et configurer son environnement de base.
- Exécuter son premier script pour vérifier l'installation.

---

### **Contenu du chapitre :**

---

#### **1. Historique de Python**
- **Origine de Python :**
  - Créé par **Guido van Rossum** en 1991.
  - Inspiré par des langages comme ABC, C, et Modula-3, Python avait pour but de rendre la programmation plus accessible et lisible.
- **Évolution :**
  - **Python 1.0 (1991)** : Introduction des fonctionnalités fondamentales comme les types de données et les structures de contrôle.
  - **Python 2.x (2000)** : Ajout de nombreuses bibliothèques, mais cette version est maintenant obsolète.
  - **Python 3.x (2008)** : Amélioration de la syntaxe et des fonctionnalités, version utilisée aujourd'hui.
- **Pourquoi le nom "Python" ?**
  - Le nom vient de la série télévisée humoristique *Monty Python's Flying Circus*. Ce n'est pas une référence à un serpent.

---

#### **2. Cadres d'utilisation de Python**
Python est utilisé dans de nombreux contextes grâce à sa simplicité et sa puissance. Voici quelques domaines principaux où il est couramment employé :

- **Développement web :**
  - Création de sites et d'applications web grâce à des frameworks tels que Flask et Django.

- **Automatisation des tâches :**
  - Scripts pour automatiser les tâches répétitives, comme la gestion de fichiers ou le scraping web.

- **Analyse de données :**
  - Traitement et analyse des données avec des bibliothèques comme Pandas et NumPy.

- **Développement de logiciels :**
  - Prototypage et développement rapide d'applications grâce à sa syntaxe concise.

---

#### **3. Installation de Python**

##### **3.1 Télécharger Python**
1. **Rendez-vous sur le site officiel de Python :**
   - [python.org](https://www.python.org/downloads/)
2. **Choisissez la version la plus récente de Python 3.**
   - Exemple : **Python 3.x.x**
   - Téléchargez la version compatible avec votre système d'exploitation (Windows, macOS, Linux).

---

##### **3.2 Installer Python sous différents systèmes d'exploitation**

1. **Sous Windows :**
   - Exécutez le fichier d'installation téléchargé.
   - Cochez l'option **"Add Python to PATH"** avant de cliquer sur "Install Now".
   - Suivez les étapes pour finaliser l'installation.

2. **Sous macOS :**
   - Python 2 est préinstallé sur macOS, mais il est obsolète.
   - Installez Python 3 via le fichier d'installation téléchargé ou utilisez Homebrew :
     ```bash
     brew install python
     ```

3. **Sous Linux :**
   - Python est généralement préinstallé. Vérifiez avec :
     ```bash
     python3 --version
     ```
   - Si Python 3 n'est pas installé, ajoutez-le via votre gestionnaire de paquets :
     ```bash
     sudo apt update
     sudo apt install python3
     ```

---

##### **3.3 Vérifier l'installation de Python**
- Ouvrez un terminal ou une invite de commande, puis tapez :
  ```bash
  python --version
  ```
  ou
  ```bash
  python3 --version
  ```
- Si Python est correctement installé, vous verrez un message indiquant la version, par exemple :  
  **Python 3.10.7**

---

#### **4. Configuration d’un éditeur de texte ou IDE**
Pour écrire du code Python efficacement, utilisez un éditeur ou un IDE :
- **IDLE :** Inclus avec Python, simple pour les débutants.
- **Visual Studio Code :**
  - Téléchargez [VS Code](https://code.visualstudio.com/).
  - Installez l’extension "Python" dans VS Code.
- **Autres options populaires :**
  - PyCharm, Atom, Jupyter Notebook (pour les scripts interactifs).

---

#### **5. Premier programme Python : "Hello, World !"**

1. **Créer un fichier Python :**
   - Ouvrez un éditeur de texte.
   - Écrivez le code suivant et sauvegardez-le dans un fichier nommé `hello.py` :
     ```python
     print("Hello, World!")
     ```

2. **Exécuter le programme :**
   - Dans le terminal ou l’invite de commande, allez dans le répertoire contenant `hello.py` :
     ```bash
     python hello.py
     ```
     ou
     ```bash
     python3 hello.py
     ```
   - Résultat attendu :
     ```
     Hello, World!
     ```

---

### **Exercices pratiques**
1. **Exercice 1 : Vérification de l'installation**
   - Tapez `python` ou `python3` dans le terminal. Essayez la commande suivante dans l'environnement interactif Python :
     ```python
     print("Python est installé avec succès !")
     ```

2. **Exercice 2 : Modifiez le programme Hello, World !**
   - Ajoutez une deuxième ligne de code qui affiche :  
     "Bienvenue dans le monde de la programmation !"

   Exemple :
   ```python
   print("Hello, World!")
   print("Bienvenue dans le monde de la programmation !")
   ```

---

### **Résumé du chapitre**
- Python a été créé par Guido van Rossum en 1991.
- Il est largement utilisé pour des applications diverses, sans mentionner ici sa polyvalence dans tous les domaines.
- L'installation de Python est simple et accessible sur tous les systèmes d'exploitation.
- Vous avez exécuté votre premier script Python avec succès.
