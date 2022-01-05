import CurrencyRouletteGame
import GuessGame
from GuessGame import get_guess_from_user
import MemoryGame
from GuessGame import compare_results



def welcome(name):
    """Game's welcome message """
    str_welcome = r'Hello ' + name + ' and welcome to the World of Games(WoG).' \
                                     '\nHere you can find many cool games to play.\n'
    return str_welcome


def load_game():
    """Choose  games option menu"""
    choose_options_message = r'Please choose a game to play:''\n' \
                             r'       1.Memory game - a sequence of numbers appear for 1 second and you have to''\n' \
                             'guess is back\n' \
                             r'       2.Guess Game - guess a number and see if you chose like the computer''\n' \
                             r'       3.Currency Roulette - try and guess the value of a random of USD in ILS''\n:'

    selected_game_option = get_guess_from_user(choose_options_message)

    if 1 <= selected_game_option <= 3:
        selected_dificulty_option = get_guess_from_user('Please choose game difficulty from 1 to 5:')
        if 1 <= selected_dificulty_option <= 5:
            if selected_game_option == 1:
                results = MemoryGame.play(selected_dificulty_option)
                compare_results(results[0], results[1], selected_dificulty_option)
            elif selected_game_option == 2:
                results = GuessGame.play(selected_dificulty_option)
                compare_results(results[0], results[1], selected_dificulty_option)

            elif selected_game_option == 3:
                results = CurrencyRouletteGame.play(selected_dificulty_option)
                compare_results(results[0], results[1], selected_dificulty_option)
        else:
            print("Please enter number between 1-5")
    else:
        print("Please enter number between 1-3")