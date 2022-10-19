# Money Manager by Marco Frascerra

import os
import string


clear = lambda: os.system("cls")
pause = lambda: os.system("pause")


def directory_check(directory):             # Checks if the name of the directory is valid
    for letter in directory:
        if letter in "\\/:*?\"<>|":
            return False
    return True


def password_check(password):               # Check if password is strong enough
    if len(password) >= 8:
        for letter in password:
            if letter in "0123456789":
                for letter2 in password:
                    if letter2 in string.ascii_uppercase:
                        return True
    return False


def first_menu():
    clear()
    print("1. Login\n2. Registrati\n3. Esci")
    choice = input(">>> ")
    return choice


def register_menu():        # Returns True if the user insert username+password correctly, False if not
    clear()
    print("Per favore inserisci un nome utente e una password per il tuo account:")
    while True:
        username = input("Nome utente >>> ").lower()
        if os.path.exists(username + ".txt"):
            clear()
            print("Il nome utente che hai scelto esiste già. Per favore inserisci un nuovo nome utente.")
            pause()
        elif not directory_check(username + ".txt"):
            clear()
            print("Il nome utente non può contenere i seguenti caratteri: \\/:*?\"<>|")
            pause()
        elif directory_check(username + ".txt"):
            with open(username + ".txt", "w"):
                pass
            break
    while True:
        password = input("Password >>> ")
        if not password_check(password):
            clear()
            print("La password è troppo debole. Essa deve essere lunga almeno 8 caratteri, contenere almeno un numero e un carattere maiuscolo.")
            pause()
        elif password_check(password):
            while True:
                clear()
                print("Nome utente: " + username + "\nPassword: " + password)
                print("Confermi?\n1. Si\n2. No")
                answer = input(">>> ")
                if answer not in "12":
                    clear()
                    print("Per favore inserisci una risposta valida.")
                    pause()
                if answer == "1":
                    with open(username + ".txt", "a") as register:
                        register.write("Username: " + username + "\nPassword: " + password + "\nAccount balance: 0.00\nSpendable money: 0.00\n-\n1. Savings: 0.00/0.00")
                    if os.path.exists(username + ".txt"):
                        clear()
                        print("La registrazione è andata a buon fine.")
                        pause()
                        return True
                if answer == "2":
                    os.remove(username + ".txt")
                    clear()
                    print("La registrazione non è andata a buon fine.")
                    pause()
                    return False


def login_menu():       # True if login is correct, False if not
    clear()
    username = input("Nome utente >>> ")
    password = input("Password >>> ")
    if os.path.exists(username + ".txt"):
        with open(username + ".txt", "r") as account:
            for row in account:
                if "Password: " in row:
                    if password == row[10:-1]:
                        print("La password è corretta.")
                        pause()
                        with open("login_setting.txt", "w") as setting:
                            setting.write(username.lower() + "\n")
                        return username.lower()
                    else:
                        print("La password è sbagliata. Riprova.")
                        pause()
                        return False
    else:
        print("Nome utente non corretto o inesistente. Riprova.")
        pause()
        return False


def organize_in_dictionary(objective):
    dictionary = dict()
    index = objective.split(".", 1)[0]
    name = (objective.split(":")[0]).split(". ")[1]
    progress = (objective.split(": ")[1]).split("/")[0]
    target = (objective.split(": ")[1]).split("/")[1]
    dictionary["index"] = int(index)
    dictionary["name"] = name
    dictionary["progress"] = round(float(progress), 2)
    dictionary["target"] = round(float(target), 2)
    return dictionary


def dictionary_to_string(dictionary):
    my_string = str(dictionary["index"]) + ". " + dictionary["name"] + ": " + str(dictionary["progress"]) + "/" + str(dictionary["target"])
    return my_string


