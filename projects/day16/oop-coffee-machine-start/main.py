from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def handle_order(user_input):
    drink = menu.find_drink(user_input)
    drink_cost = float(drink.cost)

    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink_cost):
            coffee_maker.make_coffee(drink)
        else:
            return
    else:
        return


while True:
    user_input = input(f"What would you like? {menu.get_items()}: ").lower()

    match user_input:
        case "espresso" | "latte" | "cappuccino":
            handle_order(user_input)

        case "report":
            coffee_maker.report()
            money_machine.report()

        case "off" | _:
            coffee_maker.off()
