import requests
from GuessGame import compare_results, get_guess_from_user
import random

api_key = 'c13ba0d0f6b91ad89f19'


def generate_number(difficulty_num):
    """Generate an interval from amount a money and difficulty level"""
    url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=" + api_key
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Connection problem")
    except requests.exceptions.HTTPError:
        print("Http response error")
    else:
        data = response.json()

    currency_rate = int(data['USD_ILS'])
    amount_of_money = random.randrange(1, 101)
    start_interval = (currency_rate * amount_of_money) - (5 - difficulty_num)
    end_interval = (currency_rate * amount_of_money) + (5 - difficulty_num)
    interval_list = list(range(start_interval, end_interval + 1, 1))
    return interval_list


def play(difficulty_num):
    interval_list = generate_number(difficulty_num)
    guess_from_user = get_guess_from_user('Guess a amount of value from USD to ILS:')
    # return compare_results(guess_from_user, interval_list, difficulty_num)
    return guess_from_user, interval_list