def store_data(user):           # Returns a list that contains all data of the user account (pos 0: username; pos 1: password; pos 2: Acc. balance; pos 3: Spend. money; pos 4: list of all objectives)
    data = list()
    targets = list()
    with open(user + ".txt", "r") as backup:
        for row in backup:
            if "Username" in row:
                data.append(row[10:-1])
            elif "Password" in row:
                data.append(row[10:-1])
            elif "Account balance" in row:
                data.append(row[17:-1])
            elif "Spendable money" in row:
                data.append(row[17:-1])
            elif row[0].isdigit():
                targets.append(organize_in_dictionary(row))
    data.append(targets)
    return data


def profile(user):
    account = store_data(user)
    for i in range(len(account)):
        if i == 2:
            print(f"Soldi totali sul conto: {float(account[i]):.2f} €")
        elif i == 3:
            print(f"\nPuoi spendere: {float(account[i]):.2f} €")
        elif i == 4:
            print("\nI tuoi obiettivi attivi:")
            for j in account[i]:
                print(f"\n{j['index']}. {j['name']}: {j['progress']:.2f}€/{j['target']:.2f}€")


def total_balance_calculator(account, you_can_spend):
    total_balance = you_can_spend
    for element in account[4]:
        total_balance += element["progress"]
    return total_balance


def account_updater(user, account, total_balance, you_can_spend):
    with open(user + ".txt", "w") as updated_account:
        updated_account.write("Username: " + account[0] + "\n")
        updated_account.write("Password: " + account[1] + "\n")
        updated_account.write("Account balance: " + str(total_balance) + "\n")
        updated_account.write("Spendable money: " + str(you_can_spend) + "\n")
        updated_account.write("-\n")
        for element in account[4]:
            updated_account.write(dictionary_to_string(element) + "\n")


def add_money(user, money):
    account = store_data(user)
    you_can_spend = float(account[3]) + round(money, 2)
    total_balance = total_balance_calculator(account, you_can_spend)
    account_updater(user, account, total_balance, you_can_spend)


def withdraw_money(user, money):                # Returns 0 if you can't afford to withdraw money, returns 1 if you can, but you have to take them from an objective, returns the money left on your account if you can afford to do it.
    account = store_data(user)
    you_can_spend = float(account[3]) - round(money, 2)
    if you_can_spend < 0:
        if float(account[2]) - round(money, 2) >= 0:
            return 1
        return 0
    else:
        total_balance = total_balance_calculator(account, you_can_spend)
        account_updater(user, account, total_balance, you_can_spend)
        return you_can_spend


def add_objective(user, name, target):
    account = store_data(user)
    new_objective = {"index": len(account[4]) + 1,
                     "name": name.capitalize(),
                     "progress": 0.0,
                     "target": target}
    account[4].append(new_objective)
    account_updater(user, account, account[2], account[3])
    print(f"L'obiettivo {name} è stato aggiunto con successo.")


def check_uniqueness(user, name_to_check):          # Returns True if the name is unique, False if not
    account = store_data(user)
    name_to_check = name_to_check.lower()
    for objective in account[4]:
        if name_to_check == objective["name"].lower():
            return False
    return True


def modify_objective(user, objective):              # Returns False if the name of the objective that the user inserted is not present in the account
    account = store_data(user)
    for obj in account[4]:
        if objective.lower() == obj["name"].lower():
            while True:
                clear()
                print("Cosa vuoi fare?\n1. Modifica nome\n2. Modifica target\n3. Annulla")
                choice = input(">>> ")
                if choice not in "123":
                    clear()
                    print("Per favore inserisci un numero da 1 a 3.")
                    pause()
                elif choice == "1":
                    clear()
                    new_name = input("Quale nome vuoi inserire?\n>>> ")
                    if check_uniqueness(user, new_name.lower()):
                        while True:
                            clear()
                            print(f"{new_name.capitalize()} andrà a sostituire {objective}. Confermi?\n1. Sì\n2. No")
                            cursor = input(">>> ")
                            if cursor not in "12":
                                clear()
                                print("Per favore inserisci 1 o 2.")
                                pause()
                            elif cursor == "1":
                                account[4][account[4].index(obj)]["name"] = new_name.capitalize()
                                account_updater(user, account, account[2], account[3])
                                return True
                    else:
                        clear()
                        print("Nome già esistente. Riprova.")
                        pause()
                elif choice == "2":
                    clear()
                    new_target = round(float(input("Quale nuovo target vuoi inserire?\n>>> ")), 2)
                    account[4][account[4].index(obj)]["target"] = new_target
                    account_updater(user, account, account[2], account[3])
                    clear()
                    print("Target aggiornato con successo.")
                    pause()
                    return True
                elif choice == "3":
                    return True
    return False


