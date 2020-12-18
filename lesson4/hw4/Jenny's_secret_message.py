"""
Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny,
and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

Can you help her?
"""

def greet(name):

    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

if __name__ == '__main__':
    print(greet("James"), "Hello, James!")
    print(greet("Jane"), "Hello, Jane!")
    print(greet("Jim"), "Hello, Jim!")
    print("should greet Johnny a little bit more special")
    print(greet("Johnny"), "Hello, my love!")