import gestion_taches
import fichier
import verificateur


def menu():
    print("\n--- MENU ---")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")

# def run():
#     taches = []
#     while True:
#         menu()
#         choix = input("Votre choix : ")

#         if choix == "1":
#             tache = input("Entrez une nouvelle tâche : ")
#             gestion_taches.ajouter_tache(taches, tache)
#         elif choix == "2":
#             gestion_taches.afficher_taches(taches)
#         elif choix == "3":
#             try:
#                 index = int(input("Numéro de la tâche à supprimer : ")) - 1
#                 if not gestion_taches.supprimer_tache(taches, index):
#                     print("Tâche introuvable.")
#             except ValueError:
#                 print("Veuillez entrer un nombre valide.")
#         elif choix == "4":
#             print("Fermeture du programme.")
#             break
#         else:
#             print("Choix invalide.")
def run():
    fichier_nom = "mes_taches.txt"
    taches = fichier.charger(fichier_nom)
    while True:
        menu()
        choix = input("Votre choix : ")
        # if choix == "1":
        #     tache = input("Entrez une nouvelle tâche : ")
        #     gestion_taches.ajouter_tache(taches, tache)
        if choix == "1":
            tache = input("Entrez une nouvelle tâche : ")
            if verificateur.verifier_tache(tache):
                gestion_taches.ajouter_tache(taches, tache)
            else:
                print("Erreur : tâche vide non autorisée.")
        elif choix == "2":
            gestion_taches.afficher_taches(taches)
        elif choix == "3":
            try:
                index = int(input("Numéro de la tâche à supprimer : ")) - 1
                if not gestion_taches.supprimer_tache(taches, index):
                    print("Tâche introuvable.")
            except ValueError:
                print("Erreur : veuillez entrer un entier.")
        elif choix == "4":
            fichier.sauvegarder(taches, fichier_nom)
            print("Tâches sauvegardées. À bientôt !")
            break

run()