from decorateurs import log_execution

@log_execution
def ajouter_tache(liste, tache):
    liste.append(tache)
    return liste

def afficher_taches(liste):
    for i, t in enumerate(liste):
        print(f"{i+1}. {t}")

def supprimer_tache(liste, indice):
    try:
        del liste[indice]
        return True
    except IndexError:
        return False