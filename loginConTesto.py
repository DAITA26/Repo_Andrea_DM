import os
registrati = {"MarioMerlo88": "Merluzzo10",
              "Guastafeste23": "Password55",
              "Piccozza31": "Solegirasole20",
              "Maestria7": "Arrangiarsi123"}
try:
    with open("utenti.txt", "r") as file:
        content = file.read()
        if content.strip():
            registrati = eval(content)
except FileNotFoundError:
    pass

class Utente:
    def __init__(self):
        self.user = None
        self.password = None

    def check(self):
        print("Benvenuto!")
        verifica_esistenza = input("Possiedi già un account? (si/no) ").strip().lower()
        if verifica_esistenza == "si":
            while True:
                nome_utente = input("Inserisci il tuo nome utente ").strip()
                password_utente = input("Inserisci la password ").strip()

                try:
                    stored_password = registrati[nome_utente]

                    if stored_password == password_utente:
                        print("Login effettuato con successo!")
                        break
                    elif stored_password != password_utente:
                        print("Password errata!")
                        scelta_utente = input("Vuoi riprovare? (si/no)  ").strip().lower()
                        if scelta_utente == "si":
                            continue
                        else:
                            break

                except KeyError:
                    print(f"Errore: il nome utente '{nome_utente}' non è registrato.")
                    retry = input("Vuoi riprovare? (si/no) ").strip().lower()
                    if retry != "si":
                        print("Uscita dal programma..")
                        break

        else:
            crea_utente = input("Crea un nome utente ").strip()
            crea_password = input("Crea una password ").strip()

           # with open("utenti.txt", "w") as file:
           #     file.write(f"{crea_utente}:{crea_password}\n")
            try:
                if crea_utente not in registrati:
                    registrati[crea_utente] = crea_password
                    salva_registrati = ()
                    with open("utenti.txt", "w") as file:
                        file.write(str(registrati))

                    print("Registrazione completata")
                else:
                    raise KeyError("Il nome utente esiste già.")
            except KeyError as ex:
                print(ex)



if __name__ == '__main__':
    utente = Utente()
    utente.check()
    print(registrati)