MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
PENNY_VALUE = 0.01


def check_resources(order):
    """Returns False is ingredients are insufficient for an order"""

    order_ingredients = MENU[order]["ingredients"]

    is_sufficient_resource = True

    message = "Sorry, there is not enough "
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            message += ingredient + ", "
            is_sufficient_resource = False

    if not is_sufficient_resource:
        print(f"{message[: len(message) - 2]}.")

    return is_sufficient_resource


def print_report():
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}gm\n"
          f"Money: ${profit}")


def is_transaction_successful(paid_amt, drink_cost):
    """Returns False if payment amount is insufficient"""

    is_tran_success = True

    if paid_amt < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        is_tran_success = False
    elif payment > cost:
        print(f"Here is ${round(payment - cost, 2)} in change.")
        is_tran_success = True
    else:
        is_tran_success = True

    return is_tran_success


def make_coffee(drink):
    """Deduct used ingredients from resources"""
    order_ingredients = MENU[drink]["ingredients"]

    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here's your {drink}! ☕")


def calculate_money(qtr, dime, nickle, penny):
    total_value = qtr * QUARTER_VALUE + dime * DIME_VALUE + nickle * NICKEL_VALUE + penny * PENNY_VALUE
    print(f"That's a total of {total_value}")
    return total_value


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False

    if choice == "report":
        print_report()
    else:
        if check_resources(choice):
            print("Please insert coins")
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickels = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))

            payment = calculate_money(quarters, dimes, nickels, pennies)
            cost = MENU[choice]["cost"]

            if is_transaction_successful(payment, cost):
                make_coffee(choice)
                profit += cost
