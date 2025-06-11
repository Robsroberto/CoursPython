def verifier_choix(choix):
    return choix in ["1", "2", "3", "4"]

def verifier_tache(tache):
    return len(tache.strip()) > 0