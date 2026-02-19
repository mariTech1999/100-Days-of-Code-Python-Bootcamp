import coffee_machine

total_resources = coffee_machine.resources
menu = coffee_machine.MENU

def report():
    print(f"Water: {total_resources["water"]}ml"
          f"\nMilk: {total_resources["milk"]}ml"
          f"\nCoffee: {total_resources["coffee"]}g")

def verify_ingredient(answer):
    ingredients = menu[answer]["ingredients"]
    for item in ingredients:
        if total_resources[item] < coffee_machine.MENU[answer]["ingredients"][item]:
            print(f"Sorry, there is not enought {item}")
            return False
    return True

def sub_ingredient(answer):
    ingredients = menu[answer]["ingredients"]
    for item in ingredients:
        total_resources[item] -= ingredients[item]

def calc_exchange(answer):
    print("Please insert coins: ")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

    if menu[answer]["cost"] > total:
        print("Sorry that's not enough money. Money refunded...")
        return False

    elif menu[answer]["cost"] == total:
        return True

    else:
        sub_ingredient(answer)
        change = total - menu[answer]["cost"]
        report()
        print(f"Cost: ${menu[answer]["cost"]}")
        print(f"Here is ${change:.2f} in change.")

        return True


online = True
while online:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == "report":
        report()

    elif answer in ["espresso", "latte", "cappuccino"]:
        if verify_ingredient(answer):
            if calc_exchange(answer):
                print(f"Here is your {answer}!")

    elif answer == "off":
        online = False

    else:
        print("Invalid input!")

