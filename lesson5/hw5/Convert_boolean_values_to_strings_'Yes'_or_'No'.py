"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for
"""

def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

if __name__ == '__main__':
    print(bool_to_word(True), 'Yes')
    print(bool_to_word(False), 'No')