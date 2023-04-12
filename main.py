import random

print("Welcome to the Number Guessing Game!!")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

choice = False
while choice == False:
    if difficulty.lower() == "easy" or difficulty.lower() == "hard":
        choice = True
    else:
        difficulty = input("Invalid Entry. Choose a difficulty again. Type 'easy or 'hard': ")

if difficulty.lower() == "easy":
    guess_remaining = 10
elif difficulty.lower() == "hard":
    guess_remaining = 5

game_end = False
while game_end == False:
    print(f"You have {guess_remaining} attempt(s) remaining.")
    choice = False
    while choice == False:
        try:
            guess = int(input("Make a guess: "))
            choice = True

        except ValueError:
            print("Guess must be a number")

    if guess_remaining == 1:
        print("I'm sorry. You've ran out of attempts")
        game_end = True
    elif guess == number:
        print(f"Congratulations, you've guessed correctly!! The number is {guess}!!")
        game_end = True
    elif guess < number:
        print("Too low. \nGuess again.")
        guess_remaining -= 1
    elif guess > number:
        print("Too high. \nGuess again")
        guess_remaining -= 1
    else:
        print("Invalid Entry")
