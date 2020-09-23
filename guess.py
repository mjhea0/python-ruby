import random


number = random.randint(1, 20)
guesses = 0

print('Hello! What is your name?')
name = input()

print(f"Hi, {name}. I'm thinking of a number from 1 and 20.")

while guesses < 6:
    print(f'What is your guess? You have {6 - guesses} more guesses.')
    guess = input()
    guess = int(guess)

    guesses = guesses + 1

    if guess < number:
        print('Too low.')
    elif guess > number:
        print('Too high.')
    elif guess == number:
        print(f'Good job, {name}! You guessed my number in {guesses} guesses!')
        break

if guess != number:
    print(f'Nope. The number I was thinking of was {number}.')
