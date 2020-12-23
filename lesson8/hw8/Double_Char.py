"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "
"""

def double_char(s: str):
    return ''.join(s*2 for s in s)


if __name__ == '__main__':
    print(double_char("String"), "SSttrriinngg")
    print(double_char("Hello World"), "HHeelllloo  WWoorrlldd")
    print(double_char("1234!_ "), "11223344!!__  ")