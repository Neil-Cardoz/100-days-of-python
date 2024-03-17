from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemachine = CoffeeMaker()
mullah = MoneyMachine()
on = True

while on:
    itm = menu.get_items()
    choice = input(f"What would u like? {itm}")
    print(f"You choose {choice}")
    if choice == "off":
        on = False
    elif choice == "report":
        coffeemachine.report()
        mullah.report()
    else:
        drink = menu.find_drink(choice)
        print(f"It costs {drink.cost}")

        sufficient = coffeemachine.is_resource_sufficient(drink)
        if not sufficient:
            print("Sorry it is out of stock")
        else:
            print("Sure")
            if mullah.make_payment(drink.cost):
                coffeemachine.make_coffee(drink)




