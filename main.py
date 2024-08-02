import random
from art import logo


def number_range(start_point, end_point):
    """This function will return the list of numbers:
    start_point and end_point are included"""
    numbers = []
    for _ in range(start_point, end_point + 1):
        numbers.append(_)
    return numbers


def check_guess(user_guess, random_number, guesses):
    """Function will check the result of guess, and let the user
    if guess match with random number
    if guess was too high or low
    if user used all attempts and lose the game"""
    if user_guess == random_number:
        return f"You got it! The answer was {random_number}."
    if user_guess > random_number and guesses > 0:
        return "Too high. Guess again."
    if user_guess < random_number and guesses > 0:
        return "Too low. Guess again."
    else:
        return "You've run out of guesses, you lose."


print(logo)
print("Welcome to the Number Guessing Game!")

# Prepare the list of number, use the start and end points.
start = 1
end = 100
numbers = number_range(start, end)
# Randomly choose one number from the list
random_number = random.choice(numbers)
print(f"I'm thinking of a number between {start} and {end}.")
