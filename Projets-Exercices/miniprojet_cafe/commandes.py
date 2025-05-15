def prendre_commande(menu, ventes):
    commande = []
    print("\n=== Prise de commande ===")
    while True:
        article_nom = input("Entrez le nom de l'article (ou 'terminer' ou 't' pour finir) : ").strip()
        if article_nom.lower() == 'terminer' or article_nom.lower() == 't':
            break
        # Vérification si l'article est dans le menu
        article = next((item for item in menu if item["article"].lower() == article_nom.lower()), None)
        if article:
            commande.append(article)
            print(f"Ajouté : {article['article']} ({article['prix']} €)")
        else:
            print("Article introuvable dans le menu.")

    if commande:
        afficher_recapitulatif(commande)
        ventes.extend(commande)  # Ajouter la commande au suivi des ventes

def afficher_recapitulatif(commande):
    print("\n=== Récapitulatif de la commande ===")
    total = 0
    for item in commande:
        print(f"- {item['article']} : {item['prix']} Fcfa")
        total += item['prix']
    print(f"Total : {total} Fcfa")

def afficher_suivi_ventes(ventes):
    print("\n=== Suivi des ventes ===")
    if not ventes:
        print("Aucune vente enregistrée.")
        return

    total_revenu = 0
    article_counts = {}

    # Comptabilisation des articles vendus
    for item in ventes:
        total_revenu += item["prix"]
        article_counts[item["article"]] = article_counts.get(item["article"], 0) + 1

    print("Articles vendus :")
    for article, count in article_counts.items():
        print(f"{article} : {count} vendu(s)")

    print(f"Revenu total : {total_revenu} Fcfa")
