# Ex. 1: Save the string in a .txt file

import os

string = input("Insert a string to save it in string.txt file >>> ")

with open("string.txt", "w") as file:

    file.write(string)

with open("string.txt", "r") as file:

    temp = file.read()

path = "C:\\Users\\marco\\Desktop\\Linguaggi\\Python\\file_exercises\\string.txt"

if os.path.exists(path) and temp == string:

    print("The string was saved successfully!")

else:

    print("Something went wrong! Try again...")


# Ex. 2: Save in a file n natural numbers

n = int(input("Insert a number >>> "))

with open("numbers.txt", "w") as file:

    for i in range(n+1):

        file.write(str(i) + "\n")


# Ex. 3: Save 10 random numbers in a file and then print the numbers on the same line

import random

with open("exercise.txt", "w") as file:

    for i in range(10):

        file.write(str(random.randrange(0,100)) + "\n")

with open("exercise.txt", "r") as file:

    for line in file:

        for letter in line:

            if letter == "\n":

                print(" ", end="")

            else:

                print(letter, end="")


# Ex. 4:


def age_list(my_file):

    lista = []

    number = []

    with open(my_file, "r") as data:

        for line in data:

            for letter in line:

                if letter.isdigit():

                    number.append(letter)

                else:

                    continue

            number = "".join(number)

            number = int(number)

            lista.append(number)

            number = []

#        list.sort()        active to sort the list

    return lista


def name_list(my_file):

    lista = []

    name = []

    with open(my_file, "r") as data:

        for line in data:

            for letter in line:

                if letter.isdigit():

                    continue

                else:

                    name.append(letter)

            name.pop()

            name.pop()

            name = "".join(name)

            lista.append(name)

            name = []

    return lista


my_data = {}

counter = 0

for i in age_list("data_file.txt"):

    name = name_list("data_file.txt")[age_list("data_file.txt").index(i, counter)]

    print(name)

    if i in my_data:

        my_data[i] = my_data[i] + [name]

    else:

        my_data[i] = [name]

    counter += 1

print(my_data)


