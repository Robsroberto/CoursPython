def log_execution(fonction):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Début : {fonction.__name__}")
        resultat = fonction(*args, **kwargs)
        print(f"[LOG] Fin : {fonction.__name__}")
        return resultat
    return wrapper