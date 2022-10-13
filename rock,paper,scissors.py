import random

lista = ["Carta","Forbice","Sasso"]

x = input("Scegli >>> ")

x = x.capitalize()

print(f"Tu: {x}")


def gioco(x):

    y = random.choice(lista)

    if x == y:

        print(f"Avversario: {y}\nPareggio!")

    elif y == "Sasso" and lista.index(x)-1 < 0:

        print("Avversario: Sasso\nHai vinto!")

    elif y == lista[lista.index(x)-1]:

        print(f"Avversario: {y}\nHai vinto!")

    else:

        print(f"Avversario: {y}\nHai perso!")


gioco(x)
