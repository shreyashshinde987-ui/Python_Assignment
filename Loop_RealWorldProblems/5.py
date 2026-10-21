'''
Mini Project 5: Number Guessing Game
'''
secret = 37
max_attempts = 5
attempts = 0
won = False

print("Guess the secret number! You have", max_attempts, "attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        won = True
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

print("\n----- GAME RESULT -----")
if won:
    print("Congratulations! You guessed the number.")
else:
    print("You lost! The secret number was", secret)
print("Attempts Used:", attempts)
