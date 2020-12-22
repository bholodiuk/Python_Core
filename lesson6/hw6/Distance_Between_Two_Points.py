"""
Given two ordered pairs calculate the distance between them. Round to two decimal places.
This should be easy to do in 0(1) timing.
"""
from math import dist
def distance(x1, y1, x2, y2):
    return round(dist([x1, y1], [x2, y2]), 2)

if __name__ == '__main__':
    print(distance(1, 1, 0, 0), 1.41)
    print(distance(1, 4, 0, 2), 2.24)