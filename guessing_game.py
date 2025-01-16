# 1. Name:
#     Isaac Oliphant
# 2. Assignment Name:
#     Lab 01: Guessing Game
# 3. Assignment Description:
#     The computer imports a random number between 1 and 100.  It will then repeatedly ask the user for inputs until the input equals the randomly generated number.
# 4. What was the hardest part?  Be as specific as possible.
#     The hardest part was remembering how to create the random number.  Everything else was incredibly easy; I did forget to add a final append() bit to add your last guess to the list, but that was an easy fix
# 5. How long did it take for you to complete the assignment?
#     Fifteen minutes.

from random import randint

print('This is the "guess a number" game.')
print('You try to guess a random number in the smallest number of attempts.')
print('')

# Set 1, guess 1
# Set 1, guess 0, 2, 1
# Set 10, play
# Set 50, play


#number = 1
#number = randint(1, 10)
number = randint(1, 50)
guess = int(input('Pick a number between 1-100: '))
guess_list =[]
guess_count = 1

while guess != number:
    guess_list.append(guess)
    guess_count += 1
    if guess > number:
        guess = int(input('     Too high!  Try again: '))
    elif guess < number:
        guess = int(input('     Too low!  Try again: '))

guess_list.append(guess)
print(f'Correct!  The number was {number}.')
print(f'It took you {guess_count} tries.')
print(f'Your guesses were {guess_list}')