menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 4.0,
    }
}

resources = {
    "water": 3000000,
    "milk": 2000000,
    "coffee": 1000000,
}

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

def main():
    global menu
    global water
    global milk
    global coffee
    global money

    choice = input('What would you like? (espresso/latte/cappuccino): ')
    def total_money(money):
        print('Please insert coins.')
        q = int(input('How many quarters?: '))
        d = int(input('How many dimes?: '))
        n = int(input('How many nickles?: '))
        p = int(input('How many pennies?: '))
        
        money += q * 0.25
        money += d * 0.10
        money += n * 0.05
        money += p * 0.01
        
        
        return money

    def check_choice(choice1, water, milk, coffee):
        if choice1 == "espresso":
            cost = menu['espresso']['cost']
            print(f'The cost for an espresso is {cost}')
            value = total_money(money)
            if value == cost:
                print('Here is your espresso☕. Enjoy!')
                if water < 0 or milk < 0 or coffee < 0:
                    print('Sorry not enough ingredients')
                else:
                    water -= 50
                    coffee -= 18
            elif value < cost:
                print('Sorry thats not enough money. Money refunded.')
            elif value > cost:
                new_value = round(value - cost, 2)
                print(f'Here is ${new_value} in change')
                print('Here is your espresso☕. Enjoy!')
                water -= 50
                coffee -= 18
        elif choice1 == "latte":
            cost = menu['latte']['cost']
            print(f'The cost for a latte is {cost}')
            value = total_money(money)
            if value == cost:
                print('Here is your latte☕. Enjoy!')
                if water < 0 or milk < 0 or coffee < 0:
                    print('Sorry not enough ingredients')
                else:
                    water -= 200
                    milk -= 150
                    coffee -= 24
            elif value < cost:
                print('Sorry thats not enough money. Money refunded.')
            elif value > cost:
                new_value = round(value - cost, 2)
                print(f'Here is ${new_value} in change')
                print('Here is your latte☕. Enjoy!')
                if water < 0 or milk < 0 or coffee < 0:
                    print('Sorry not enough ingredients')
                else:
                    water -= 200
                    milk -= 150
                    coffee -= 24
        elif choice1 == "cappuccino":
            cost = menu['cappuccino']['cost']
            print(f'The cost for a cappuccino is {cost}')
            value = total_money(money)
            if value == cost:
                print('Here is your cappuccino☕. Enjoy!')
                if water < 0 or milk < 0 or coffee < 0:
                    print('Sorry not enough ingredients')
                else:
                    water -= 250
                    milk -= 100
                    coffee -= 24
            elif value < cost:
                print('Sorry thats not enough money. Money refunded.')
            elif value > cost:
                new_value = round(value - cost, 2)
                print(f'Here is ${new_value} in change')
                print('Here is your cappuccino☕. Enjoy!')
                if water < 0 or milk < 0 or coffee < 0:
                    print('Sorry not enough ingredients')
                else:
                    water -= 250
                    milk -= 100
                    coffee -= 24
        else:
            print('We do not sell that coffee.')

    check_choice(choice, water, milk, coffee)
    

anything = True

while anything:
    dywtga = input('Do you want to order a coffee? (Yes/No): ').lower()
    if dywtga != 'yes':
        anything = False
    else:
        main()