def charger_menu():
    # Liste des articles disponibles
    menu = [
        {"article": "Café", "prix": 250.0},
        {"article": "Thé", "prix": 200.0},
        {"article": "Croissant", "prix": 300.0},
        {"article": "Jus d'orange", "prix": 500.0}
    ]
    return menu

def afficher_menu(menu):
    print("\n=== Menu du Café ===")
    for index, item in enumerate(menu):
        print(f"{index + 1}. {item['article']} - {item['prix']} Fcfa")
