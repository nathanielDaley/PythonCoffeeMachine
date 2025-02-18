# -----------------------------
# Global variables
# -----------------------------
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
VALID_USER_INPUTS = ["espresso", "latte", "cappuccino", "off", "report"]
VALID_USER_MONEY_INPUTS = ["quarter", "dime", "nickle", "penny"]

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


# --------------------------
# Define functions
# --------------------------
def print_report(resources_to_print, profit_to_print):
    """prints what is in the coffee machine and the days profit."""
    print(f"Water: {resources_to_print["water"]}")
    print(f"Milk: {resources_to_print["milk"]}")
    print(f"Coffee: {resources_to_print["coffee"]}")
    print(f"Money: ${profit_to_print}")


def make_drink(drink_type, resources_to_use):
    if "water" in MENU[drink_type]["ingredients"]:
        resources_to_use["water"] -= MENU[drink_type]["ingredients"]["water"]
    if "milk" in MENU[drink_type]["ingredients"]:
        resources_to_use["milk"] -= MENU[drink_type]["ingredients"]["milk"]
    if "coffee" in MENU[drink_type]["ingredients"]:
        resources_to_use["coffee"] -= MENU[drink_type]["ingredients"]["coffee"]

    return resources_to_use


def get_user_input():
    u_input = input("What would you like? Type \"espresso\" \"latte\" or \"cappuccino: ").lower()
    while not u_input in VALID_USER_INPUTS:
        print("Invalid input")
        u_input = input("What would you like? Type \"espresso\" \"latte\" or \"cappuccino: ").lower()

    return u_input

def get_money():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_enough_resources(drink, resources_to_check):
    if "water" in MENU[drink]["ingredients"] and resources_to_check["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif "milk" in MENU[drink]["ingredients"] and resources_to_check["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif "coffee" in MENU[drink]["ingredients"] and resources_to_check["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False

    return True



# -----------------------------------
# Main code
# -----------------------------------
machineOn = True
while machineOn:
    user_input = get_user_input()

    if user_input == "off":
        machineOn = False
    elif user_input == "report":
        print_report(resources, profit)
    elif user_input == "espresso" or user_input == "latter" or user_input == "cappuccino":
        if check_enough_resources(user_input, resources):
            user_money = get_money()
            drink_cost = MENU[user_input]["cost"]
            if user_money > MENU[user_input]["cost"]:
                print(f"Here is ${round(user_money - drink_cost, 2) } in change.")
                make_drink(user_input, resources)
                profit += drink_cost
                print(f"Here is your {user_input}!")
            elif user_money == drink_cost:
                make_drink(user_input, resources)
                profit += drink_cost
                print(f"Here is your {user_input}!")
            else:
                print(f"Sorry that's not enough money. Money refunded.")

            user_money = 0
