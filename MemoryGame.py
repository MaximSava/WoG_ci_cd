import random
import os
from time import sleep


def generate_sequence(difficulty_number):
    """Will generate a list of random numbers between 1 to 101. The list
    length will be difficulty."""
    random_numbers_list = random.sample(range(1, 101), difficulty_number)
    print("We going to show random numbers.Are you ready to remember numbers?")
    # Countdown and Console cleaning
    for i in range(4, 0, -1):
        print(i, end='\r')
        sleep(1)
    print(random_numbers_list)
    sleep(0.7)
    print('\n' * 200)
    os.system('cls||clear')
    return random_numbers_list


def get_list_from_user(difficulty_number):
    """Will return a list of numbers prompted from the user. The list length
    will be in the size of difficulty."""
    try:
        user_list_numbers = [int(input('Input your numbers:')) for i in range(0, difficulty_number)]
    except ValueError:
        print("Value must be the number or Enter one by one numbers")
    else:
        return user_list_numbers


def play(difficulty_num):
    gen_seq = generate_sequence(difficulty_num)
    list_from_user = get_list_from_user(difficulty_num)
    return list_from_user, gen_seq
