class LoginError2(Exception):
    """Eccezione personalizzata per errori di login."""
    pass

class UserNotFoundError2(LoginError2):
    """Errore quando l'utente non esiste."""
    pass

class IncorrectPasswordError2(LoginError2):
    """Errore quando la password è sbagliata."""
    pass

def login(utente, password, credenziali):

    if utente not in credenziali:
        raise UserNotFoundError2(f"L'utente {utente} non esiste.")

    if credenziali[utente] != password:
        raise IncorrectPasswordError2("La password inserita è errata.")

    return f"Login effettuato con successo per l'utente {utente}!"

#Dizionario Nome Utente & Password
credenziali = {
    'MarioMerlo': 'Merluzzo1',
    'Jacopone77': 'passwordissima',
    'Lucano123': 'pippo201'
}

#Simulazione del login
try:
    username = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")

    risultato = login(username, password, credenziali)
    print(risultato)
except UserNotFoundError2 as e:
    print(f"Errore: {e}")

except IncorrectPasswordError2 as e:
    print(f"Errore: {e}")

except Exception as e:
    print(f"Errore imprevisto: {e}")