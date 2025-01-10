# Definizione della funzione
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz!!!")
        elif i % 3 == 0:
            print("Fizz!")
        elif i % 5 == 0:
            print("Buzz!")
        else:
            print(i)

# Input del numero da parte dell'utente
num = int(input("Inserisci un numero da FizzBuzz-are: "))
# Chiamata della funzione
fizz_buzz(num)