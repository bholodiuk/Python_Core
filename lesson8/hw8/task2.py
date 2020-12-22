"""
Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел
від 1 до 100 і пропонує користувачу вгадати це число.

Програма зчитує числа, які вводить користувач і видає користувачу
підказки про те чи загадане число більше чи менше за введене користувачем.
Гра має тривати до моменту поки користувач не введе число, яке загадане програмою,
тоді друкує повідомлення привітання.
(для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())
"""
from random import randint

def init_user():
    """
    Initialize game with base args.
    :return: init_player_name   - real player name.
             init_random_number - guessed game number
    """
    init_player_name = input('Enter your name: ')

    init_random_number = randint(a=0, b=100)

    return init_player_name, init_random_number

def run_game(player_name: str, random_number: int):
    """
    Creating of game process.
    :param player_name:
    :param random_number:
    :return: None
    """
    try:
        move_counter = 0
        while True:
            player_number = int(input(f'Enter your number [{player_name}]: '))
            move_counter += 1
            if player_number == random_number:
                print(f'Congratulations {player_name}!!! You win!!!! Guessed number was -> {random_number} '
                      f'You made -> {move_counter} types')
                break
            else:
                if (player_number - random_number) > 0:
                    print(f'{player_name} you enter too big number')
                else:
                    print(f'{player_name} you enter too small number')

    except KeyboardInterrupt as keyboard_error:
        print(f'KeyboardInterrupt -> {keyboard_error}')
    except ValueError as value_error:
        print(f'ValueError -> {value_error}')
    except BaseException as base_error:
        print(f'BaseException -> {base_error}')

if __name__ == '__main__':

    user_name, secret_value = init_user()

    run_game(player_name=user_name, random_number=secret_value)

