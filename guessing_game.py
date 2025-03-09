import random  # Import the random module

print("🎯 Welcome to the Number Guessing Game!")
print("I have picked a random number between 1 and 100.")
print("Can you guess what it is?")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Keep track of number of attempts
attempts = 0

while True:  # Infinite loop until the correct guess
    guess = int(input("Enter your guess (1-100): "))  # Ask user for a guess
    attempts += 1  # Increase attempt count

    if guess < secret_number:
        print("⬆️ Higher! Try again.")  # Hint if guess is too low
    elif guess > secret_number:
        print("⬇️ Lower! Try again.")  # Hint if guess is too high
    else:
        print(f"🎉 Congrats! You guessed the number {secret_number} in {attempts} attempts! You must be a genius! 🤯")
        break  # Exit loop when the correct number is guessed
