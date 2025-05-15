from menu import afficher_menu, charger_menu
from commandes import prendre_commande, afficher_suivi_ventes

def afficher_menu_principal():
    print("\n=== Café Gestion ===")
    print("1. Voir le menu")
    print("2. Prendre une commande")
    print("3. Suivi des ventes")
    print("4. Quitter")

def main():
    menu = charger_menu()  # Charger le menu depuis menu.py
    ventes = []  # Liste pour stocker les commandes effectuées

    while True:
        afficher_menu_principal()
        choix = input("Choisissez une option : ")

        if choix == '1':
            afficher_menu(menu)
        elif choix == '2':
            prendre_commande(menu, ventes)
        elif choix == '3':
            afficher_suivi_ventes(ventes)
        elif choix == '4':
            print("Merci d'avoir utilisé Café Gestion. Bonne journée !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
