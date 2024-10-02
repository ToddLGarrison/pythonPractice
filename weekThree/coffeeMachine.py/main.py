from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

joe = CoffeeMaker()

johnny = MoneyMachine()

menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        joe.report()
        johnny.report()
    else:
        drink = menu.find_drink(choice)
        if joe.is_resource_sufficient(drink) and johnny.make_payment(drink.cost):
                joe.make_coffee(drink)
