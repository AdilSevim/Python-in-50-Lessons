"""
Day 6, Example 2: Guessing Game

Purpose: Create an interactive number guessing game using a while loop.
We use a loop to keep the game running until the user guesses correctly.

Expected output when run:
I'm thinking of a number between 1 and 10.
What's your guess? [user types number]
[Too high/Too low/Correct!]
...
"""
"""
Note: To help you get used to the def structure found in C, everything written from now on will be written in this way. At the same time, this will help you lay a foundation for C and other programming languages."""

import random

def main():
    """Run a number guessing game."""
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    print("I'm thinking of a number between 1 and 10.")
    
    # Keep track of whether the user has guessed correctly
    guessed_correctly = False
    
    # Keep asking for guesses until the user is correct
    while not guessed_correctly:
        # Get the user's guess
        guess_input = input("What's your guess? ")
        guess = int(guess_input)
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Correct! You guessed it!")
            guessed_correctly = True
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


if __name__ == "__main__":
    main()
