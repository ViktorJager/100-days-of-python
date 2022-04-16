from data import MENU, resources, available_coins, restocked_resources
from misc import clear
from art import logo


def off():
    print("🤖 Turning off for maintenance. Beep-bop")
    quit()


def report():
    print("📢 Report: ")
    for item in resources:
        print(f"{item.title()}\t{add_unit_to_item(item, resources)}")


def add_unit_to_item(item, resources):
    match item.lower():
        case "water" | "milk":
            return f"{resources[item]}ml"
        case "coffee":
            return f"{resources[item]}g"
        case "money":
            return f"${resources[item]}"
        case _:
            return f"{resources[item]}"


# Check that enoug resources are available to make the drink
def enough_resources_available(drink):
    required_ingredients = MENU[drink]["ingredients"]

    for ingredient in required_ingredients:
        # print(f"{ingredient} {required_ingredients[ingredient]}")
        if resources[ingredient] - required_ingredients[ingredient] <= 0:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def calculate_monetary_value(coins):
    sum = 0.0
    for coin in coins:
        sum += coins[coin] * available_coins[coin]
    return round(sum, 2)


def process_coins():
    inserted_coins = {}
    for coin in available_coins:
        number_of_coins = float(input(f"How many {coin}?: "))
        inserted_coins[coin] = number_of_coins
    return calculate_monetary_value(inserted_coins)


def calculate_change(cost, payment):
    return round(payment - cost, 2)


def add_profit(cost):
    resources["money"] = resources["money"] + cost


def check_transation(drink, payment):
    cost = MENU[drink]["cost"]
    if cost > payment:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        add_profit(cost)
        change = calculate_change(cost, payment)
        if change > 0:
            print(f"💰 Here is ${change} dollars in change")
        return True


def make_drink(drink):
    required_ingredients = MENU[drink]["ingredients"]

    for ingredient in required_ingredients:
        resources[ingredient] = resources[ingredient] - required_ingredients[ingredient]


print(logo)

while True:
    user_input = input(
        "What would you like? [espresso / latte / cappuccino / report / off]: "
    ).lower()

    match user_input:
        case "espresso" | "latte" | "cappuccino":
            drink = user_input
            if enough_resources_available(drink):
                user_payment = process_coins()

                if check_transation(drink, user_payment):
                    make_drink(drink)
                    print(f"☕ Here is your {drink}. Enjoy!")

        case "report":
            report()

        case "off" | _:
            off()
