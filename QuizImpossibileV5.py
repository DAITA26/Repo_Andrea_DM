import random

#Domande e risposte
domande = [

    ("Qual è il colore a cui sto pensando?", ["Rosso", "Magenta", "Bordeaux", "Purpureo"]),
    ("Quale è il cognome di Mario?", ["Merlo", "Rossi", "Guidoni", "Giannini"]),
    ("A che numero sto pensando?", [27, 7, 10, 11]),
    ("Quale è il mio Imperatore Romano preferito?", ["Augusto", "Traiano", "Adriano", "Aurelio"]),
    ("Qual è il mio minerale preferito?", ["Quarzo", "Smeraldo", "Diamante", "Grafite"])

]


def quiz():
    punteggi = []

    while True:

#Genera una risposta corretta casuale per ogni domanda
        risposte_corrette = [random.choice(domanda[1]) for domanda in domande]

#Ordina le risposte in modo casuale per ogni domanda
        opzioni = [[domanda[1][i] for i in random.sample(range(4), 4)] for domanda in domande]

#Mostra le domande e gestisce la risposta dell'utente
        for i, domanda in enumerate(domande):
            print(f"\nDomanda: {domanda[0]}")
            for j, opzione in enumerate(opzioni[i]):
                print(f"{j + 1}) {opzione}")

            while True:
                try:
                    risposta = int(input("Inserisci il numero della tua risposta: "))
                    if 1 <= risposta <= 4:
                        break
                    else:
                        print("Inserisci un numero tra 1 e 4.")
                except ValueError:
                    print("Input non valido. Inserisci un numero intero positivo.")

            if opzioni[i][risposta - 1] == risposte_corrette[i]:
                print("Corretto!")
                punteggi.append(1)
            else:
                print(f"Incorretto. La risposta corretta era {risposte_corrette[i]}.")
                punteggi.append(0)

#Calcola e mostra il punteggio finale
        percentuale = sum(punteggi) / len(domande) * 100
        print(f"\nQuiz terminato. Il tuo punteggio è {sum(punteggi)}/{len(domande)}")
        print(f"La tua percentuale di vittoria: {percentuale:.2f}%")

#Richiesta di conferma per rigiocare o uscire
        while True:
            risposta = input("Vuoi rigiocare? (S/N): ").upper()
            if risposta == 'S':
                break
            elif risposta == 'N':
                return
            else:
                print('Input non valido. Inserisci "S" per rigiocare o "N" per uscire.')


#Esecuzione
quiz()
