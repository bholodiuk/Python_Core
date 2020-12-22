"""
Create a polygon class and a rectangle class
that inherits from the polygon class and finds the square of rectangle.
"""

class Polygon:

    def __init__(self, name: str, no_of_sides):
        self.name = name
        self.no_of_sides = no_of_sides
        self.sides = [0] * no_of_sides

    def __repr__(self):
        return f'{self.name} -> {str(self.sides)}'

    def input_sides(self):
        """
        Initialize Polygon sides length.
        :return: initialized polygon
        """
        print(f'Enter {self.name} sides')
        temp_list = []
        for index, side in enumerate(self.sides, start=1):
            temp_list.append(int(input(f'Enter side {index}: ')))

        self.sides = temp_list


class Rectangle(Polygon):
    """
    Class determined property of Rectangle(kind of Polygon).
    """

    def area_calculate(self):
        """
        Calculate rectangle area.
        :return: rectangle area
        """
        a, b, c, d = self.sides
        return f'{self.name} area = {a * b}'

if __name__ == '__main__':
    rectangle1 = Rectangle(name='Rectangle', no_of_sides=4)
    rectangle1.input_sides()
    print(rectangle1.area_calculate())