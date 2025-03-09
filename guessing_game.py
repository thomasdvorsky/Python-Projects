print("🎯 Welcome to the Number Guessing Game!")
print("I have picked a random number between 1 and 100.")
print("Can you guess what it is?")

import random # Import the random module

# Generate a random number between 1 and 100
secret_number = random.randint(1,100)

# Ask the player for a guess
guess = int(input("Enter your guess (1-100_:"))

# Check if the guess is correct
if guess == secret_number:
    print("Congrats! You guessed the correct number! How did you know the number was {secret_number}? You must be a genius!🤯")
else:
    print("Wrong guess! The correct number was {secret_number}. Better luck next time!🎯")
