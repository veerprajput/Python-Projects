# #Write your code below this line 👇🚨🚨🚨

player_health = 10
player_strength = 250
player_speed = 650


def drink_potion():
    global player_health
    global player_strength
    global player_speed
    player_speed += 50
    player_health += 30
    player_strength += 50
    print('You drank a power potion')

drink_potion()
drink_potion()
drink_potion()


print(f' Your health is {player_health}')
print(f' Your strength is {player_strength}')
print(f' Your speed is {player_speed}')

