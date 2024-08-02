import random
from art import logo


def number_range(start_point, end_point):
    """This function will return the list of numbers:
    start_point and end_point are included"""
    numbers = []
    for _ in range(start_point, end_point + 1):
        numbers.append(_)
    return numbers


def check_guess(user_guess, choosen_number, guesses):
    """Function will check the result of guess, and let the user
    if guess match with random number
    if guess was too high or low
    if user used all attempts and lose the game"""
    if user_guess == choosen_number:
        return f"You got it! The answer was {choosen_number}."
    if user_guess > choosen_number and guesses > 0:
        return "Too high. Guess again."
    if user_guess < choosen_number and guesses > 0:
        return "Too low. Guess again."
    else:
        return (f"You've run out of guesses, you lose. The answer was"
                f" {choosen_number}")


def game():
    """Guessing Number Game"""
    print(logo)
    print("Welcome to the Number Guessing Game!")

    # Prepare the list of number, use the start and end points.
    start = 1
    end = 100
    numbers = number_range(start, end)

    # Randomly choose one number from the list
    random_number = random.choice(numbers)
    print(f"I'm thinking of a number between {start} and {end}.")

    # Game level, easy 10 guesses, hard 5 guesses
    attempts = 0
    if input("Choose a difficulty, type 'easy' or 'hard \n") == "easy":
        attempts = 10
    else:
        attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")

    # Guessing until the attempts > 0
    while attempts > 0:
        attempts -= 1
        guess = int(input("Make a guess: "))
        if guess == random_number:
            attempts = 0
            print(check_guess(user_guess=guess, choosen_number=random_number,
                              guesses=attempts))
        else:
            print(check_guess(user_guess=guess, choosen_number=random_number,
                              guesses=attempts))


game()
# Ask the user if would like to play again
if input("Play again? Type 'y' or 'n \n") == "y":
    game()
