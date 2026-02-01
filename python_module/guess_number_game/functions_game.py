import getpass
import random
import pandas as pd
from getpass import getpass


def menu():
    menu_choice = input(
        "Welcome to the game 'Guess the Number'. These are the options: "
        "\n1. Play alone. "
        "\n2. Play 2 players. "
        "\n3. Statistics. "
        "\n4. Exit. "
        "\nChoose your option: "
    )
    return int(menu_choice)


def valid(min_val, max_val, choice):
    while choice < min_val or choice > max_val:
        choice = int(input('Invalid option, please choose a valid one: '))
    return choice


def choose_num_difficulty():
    difficulty_number = int(input(
        "Please, choose the difficulty of the number: "
        "\n1. Normal (number from 1 to 1000) "
        "\n2. Hard (number from 1 to 3000) "
        "\n3. Very Hard (number from 1 to 5000) \n"
    ))
    return difficulty_number


def max_number_possible(difficulty_number):
    if difficulty_number == 1:
        max_number = 1000
    elif difficulty_number == 2:
        max_number = 3000
    else:
        max_number = 5000
    print(f"Great! The number will be between 1 and {max_number}")
    return max_number


def num_to_guess(game_choice, max_number):
    if game_choice == 1:
        number_chosen = random.randint(1, max_number)
        return number_chosen
    elif game_choice == 2:
        number_chosen = int(getpass('Player 1: Which number do you want Player 2 to guess?: '))
        number_chosen = valid(1, max_number, number_chosen)
        print('Number registered, thank you!')
        return number_chosen


def difficulty():
    chosen_difficulty = int(input(
        "Please, choose the game difficulty: "
        "\n1. Easy (20 tries) "
        "\n2. Medium (12 tries) "
        "\n3. Hard (5 tries) \n"
    ))
    return chosen_difficulty


def chose_tries(game_difficulty):
    if game_difficulty == 1:
        tries = 20
    elif game_difficulty == 2:
        tries = 12
    else:
        tries = 5
    print(f"Registered, you have {tries} tries")
    return tries


def registering_user(tries, difficulty_option):
    user_name = input('Please, write your name to register it: ').title()
    file_name = 'c:/...xlsx'

    try:
        df = pd.read_excel(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Difficulty', 'User', 'Victories', 'Lost_games'])

    if tries > 0:
        win = 1
        lost_game = 0
    else:
        win = 0
        lost_game = 1

    new_entry = pd.DataFrame({
        'Difficulty': [difficulty_option],
        'User': [user_name],
        'Victories': [win],
        'Lost_games': [lost_game]
    })

    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_excel(file_name, index=False)

    print("Registration saved successfully")
