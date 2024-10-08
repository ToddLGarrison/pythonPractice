from menu import MENU
from resources import resources

# print(MENU["latte"]["cost"])

profit = 0

def drink_cost(drink_name):
    price = MENU[drink_name]["cost"]
    return price

def check_resources(drink_ingredients):
    can_make = True
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            can_make = False
    return can_make

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    money_sufficient = True
    if money_received <= drink_cost:
            print("Sorry, that is not enough money. Money refunded.")
            money_sufficient = False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
    return money_sufficient

def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}, enjoy your coffee")

machine_on = True

while machine_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_choice == "off":
        machine_on = False
        print("Turning machine off...")
    elif coffee_choice == "report":
        print(resources)
        print(f"Money: {profit}")
    else:
        drink = MENU[coffee_choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(coffee_choice, drink["ingredients"])


