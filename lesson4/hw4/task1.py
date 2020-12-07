"""
Write a script that will calculate the factorial of the entered number  without using recursion
"""
import math


def factorial(value: int):
    value_factorial = 1
    if value == 1:
        return value_factorial
    else:
        for digit in range(1, value + 1):
            value_factorial *= digit

        return value_factorial

if __name__ == '__main__':
    input_value = int(input('Enter number: '))

    print(factorial(value=input_value))