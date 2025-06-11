def sauvegarder(taches, nom_fichier):
    with open(nom_fichier, "w") as f:
        for tache in taches:
            f.write(tache + "\n")

def charger(nom_fichier):
    try:
        with open(nom_fichier, "r") as f:
            return [ligne.strip() for ligne in f.readlines()]
    except FileNotFoundError:
        return []