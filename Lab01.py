# 1. Name: 
#    Braint Wooley
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program is ment to guess a number
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part of this lab for me was getting back into the rythm of writing in python again.
#    It also was very difficult for me to figure out loops again. It took me several times to figure out whayt loop to use.
#    I aslo had a hard time trouble shooting and debugund the lab. This was esspically with the random number and getting that to work with the game.
# 5. How long did it take for you to complete the assignment?
#    It took me about 4 hours to complete and submit the assignment  

import random

def number_game():
    # Game introduction.
    print('This is a "guess the number" game.')
    print('You are gonna try to guess a random number in the smallest ammount of attempts.')
    # Prompt the user for how difficult the game will be. Ask for an integer.
    value_max = input('\nPlease pick a Positive integer: ')
    # Generate a random number between 1 and the chosen value.
    value_random = random.randint(1, int(value_max))
    # Give the user instructions as to what he or she will be doing.
    print('You shall be guessing a number from the number you picked')
    # Store the number in an array so it can be displayed later.
    guesses = []
    attempts = 0


    print(f"I am thing of a number bwtween 1 and {value_max}.")
    # Play the guessing game.
    while True:
        # Prompt the user for a number.
        input_of_user = input('\nPlease enter in a number: ')
            
        try:
            # Initialize the sentinel and the array of guesses.
            guess = int(input_of_user)
            guesses.append(guess)
            attempts += 1
            # Make a decision: was the guess too high, too low, or just right.
            if guess < value_random:
                print("     Your guess is to low.")
            elif guess > value_random:
                print("     Your guess was to high.")
            else:
                # Give the user a report: How many guesses and what the guesses where.
                print(f"Congrats you guessed the number in {attempts} attempt(s)! The number was {guess}")
                print("The numbers you guessed were:", guesses)
                break
        except ValueError:
            print("Please enter a valid guess.")

if __name__ == '__main__':
    number_game()