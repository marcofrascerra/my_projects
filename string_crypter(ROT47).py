# This program will encrypt or decrypt a string following the ROT-47 rules


ascii_char = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def encrypt(string):

    string = list(string)

    for i in range(len(string)):

        if string[i] == " ":

            continue

        if ascii_char.index(string[i]) + 46 >= 93:

            string[i] = ascii_char[ascii_char.index(string[i]) - 47]

        else:

            string[i] = ascii_char[ascii_char.index(string[i]) + 47]

    string = "".join(string)

    return string


def decrypt(string):

    string = list(string)

    for i in range(len(string)):

        if string[i] == " ":

            continue

        if ascii_char.index(string[i]) - 46 <= 0:

            string[i] = ascii_char[ascii_char.index(string[i]) + 47]

        else:

            string[i] = ascii_char[ascii_char.index(string[i]) - 47]

    string = "".join(string)

    return string


try:

    choice = int(input("What do you want to do?\n1. Encrypt\n2. Decrypt\n>>> "))

    if choice == 1:

        string = input("Insert the string you want to encrypt >>> ")

        print("Here's the encrypted string: " + encrypt(string))

    elif choice == 2:

        string = input("Insert the string you want to decrypt >>> ")

        print("Here's the decrypted string: " + decrypt(string))

    else:

        print("Please insert a valid choice.")

except ValueError:

    print("Something went wrong. Please try again.")
