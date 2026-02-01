# Juego: Adivina el número
# Requisitos:
# - Python
# - Librerías: random, pandas, matplotlib, openpyxl
# Este codigo crea un archivo en : c:/EjerciciosPython/records_adivina_numero.xlsx

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import functions_game as f_j

# Game: Guess the Number
# Requirements:
# - Python
# - Libraries: random, pandas, matplotlib, openpyxl
# This code creates a file in: c:/PythonExercises/guess_number_records.xlsx

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import functions_game as f_g

game_on = True

while game_on:
    game_option = f_g.menu()
    game_option = f_g.valid(1, 4, game_option)

    if game_option == 1 or game_option == 2:

        game_difficulty = f_g.difficulty()
        game_difficulty = f_g.valid(1, 3, game_difficulty)

        number_difficulty = f_g.choose_num_difficulty()
        number_difficulty = f_g.valid(1, 3, number_difficulty)

        max_number = f_g.max_number_possible(number_difficulty)

        tries = f_g.chose_tries(game_difficulty)
        number_to_guess = f_g.num_to_guess(game_option, max_number)

        print(f"Game recap: option {game_option}, {tries} tries, "
              f"number to guess is between 1 and {max_number}")

        while tries > 0:
            try:
                guess = int(input("Guess the number: "))
            except ValueError:
                print('Invalid input, please enter only numbers.')
                continue

            if guess == number_to_guess:
                print("Congratulations! You guessed it!")
                break
            elif guess > number_to_guess:
                print("Your number is higher, try again!")
                tries -= 1
                print(f"Remaining tries: {tries}")
            else:
                print("Your number is lower, try again!")
                tries -= 1
                print(f"Remaining tries: {tries}")

        f_g.registering_user(tries=tries, difficulty_option=game_difficulty)

    elif game_option == 3:
        try:
            df = pd.read_excel('c:/PythonExercises/guess_number_records.xlsx')
            print('Three charts will be displayed for the three difficulty levels:\n'
                  'Easy\n'
                  'Medium\n'
                  'Hard\n')

            groups = [
                (1, 'Easy Level Ranking', 'green'),
                (2, 'Medium Level Ranking', 'orange'),
                (3, 'Hard Level Ranking', 'red')
            ]

            groups = [(n, t, c) for n, t, c in groups if not df[df['Difficulty'] == n].empty]

            fig, axs = plt.subplots(1, len(groups), figsize=(6 * len(groups), 6))
            if len(groups) == 1:
                axs = [axs]

            for ax, (level, title, color) in zip(axs, groups):

                df_group = df[df['Difficulty'] == level]

                grap = df_group.groupby('User', as_index=False).Victories.sum()

                grap = grap.sort_values('Victories', ascending=False).head(5)

                ax.bar(grap['User'], grap['Victories'], color=color)
                ax.set_title(title)
                ax.set_xlabel('Users')
                ax.set_ylabel('Victories')

                ax.yaxis.set_major_locator(MaxNLocator(integer=True))
                if not grap.empty:
                    ax.set_ylim(0, grap['Victories'].max() + 1)

            plt.tight_layout()
            plt.show()

        except FileNotFoundError:
            print('Try again later, no statistics available yet.')

    else:
        print('Goodbye, thank you for playing!')
        game_on = False
