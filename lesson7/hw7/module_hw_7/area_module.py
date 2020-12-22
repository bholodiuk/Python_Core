from math import pow, pi

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
    return round(pi * pow(args[0], 2))