def delete_objective(user, objective):
    account = store_data(user)
    to_delete = dict()
    switch = False
    for element in account[4]:
        if objective != element["name"] and switch is False:
            continue
        elif objective != element["name"] and switch is True:
            account[4][account[4].index(element)]["index"] -= 1
        elif objective == element["name"]:
            switch = True
            to_delete = element
    account[4].remove(to_delete)
    account_updater(user, account, account[2], account[3])


def move_money(user, money, objective, mode):
    account = store_data(user)
    if mode == "put":
        if money > float(account[3]) and money > float(account[2]):
            clear()
            print("Non hai abbastanza soldi. Riprova con una cifra più piccola.")
            pause()
        elif money > float(account[3]) and money < float(account[2]):
            clear()
            print("Al momento non possiedi quella cifra tra i soldi spendibili. Riprova prelevando soldi da altri obiettivi.")
            pause()
        elif money < float(account[3]):
            you_can_spend = float(account[3]) - money
            for element in account[4]:
                if objective == element["name"]:
                    account[4][account[4].index(element)]["progress"] += money
                    account_updater(user, account, account[2], you_can_spend)
                    clear()
                    print(f"Operazione avvenuta con successo. Hai spostato {money} € sull'obiettivo {objective}")
                    pause()
    elif mode == "take":
        for element in account[4]:
            if objective == element["name"]:
                if money > element["progress"]:
                    clear()
                    print("Non puoi prelevare quella cifra. Riprova con una cifra più piccola.")
                    pause()
                else:
                    you_can_spend = float(account[3]) + money
                    account[4][account[4].index(element)]["progress"] -= money
                    account_updater(user, account, account[2], you_can_spend)
                    clear()
                    print(f"Operazione avvenuta con successo. Hai prelevato {money}€ dall'obiettivo {objective}")
                    pause()


