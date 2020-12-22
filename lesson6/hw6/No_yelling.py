"""
Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing.
String should be capitalized and properly spaced. Using re and string is not allowed.

Examples:

filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!
"""

def filter_words(st):
    st = st.lower()
    return st.capitalize()

if __name__ == '__main__':
    print(filter_words('HELLO world!'), 'Hello world!')
    print(filter_words('This will not pass '), 'This will not pass')