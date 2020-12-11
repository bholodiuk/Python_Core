"""
Write a program that calculates the square of a rectangle, triangle and circle
(write three functions to calculate the square, and call them in the main program depending on the user's choice).
"""

def rectangle_square(*args):
    """
    Calculate square of rectangle.
    Formula -> Area = w × h
    :param args: two different sides.
    :return: rectangle_square.
    """
    return round(args[0] * args[1], 2)

def triangle_square(*args):
    """
    Calculate square of triangle.
    Formula -> ½ × b × h
    :param args: base-side and high.
    :return: triangle_square.
    """
    return round(0.5 * args[0] * args[1], 2)

def circle_square(*args):
    """
    Calculate square of circle.
    :param args: circle radius.
    :return: circle_square.
    """
    PI = 3.14

    return round(PI * (args[0] ** 2))

if __name__ == '__main__':
    while True:
        choice_string = input('Make your choice: Square(triangle, rectangle, circle), or exit to stop: ')

        if choice_string == 'triangle':
            # Formula -> ½ × b × h
            base_side = int(input('    Enter base side of triangle: '))
            high = int(input('    Enter high of triangle: '))
            print(f'    square -> {triangle_square(base_side, high)}')
            break
        elif choice_string == 'rectangle':
            # Formula -> Area = w × h
            side_one = int(input('    Enter first side of rectangle: '))
            side_two = int(input('    Enter second of rectangle: '))
            print(f'    square -> {rectangle_square(side_one, side_two)}')
            break
        elif choice_string == 'circle':
            # Formula -> Area = π × r2
            radius = int(input('    Enter radius of circle: '))
            print(f'    square -> {circle_square(radius)}')
            break
        else:
            if choice_string.lower() == 'exit':
                print(f'Program was stopped by typing -> {choice_string}.')
                break
            else:
                print(f'Entered choice {choice_string} is wrong!!! Make your choice again!!!.')