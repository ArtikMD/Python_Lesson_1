# Charisma2 = 5.2 # double
# boolean = False # True
# print(bool(12))
# print('Hello ' + name)
# print('Your id is ' + id)
import random

# if Score == 400:
# print('You won absolutely nothing, wow good job, kys')
# else:
# print('Get back to work monkey')

lives = 3
win_Fan = random.randint(0, 6)
check = int(input('Enter your number'))

while lives != 1:
    if check == win_Fan:
        print('You won, kys')
        break
    elif check > win_Fan:
        print('Your number is more than needed')
    elif check < win_Fan:
        print('Your number is less than needed')
    else:
        print('Wrong data input')
    lives = lives - 1
    check = int(input('Enter your number'))
else:
    print('You lost monkey')