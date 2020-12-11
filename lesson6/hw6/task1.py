"""
Write a function that returns the largest number of two numbers
(use DocStrings documentation strings in the function).
"""

def max_value(*args):
    """
    Method returns max value between 2 values.
    :parameters:
        *args: int, int - two integer values

    :return:
        max(args)
    """
    return max(args)

if __name__ == '__main__':
    value_one = int(input("Enter first value: "))
    value_two = int(input("Enter second value: "))
    print(f'Max value between {value_one} and {value_two} -> {max_value(value_one, value_two)}')