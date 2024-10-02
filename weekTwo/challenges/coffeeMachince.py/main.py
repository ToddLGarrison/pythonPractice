from menu import MENU
from resources import resources

#Coin operated - .01, .05, .10, .25

#print report - what resources are left
#check resources are sufficient when drink ordered
#take coins - calculate change - if not enough refund - if correct or more provide change
#if drink made resources are deducted

coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

machine_on = True
if coffee_choice == "off":
    machine_on = False
    print("Turning machine off...")


if coffee_choice == "report":
    print(resources)

