#Dizionario Nome Utente & Password
utentePass = {
    'MarioMerlo85': 'Merluzzo1',
    'Jacopone77': 'Passwordissima',
    'Lucano123': 'Pippoide201'
}

def login():
    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la tua password: ")

    try:
        stored_password = utentePass.get(username)

        if stored_password == password:
            print("Login effettuato con successo!")
        else:
            raise ValueError("Utente o Password errata")

    except Exception as ex:
        print(f"Errore: {ex}")


#Esecuzione
login()
