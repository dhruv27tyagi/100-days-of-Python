import random

print("Welcome to the Number Guessing Game ")
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

print(f"I am thinking of a number. You have {lives} attempts remaining to guess the number.")

number = random.randrange(1,100)

while lives > 0:
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too High.\nGuess again.")
        lives -= 1
    elif guess < number:
        print("Too low.\nGuess again.")
        lives -= 1
    elif guess == number:
        print("Correct guess!\nYou won.")
        break    

if lives == 0:
    print("You have run out of guesses.\nYou lose.")
