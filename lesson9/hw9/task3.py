"""
Color Ghost
Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
"""
import random


class Ghost(object):
    def __init__(self, color):
        self.color = random.choice(["white", "yellow", "purple", "red"])

if __name__ == '__main__':
    ghosts = [Ghost(color='white').color for _ in range(100)]
    print(ghosts.count("white") >= 1)
    print(ghosts.count("yellow") >= 1)
    print(ghosts.count("purple") >= 1)
    print(ghosts.count("red") >= 1)