# This program will tell you your exact age in years, months, days, hours, minutes, seconds, by your choice

import datetime


error = "Please insert a valid date"


def set_age(today, birth):

    age = {
        "year": int(today["year"]) - int(birth["year"]),
        "month": int(today["month"]) - int(birth["month"]),
        "day": int(today["day"]) - int(birth["day"]),
        "hour": int(today["hour"]) - int(birth["hour"]),
        "minute": int(today["minute"]) - int(birth["minute"]),
        "second": int(today["second"]) - int(birth["second"])
    }

    if age["day"] < 0:
        age["month"] -= 1
        age["day"] = 30 + age["day"]

    if age["month"] < 0:
        age["year"] -= 1
        age["month"] = 12 + age["month"]

    return age


def input_birth():

    print("Please insert your date of birth")

    date = {
        "year": input("Year: "),
        "month": input("Month: "),
        "day": input("Day: "),
        "hour": 0,
        "minute": 0,
        "second": 0
    }

    if int(date["year"]) < 0 or int(date["month"]) <= 0 or int(date["day"]) <= 0:
        print(error)

    elif int(date["year"]) > int(current_date["year"]) or int(date["month"]) > 12 or int(date["day"]) > 31:
        print(error)

    elif int(date["year"]) == int(current_date["year"]) and int(date["month"]) > int(current_date["month"]):
        print(error)

    elif int(date["year"]) == int(current_date["year"]) and int(date["month"]) == int(current_date["month"]) and int(date["day"]) > int(current_date["day"]):
        print(error)

    elif int(date["month"]) in [4, 6, 9, 11]:

        if int(date["day"]) > 30:
            print(error)

        else:
            return date

    elif int(date["month"]) == 2:

        if int(date["year"]) % 4 == 0 and int(date["day"]) > 29:
            print(error)

        elif int(date["year"]) % 4 != 0 and int(date["day"]) > 28:
            print(error)

        else:
            return date

    else:
        return date


def conv_months(age):

    age["month"] += age["year"] * 12

    age["year"] = 0

    return age


def conv_days(age):

    age = conv_months(age)

    age["day"] += age["month"] * 30

    age["month"] = 0

    return age


def conv_hours(age):

    age = conv_days(age)

    age["hour"] += age["day"] * 24

    age["day"] = 0

    return age


def conv_minutes(age):

    age = conv_hours(age)

    age["minute"] += age["hour"] * 60

    age["hour"] = 0

    return age


def conv_seconds(age):

    age = conv_minutes(age)

    age["second"] += age["minute"] * 60

    age["minute"] = 0

    return age


current_time = datetime.datetime.now()

current_date = {
    "year": str(current_time)[:4],
    "month": str(current_time)[5:7],
    "day": str(current_time)[8:10],
    "hour": str(current_time)[11:13],
    "minute": str(current_time)[14:16],
    "second": str(current_time)[17:19]
}

bday = input_birth()

if bday is not None:

    my_age = set_age(current_date, bday)

    choice = int(input("Select a format for your age\n1. Years\n2. Months\n3. Days\n4. Hours\n5. Minutes\n6. Seconds\nYour choice: "))

    if choice in [1, 2, 3, 4, 5, 6]:

        if choice == 1:
            print(f"You are {my_age['year']} years, {my_age['month']} months, {my_age['day']} days, {my_age['hour']} hours,", end=" ")
            print(f"{my_age['minute']} minutes and {my_age['second']} seconds old")

        elif choice == 2:
            my_age = conv_months(my_age)
            print(f"You are {my_age['month']} months, {my_age['day']} days, {my_age['hour']} hours,", end=" ")
            print(f"{my_age['minute']} minutes and {my_age['second']} seconds old")

        elif choice == 3:
            my_age = conv_days(my_age)
            print(f"You are {my_age['day']} days, {my_age['hour']} hours, {my_age['minute']} minutes and {my_age['second']} seconds old")

        elif choice == 4:
            my_age = conv_hours(my_age)
            print(f"You are {my_age['hour']} hours, {my_age['minute']} minutes and {my_age['second']} seconds old")

        elif choice == 5:
            my_age = conv_minutes(my_age)
            print(f"You are {my_age['minute']} minutes and {my_age['second']} seconds old")

        else:
            my_age = conv_seconds(my_age)
            print(f"You are {my_age['second']} seconds old")

    else:
        print("Insert a valid choice")
