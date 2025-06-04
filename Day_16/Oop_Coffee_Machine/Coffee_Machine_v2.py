from mimetypes import init
from secrets import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

choice = input("What would you like? (espresso/latte/cappuccino/): ")
cm = CoffeeMaker()
water = cm.resources["water"]
milk = cm.resources["milk"]
coffee = cm.resources["coffee"]

prices = {
    'espresso': 1.5,
    'latte': 2.5,
    'cappuccino': 3,
          }

menu = Menu()
mm = MoneyMachine()
mi = MenuItem(choice, water, milk, coffee, prices[choice])



if choice == "report":
    cm.report()
elif choice == "off":
    exit()
elif choice == "espresso":
    if cm.is_resource_sufficient(mi) == True:
        print(f'The cost of a {choice} is {mi.cost}')
        if mm.make_payment(mi.cost) == True:
            cm.make_coffee(mi)
    else:
        print('Sorry')
elif choice == "latte":
    if cm.is_resource_sufficient(mi) == True:
        print(f'The cost of a {choice} is {mi.cost}')
        if mm.make_payment(mi.cost) == True:
            cm.make_coffee(mi)
    else:
        print('Sorry')
elif choice == "cappuccino":
    if cm.is_resource_sufficient(mi) == True:
        print(f'The cost of a {choice} is {mi.cost}')
        if mm.make_payment(mi.cost) == True:
            cm.make_coffee(mi)
    else:
        print('Sorry')