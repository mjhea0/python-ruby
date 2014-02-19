import random
import os

number = random.randint(1, 20)
guesses = 0

print 'Hello! What is your name?'
name = raw_input()

print "Hi, {}. I'm thinking of a number from 1 and 20.".format(name) 

while guesses < 6:

    print 'What is your guess. You have {} more guesses.'.format(6-guesses)
    guess = raw_input()
    guess = int(guess)

    guesses = guesses + 1

    if guess < number:
        print 'Too low.'
    elif guess > number:
        print 'Too high.'
    elif guess == number:
        print 'Good job, {}! You guessed my number in {} guesses!'.format(name,guesses)
        break

if guess != number:
    print 'Nope. The number I was thinking of was {}.'.format(number)
