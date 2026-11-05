"""Fabrique le grand registre de Yonnee Express : 500 000 livraisons (environ 25 Mo).

Le fichier est trop gros pour être partagé : chacun le fabrique sur son ordinateur.
Graine fixe : tout le monde obtient exactement le même fichier.

Usage : python fabriquer_grand_registre.py       (crée registre_grand.csv dans le dossier courant)
"""
import csv
import random
from datetime import date, timedelta

TARIFS = {"Médina": 1000, "Plateau": 1500, "Yoff": 2000, "Parcelles": 2000, "Pikine": 2500}
LIVREURS = ["Awa", "Modou", "Fatou", "Ibou", "Coumba"]
COLONNES = ["numero", "date", "livreur", "quartier", "poids", "montant", "frais", "duree_min"]
NOMBRE = 500_000


def une_livraison(rng, numero, debut, jours):
    quartier = rng.choice(list(TARIFS))
    poids = round(rng.uniform(0.3, 12), 1)
    duree = int(rng.gauss(35 + 5 * list(TARIFS).index(quartier), 10))
    return {
        "numero": numero,
        "date": (debut + timedelta(days=rng.randrange(jours))).isoformat(),
        "livreur": rng.choice(LIVREURS),
        "quartier": quartier,
        "poids": poids,
        "montant": rng.randrange(1000, 150001, 500),
        "frais": TARIFS[quartier] + (500 if poids > 5 else 0),
        "duree_min": max(duree, 8),
    }


def livraisons(nombre):
    rng = random.Random(2026)
    for numero in range(1, nombre + 1):
        yield une_livraison(rng, numero, date(2025, 1, 1), 660)


if __name__ == "__main__":
    with open("registre_grand.csv", "w", newline="", encoding="utf-8") as fichier:
        ecrivain = csv.DictWriter(fichier, fieldnames=COLONNES, delimiter=";")
        ecrivain.writeheader()
        ecrivain.writerows(livraisons(NOMBRE))
    print(f"registre_grand.csv : {NOMBRE:,} livraisons écrites".replace(",", " "))
