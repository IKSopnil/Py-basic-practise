import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print("Sorry,too low ...guess again.")
        elif guess > random_number:
            print("Sorry,too high ...guess again.")
    print("CONGRATS U WON")

guess(10)
"""def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high :
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} is too high(H) or too low (l) or correct (c)?').lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess + 1
    print(f"congo {guess} is right")
computer_guess(10)"""