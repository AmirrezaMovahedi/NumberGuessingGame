import random

while True:
    try:
        minimum_number = int(input('please enter minimum number: '))
        maximum_number = int(input('please enter maximum number: '))
        break

    except ValueError:
        continue

random_number = random.randrange(minimum_number, maximum_number)
guess_chance = 10
counter = 0

while True:
    try:
        if counter != guess_chance:
            guess = int(input(f'please enter your guess [{minimum_number} to {maximum_number}]: '))
            counter += 1
            if guess == random_number:
                print(f'Congratulations! counter: {counter}')
                break
            elif guess > random_number:
                print('Try Again! You guessed too high')
            elif guess < random_number:
                print('Try Again! You guessed too small')
        else:
            print('Better Luck Next Time!')
            break

    except ValueError:
        continue
