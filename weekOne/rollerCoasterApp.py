print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket price is $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket price is $7")
    elif age >= 45 and age <= 55:
        print("Midlife crisis ticket is free")
    else:
        bill = 10
        print("Adult ticket price is $10")

    want_ticket = input("Do you want a ticket for an added $3? Enter y for yes or n for no ")

    if want_ticket == "y":
        bill += 3
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
else:
    print("Sorry, you are too short and can't ride the rollercoaster")