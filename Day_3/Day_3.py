# #Write your code below this line 👇🚨🚨🚨
# # #Conditionals

print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm?'))
bill = 0


if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age in years?'))
    if age > 18:
        print('Adult tickets are 12$')
        bill = 12
    elif age < 12:
        print('Child tickets are 5$')
        bill = 5
    elif age >= 45 and age <= 55:
        print('Everything is going to be ok. Have a free ride')
    else:
        print('Youth tickets are 7$')
        bill = 7
    wants_photo = input('Do you want a photo taken? Y or N').lower()
    if wants_photo == 'y':
        bill += 3
        
    print(f'Your final bill is {bill}$')
        
else:
    print("Sorry, you have to grow taller before you can ride.")

# # #Even or Odd
# # number = int(input("Which number do you want to check? "))

# # if number % 2 == True:
# #     print('This is an odd number.')
# # else:
# #     print('This is an even number')

# #Leap Year or not leap year.
# # year = int(input("Which year do you want to check? "))

# # if year % 4:
# #     print('Not leap year.')
# # elif year / 4:
# #     if year / 100:
# #         if year / 400:
# #             print('Leap year.')
# #         else:
# #             print('Not a leap year.')
# #     else:
# #         print('Not a leap year.')

# # print('Welcome to Python Pizza Deliveries!')
# # size = input("What size pizza do you want? S, M, or L ")
# # add_pepperoni = input("Do you want pepperoni? Y or N ")
# # extra_cheese = input("Do you want extra cheese? Y or N ")

# # bill = 0
# # if size == 'S':
# #     bill += 15
# # elif size == 'M':
# #     bill += 20
# # else:
# #     bill += 25
# # if add_pepperoni == 'Y' and size == 'S':
# #     bill += 2
# # elif add_pepperoni == 'Y':
# #     bill += 3
# # if extra_cheese == 'Y':
# #     bill += 1
# # print(f'Your final bill is: ${bill}')