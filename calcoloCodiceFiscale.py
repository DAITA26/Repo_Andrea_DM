import datetime

#Dati inerenti a nomi, comuni, etc (esempio fittizio, inserire dati personali per verifica)
comuni_belfiore = {
    "ROMA": "F100",
    "MILANO": "F102",
    "NAPOLI": "F103",
    #Aggiungere i dati per prova qui sotto:

}


def calcola_codice_cognome(cognome):
    consonanti = ''.join([c for c in cognome.upper() if c.isalpha() and c not in 'AEIOU'])
    vocali = ''.join([c for c in cognome.upper() if c.isalpha() and c in 'AEIOU'])
    return consonanti[:3] + vocali[:2].upper() + 'XX'


def calcola_codice_nome(nome):
    consonanti = ''.join([c for c in nome.upper() if c.isalpha() and c not in 'AEIOU'])
    vocali = ''.join([c for c in nome.upper() if c.isalpha() and c in 'AEIOU'])
    return consonanti[:3] + vocali[:2].upper() + 'XX'


def calcola_codice_data_nascita(data_nascita, sesso):
    data = datetime.datetime.strptime(data_nascita, '%d/%m/%Y')
    anno = str(data.year)[-2:]
    mese_codice = 'ABCDEHLMPRST'
    mese = mese_codice[data.month - 1]
    giorno = data.day + 40 if sesso == 'F' else data.day
    return anno + mese + f'{giorno:02d}'


def calcola_codice_comune(comune):
    return comuni_belfiore.get(comune.upper(), 'XXX')  #Restituisce 'XXX' se il comune non è trovato


def calcola_carattere_di_controllo(cf_parziale):
    valori = {chr(i): i - 48 for i in range(48, 58)}
    valori.update({chr(i): i - 55 for i in range(65, 91)})

    dispari = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
               1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 1, 0, 5, 7, 9, 13, 15, 17, 19, 21]
    pari = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 1, 0, 5, 7, 9, 13, 15, 17, 19, 21]

    somma = sum(dispari[valori[cf_parziale[i]]] if i % 2 == 0 else pari[valori[cf_parziale[i]]] for i in range(15))
    return chr((somma % 26) + 65)


def genera_codice_fiscale(nome, cognome, data_nascita, sesso, comune):
    cf = calcola_codice_cognome(cognome)
    cf += calcola_codice_nome(nome)
    cf += calcola_codice_data_nascita(data_nascita, sesso)
    cf += calcola_codice_comune(comune)
    cf += calcola_carattere_di_controllo(cf)
    return cf


def main():
    print("Generatore di Codice Fiscale")

    cognome = input("Inserisci il cognome: ").upper()
    nome = input("Inserisci il nome: ").upper()
    data_nascita = input("Inserisci la data di nascita (dd/mm/yyyy): ")
    sesso = input("Inserisci il sesso (M/F): ").upper()
    comune = input("Inserisci il comune di nascita: ").upper()

    codice_fiscale = genera_codice_fiscale(nome, cognome, data_nascita, sesso, comune)
    print(f"Il tuo codice fiscale è: {codice_fiscale}")


if __name__ == "__main__":
    main()