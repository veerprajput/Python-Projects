print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

signs = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    
}
def calculator():
    true = True
    num1 = float(input("What's the first number?: "))
    for i in signs:
        print(i)

    while true:
        sign = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        function = signs[sign]
        num3 = function(num1, num2)
        print(f"{num1} {sign} {num2} = {num3}")
        
        y = input('Do you want to go again? Type y for yes, n for no or type new for fresh new calculator? ').lower()

        print(f'{num1} {sign} {num2} = {num3}')
        if y == 'y':
            num1 = num3 
        elif y == 'new':
            calculator()
        else:
            break

calculator()