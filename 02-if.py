if True:
    print("It's true")
else:
    print("It's false")

age = 23
print(f'I am {age} years\' old.')

if age >= 18:
    print('I am an adult.')
    print('I will go to college.')
else:
    pring('I am a kid.')

import random

num = random.randint(1, 10)
# print(num)
your_guess = int(input('please guess a number, from 1-10'))
if your_guess == num:
    print('Congs! You got it!')
else:
    if your_guess > num:
        print('your number is too big')
    else:
        print('your number is too small')
