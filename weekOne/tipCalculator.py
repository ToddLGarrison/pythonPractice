print("Welcome to the Tip Calculator!!")
totalBill = int(input("What was the total bill?\n"))
tipPercent = int(input("How much of a tip would you like to give? 15, 20, 25?\n"))
numOfPeople = int(input("How many people are splitting the bill?\n"))
tipAmount = float(tipPercent / 100)
amountToPay = round(((totalBill + tipAmount)/ numOfPeople), 2)
print("Each person should pay " + str(amountToPay))