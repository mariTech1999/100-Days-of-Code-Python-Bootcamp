from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem, Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

on = True

while on:

    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
