"""
Task1.
Write a Python program to check the validity of a password (input from users).

Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""
import re

def password_validation(secure_string: str):
    """
    Check if input string is required
    :param secure_string:  - input string value
    :return: True if input string
    """
    if 6 <= len(secure_string) <= 16:
        if re.findall("[a-z]", secure_string) and \
                re.findall("[A-Z]", secure_string) and \
                re.findall("[0-9]", secure_string) and \
                re.findall("[$#@]", secure_string):

            print('Password valid')
            return True
        else:
            print('Password not valid')
            return False
    else:
        print('Password not valid')
        return False

if __name__ == '__main__':
    input_string = input('Enter password: ')

    print(password_validation(secure_string=input_string))