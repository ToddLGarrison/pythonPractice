print("Welcome to Python Pizza!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "L":
    bill += 25
elif size == "M":
    bill += 20
else:
    bill += 15

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print (f"Your total bill is ${bill}")