def personal_area(user):
    # message = "Mi dispiace, questa funzione non è ancora stata aggiunta. Presto arriveranno nuovi update."
    while True:
        clear()
        print("Ciao " + user + "! Questa è la tua area personale.")
        print("1. Visualizza dettagli conto")
        print("2. Aggiungi soldi sul conto")
        print("3. Preleva soldi dal conto")
        print("4. Aggiungi obiettivo")
        print("5. Modifica obiettivo")
        print("6. Rimuovi obiettivo")
        print("7. Sposta soldi su obiettivo")
        print("8. Prendi soldi da obiettivo")
        print("9. Logout")
        print("10. Esci dal programma")
        choice = input(">>> ")
        if choice not in "12345678910":
            clear()
            print("Per favore inserisci un numero da 1 a 10.")
            pause()
        if choice == "1":
            clear()
            profile(user)
            print()
            pause()
        if choice == "2":
            clear()
            print("Quanti soldi vuoi aggiungere sul conto?")
            money = float(input(">>> "))
            add_money(user, money)
            print(f"Operazione avvenuta con successo. Sono stati aggiunti {money:.2f}€ sul tuo conto.")
            pause()
        if choice == "3":
            clear()
            print("Quanti soldi vuoi prelevare dal conto?")
            money = float(input(">>> "))
            temp = withdraw_money(user, money)
            if temp == 0:
                print("Mi dispiace, non puoi prelevare quella quantità di denaro. Prova con un'altra somma.")
                pause()
            elif temp == 1:
                print("Attualmente non puoi prelevare quella somma, ma se sposti i soldi da un obiettivo sul conto potrai farlo.")
                pause()
            else:
                print(f"Operazione andata a buon fine!\n\nPuoi spendere ancora {str(temp)} €")
                pause()
        if choice == "4":
            clear()
            print("Che nome vuoi dare al tuo obiettivo?")
            name = input(">>> ")
            clear()
            print(f"Che target vuoi mettere all'obiettivo {name}?")
            target = round(float(input(">>> ")), 2)
            if check_uniqueness(user, name.lower()):
                clear()
                add_objective(user, name.capitalize(), target)
                pause()
            else:
                clear()
                print("Non è stato possibile inserire l'obiettivo perchè il nome è già esistente. Riprova.")
                pause()
        if choice == "5":
            clear()
            print("Quale obiettivo vuoi modificare?")
            objective = input(">>> ")
            if not modify_objective(user, objective.capitalize()):
                clear()
                print(f"Non sono riuscito a trovare alcun obiettivo con il nome {objective}. Riprova.")
                pause()
        if choice == "6":
            clear()
            print("Quale obiettivo vuoi eliminare?")
            objective = input(">>> ")
            if check_uniqueness(user, objective.lower()):
                clear()
                print(f"Non esiste alcun obiettivo con il nome {objective.capitalize()}. Riprova.")
                pause()
            else:
                while True:
                    clear()
                    print(f"Stai per eliminare l'obiettivo {objective.capitalize()}. Una volta eliminato, non sarà più possibile recuperarne i dati. Sei sicuro?\n1. Sì\n2. No")
                    choice = input(">>> ")
                    if choice not in "12":
                        clear()
                        print("Per favore inserisci 1 o 2.")
                        pause()
                    elif choice == "1":
                        delete_objective(user, objective.capitalize())
                        clear()
                        print(f"Operazione avvenuta con successo. L'obiettivo {objective.capitalize()} è stato eliminato.")
                        pause()
                        break
                    elif choice == "2":
                        clear()
                        print(f"Operazione annullata con successo. L'obiettivo {objective} non è stato eliminato.")
                        pause()
                        break
        if choice == "7":
            clear()
            print("Su quale obiettivo vuoi spostare i soldi?")
            objective = input(">>> ")
            if check_uniqueness(user, objective):
                clear()
                print(f"Non esiste alcun obiettivo con il nome {objective.capitalize()}. Riprova.")
                pause()
            else:
                clear()
                print(f"Quanti soldi vuoi spostare sull'obiettivo {objective.capitalize()}?")
                money = round(float(input(">>> ")), 2)
                move_money(user, money, objective.capitalize(), "put")
        if choice == "8":
            clear()
            print("Da quale obiettivo vuoi prelevare soldi?")
            objective = input(">>> ")
            if check_uniqueness(user, objective):
                clear()
                print(f"Non esiste alcun obiettivo con il nome {objective.capitalize()}. Riprova.")
                pause()
            else:
                clear()
                print(f"Quanti soldi vuoi prelevare dell'obiettivo {objective}?")
                money = round(float(input(">>> ")), 2)
                move_money(user, money, objective.capitalize(), "take")
        if choice == "9":
            with open("login_setting.txt", "w") as setting:
                setting.write("False\n")
            clear()
            print("Logout effettuato con successo.")
            pause()
            break
        if choice == "10":
            quit()


while True:
    if os.path.exists("login_setting.txt"):
        with open("login_setting.txt", "r") as setting:
            last_login = setting.read()
            if last_login == "False\n":
                choice = first_menu()
                if choice not in "123":
                    clear()
                    print("Per favore inserisci un numero da 1 a 3.")
                    pause()
                if choice == "1":
                    user = login_menu()
                    if user is not False:
                        personal_area(user)
                elif choice == "2":
                    register_menu()
                elif choice == "3":
                    quit()
            else:
                personal_area(last_login[:-1])
    else:
        with open("login_setting.txt", "w") as setting:
            setting.write("False\n")
