import art
import random


def guessthename(number_to_guess):
    print(art.logo)

    print("Welcome to the Guess the Name!")

    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Typer 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    print(f"You have {lives} attempts to guess the name.")

    while True:
        while lives > 0:
            guess = 0
            valid = False
            while not valid:
                try:
                    guess = int(input("Make a guess: "))
                    if 1<=guess<=100:
                        valid = True
                    else:
                        print("Please enter a number between 1 and 100.")

                except ValueError:
                    print("That's not a number!")


            if guess > number_to_guess:
                print("Your guess is too high.")
                lives -= 1
                print("Guess again.")
                print(f"You have {lives} attempts to guess the name.")
            elif guess < number_to_guess:
                print("Your guess is too low.")
                lives -= 1
                print("Guess again.")
                print(f"You have {lives} attempts to guess the name.")
            else:
                print("You guessed RIGHT!")
                return
        print("You couldn't guess the name.")
        return

game = True
while game:
    number_random = random.randint(1, 100)
    guessthename(number_random)
    game = input("Do you want to play again? (y/n): ").lower()
    if game == 'n':
        game = False
    print("\n"*20)