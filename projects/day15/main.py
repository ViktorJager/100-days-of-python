from data import MENU, resources

"""
print(resources)
resources["money"] = 10.2
print(resources)
"""


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
            return False
    return True


# Get user input from prompt
user_input = input(
    "What would you like? (espresso/latte/cappuccino) (off, report) "
).lower()

# call function on prompt input
match user_input:
    case "espresso" | "latte" | "cappuccino":
        print("Making drink") if enough_resources_available(user_input) else print(
            "Out of resources!"
        )
    case "report":
        report()
    case "off" | _:
        off()
