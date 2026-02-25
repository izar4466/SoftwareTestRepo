# lets play a random number gussing game
import random
a = random.randint(1, 100)
print("Welcome to the random number guessing game!")
print("I have selected a random number between 1 and 100. Can you guess it?")
while True:
    guess = int(input("Enter your guess: "))
    if guess < a:
        print("Too low! Try again.")
    elif guess > a:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
    
    