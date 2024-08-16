print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age >= 10:
        print("The ticket price is $10")
    else:
        print("The ticket price is $8")
else:
    print("Sorry, you are too short and can't ride the rollercoaster")