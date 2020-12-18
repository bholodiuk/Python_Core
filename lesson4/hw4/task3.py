"""
Print Fibonacci numbers up to the entered number n,
using cycles.
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
"""

def fibonacci_sequence(n):
    if n > 1:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
    return n

if __name__ == '__main__':
    up_value = int(input('Enter fibonacci sequence max value '))

    for value in range(up_value):
        if fibonacci_sequence(value) <= up_value:
            print(fibonacci_sequence(value))
