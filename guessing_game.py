print("🎯 Welcome to the Number Guessing Game!")
print("I have picked a random number between 1 and 100.")
print("Can you guess what it is?")

import random # Import the random module

# Generate a random number between 1 and 100
secret_number = random.randint(1,100)

# Debugging line (remove later) - Shows the secret number for testing
print(f"(Debug: The secret number is {secret_number})")

# Ask the player for a guess
guess = int(input("Enter your guess (1-100_:"))

# Check if the guess is correct
if guess == secret_number:
    print("Congrats! You guessed the correct number!")
  Else:
    print("Wrong guess! Try again next time.")
