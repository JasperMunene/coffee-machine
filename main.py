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

# TODO: PROMPT USER BY ASKING THEM WHAT THEY LIKE
def check_resources(drink):
    """Check if there are enough resources to make the chosen drink."""
    ingredients = MENU[drink]["ingredients"]

    for ingredient, amount_required in ingredients.items():
        if resources.get(ingredient, 0) < amount_required:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True  # This needs to be outside the loop


def check_money(drink, money):
    """Check for money required to make the chosen drink."""
    drink_money = MENU[drink]["cost"]
    if money >= drink_money:  # Allow exact payment
        print(f"Here is your change: ${round(money - drink_money, 2)}")
        return True
    else:
        print("You don't have enough money to get the drink.")
        print(f"Money refunded: ${round(money, 2)}")
        return False


def deduct_resources(drink):
    """Deduct resources used to make the drink."""
    ingredients = MENU[drink]["ingredients"]
    for ingredient, amount_required in ingredients.items():
        resources[ingredient] -= amount_required


while True:
    preference = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if preference in ['espresso', 'latte', 'cappuccino']:
        if check_resources(preference):
            print('Please insert coins')
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))

            # Calculate the total money inserted
            user_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

            # Check if the money is enough
            if check_money(preference, user_money):
                deduct_resources(preference)
                print(f"Here is your {preference}. Enjoy!")
        else:
            print(f"Cannot make {preference} due to insufficient resources.")

    elif preference == 'report':
        for item, amount in resources.items():
            print(f"{item.capitalize()}: {amount}ml")
    elif preference == 'off':
        print('Turning off...')
        break
    else:
        print('Invalid input')

