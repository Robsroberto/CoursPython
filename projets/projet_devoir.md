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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="../python.jpeg" alt="ISI" width="50px">

# **Cahier des Charges : Application de Gestion des Réservations d’une Salle de Cinéma**  

## Par Robert DIASSÉ 

## **1. Présentation du Projet**  

### **1.1. Contexte et Objectifs**  
L’objectif de ce projet est de développer une application en **Python avec Tkinter** permettant la **gestion des réservations de places** pour une salle de cinéma. Cette application offrira une interface graphique simple et intuitive permettant aux utilisateurs de :  
- Consulter la liste des films et leurs séances disponibles.  
- Sélectionner un film et une séance.  
- Réserver un nombre de places.  
- Annuler une réservation si nécessaire.  

Ce projet vise à vous initier à la conception d’interfaces graphiques avec **Tkinter**, tout en appliquant les notions de programmation structurée et de gestion des données en mémoire dont les tous cours vous ont été fourni .  

---

## **2. Spécifications Fonctionnelles**  

### **2.1. Gestion des Films et Séances**  
- Affichage des films disponibles avec leurs horaires de projection.  
- Sélection d’un film et d’une séance.  

### **2.2. Gestion des Réservations**  
- Saisie du **nombre de places** à réserver.  
- Vérification de la **disponibilité des places** avant validation.  
- Mise à jour du **nombre de places restantes** après chaque réservation.  
- Possibilité d’**annuler une réservation**.  

### **2.3. Interface Graphique (UI/UX)**  
- Une **fenêtre principale** avec :  
  - Une **liste déroulante** pour sélectionner un film et une séance.  
  - Un **champ de saisie** pour entrer le nombre de places à réserver.  
  - Un **bouton de validation** pour confirmer la réservation.  
  - Un **affichage en temps réel** du nombre de places disponibles.  

---

## **3. Architecture du Projet**  

### **3.1. Organisation des Fichiers**  

Le projet sera structuré comme suit :  

```
GestionCinema/
├── main.py         # Point d'entrée principal de l'application
├── gui.py          # Interface graphique avec Tkinter
├── cinema.py       # Gestion des séances et des réservations
└── README.md       # Documentation du projet
```

- **`main.py`** : Initialise et lance l’application.  
- **`gui.py`** : Contient le code lié à l’interface graphique.  
- **`cinema.py`** : Gère les données des films et la logique métier des réservations.  
- **`README.md`** : Explication du fonctionnement du projet et instructions d’utilisation.  

---

## **4. Déroulement de l’Application**  

### **4.1. Lancement de l’Application**  
- Affichage de la fenêtre principale.  
- Chargement des films et des séances disponibles.  

### **4.2. Réservation d’une Séance**  
- L’utilisateur sélectionne un **film** et un **horaire**.  
- Il entre le nombre de places qu’il souhaite réserver.  
- L’application vérifie si les places sont disponibles.  
- Si la réservation est validée, le nombre de places restantes est mis à jour.  

### **4.3. Annulation d’une Réservation**  
- L’utilisateur sélectionne une réservation existante.  
- Il peut annuler sa réservation, ce qui remet les places à disposition.  

---

## **5. Contraintes Techniques**  

### **5.1. Technologies Utilisées**  
- **Langage** : Python  
- **Bibliothèque** : Tkinter  

### **5.2. Contraintes de Développement**  
- L’interface doit être simple et intuitive.  
- Le programme doit être modulaire et bien structuré.  
- L’application doit fonctionner **sans base de données** (stockage en mémoire des réservations).  

---

## **6. Instructions pour Git/GitHub**  

Vous devrez :  
1. **Initialiser un dépôt Git** dans leur projet :  
   ```sh
   git init
   ```  
2. **Créer un dépôt GitHub** et **lier leur projet** :  
   ```sh
   git remote add origin https://github.com/utilisateur/gestion-cinema.git
   ```  
3. **Commiter et pousser leur projet en ligne** :  
   ```sh
   git add .
   git commit -m "Initialisation du projet"
   git push -u origin main
   ```  
**NB: Faites les recherches nécessaires sur git et github pour arrivé au resultat attendu**
---

## **7. Modalités d’Évaluation**  

Vous serez évalués sur :  
- **une présentation de votre application avec les fonctionnalités et le code structuré**
- **La bonne structuration du code** et son organisation en modules.  
- **L’interface utilisateur** et son ergonomie.  
- **Le respect des fonctionnalités demandées**.  
- **L’utilisation de Git et GitHub** pour la gestion de version.  

---



