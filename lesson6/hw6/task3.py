"""
Write a function that calculates the number of characters included in a given string
"""

def string_len_calculation(input_string: str):
    """
    Calculating length of input string.
    :param input_string: length calculated value.
    :return: len(input_string) - length of input_string.
    """
    return len(input_string)

if __name__ == '__main__':
    value = input('Enter your string: ')

    print(f'{value} consist of: {string_len_calculation(input_string=value)} characters.')