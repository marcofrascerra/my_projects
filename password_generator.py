# This program will generate a password with a number of character of your choice between 8 and 64

import string

import random


numbers = "0123456789"

symbols = "!?$?%^&*()_-+={[}]:;@#|\<,>.?/"

key = ""


def psw_creator(length):

    password = ""

    charset = string.ascii_uppercase + string.ascii_lowercase + numbers + symbols

    for i in range(length):

        password += charset[random.randrange(len(charset))]

    return password


def psw_checker(password):

    counter = 0

    for i in password:

        if i in string.ascii_uppercase:

            counter += 1

            break

    for i in password:

        if i in string.ascii_lowercase:

            counter += 1

            break

    for i in password:

        if i in numbers:

            counter += 1

            break

    for i in password:

        if i in symbols:

            counter += 1

            break

    if counter == 4:

        return True

    else:

        return False


psw_length = int(input("Insert the length of the password you want to create (the number must be between 8 and 64)\n>>> "))

if 8 <= psw_length <= 64:

    while psw_checker(key) is False:

        key = psw_creator(psw_length)

    print("Here's your password. Keep it safe! >>> " + key)

else:

    print("Enter a valid number")
