import random
from Score import add_score


def generate_number(difficulty_num):
    """Generate random number and save it to return secret_number"""
    secret_number = random.randrange(1, difficulty_num)
    return secret_number


def get_guess_from_user(input_string):
    """ Will prompt the user for a number between 1 to difficulty and return the number."""
    try:
        user_input_num = int(input(input_string))
    except ValueError:
        print("Value must be the number")
    else:
        return user_input_num


def compare_results(user_guessed_number, secret_number,difficulty_number):
    """ Will compare the the secret generated number to the one prompted by the get_guess_from_user."""
    if user_guessed_number == secret_number:
        add_score(difficulty_number)
        print("Your lucky bastard :)")
    elif user_guessed_number is list:
        if user_guessed_number in secret_number:
            add_score(difficulty_number)
            print("Your lucky bastard :)")
    else:
        print("Try again :(")


def play(difficulty_num):
    """ Will call the functions above and play the game. Will return True / False if the user lost or won."""
    sec_number = generate_number(difficulty_num)
    guessed_num = get_guess_from_user("Guess generated  number:")
    return guessed_num, sec_number
