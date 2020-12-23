"""
Write a program that analyzes the entered number and, depending on the number, gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
Take into account cases of entering numbers from 8 and more, as well as cases of entering non-numerical data.
"""

if __name__ == '__main__':
    day_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    try:
        input_value = int(input('Enter number 1-7: '))
        if input_value > 0:
            raise ValueError('non-numerical data')
        print(f'{input_value} is {day_week[input_value]}')
    except TypeError as type_error:
        print(f'TypeError -> {type_error}')
    except IndexError as index_error:
        print(f'IndexError -> {index_error}')
    except ValueError as value_error:
        print(f'ValueError -> {value_error}')



