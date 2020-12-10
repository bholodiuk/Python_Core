"""
In the range from 1 to 10 determine
even numbers that are divisible by 2,
odd numbers, which are divisible by 3,
numbers that are not divisible by 2 and 3.
"""

def numbers_determination():
    for digit in range(1, 11):
        if digit % 2 == 0:
            print(f'{digit} is even')
        elif digit % 3 == 0:
            print(f'{digit} is odd')
        else:
            print(f'{digit} is not divisible by 2 and 3')


if __name__ == '__main__':
    numbers_determination()