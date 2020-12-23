"""
Write a program that prompts the user to enter their age, and then displays a message stating whether the age is even or odd.
The program must provide the ability to enter a negative number, and in this case generate an exception.
The master code should call a function that processes the information entered.
"""

class User:
    def __init__(self, name, age):
        self.name = name

        try:
            if age > 0:
                self.age = age
            else:
                raise CustomError('Value is negative')
        except CustomError as customer_error:
            print("We obtain error:", customer_error.data)

    def display_msg(self):
        detect = True
        if self.age % 2 == 0:
            pass
        else:
            detect = False

        return f'{self.name} -> have {"even" if detect else "odd"} age {self.age}'

class CustomError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

if __name__ == '__main__':
    try:
        input_value = input("Enter user name,age: ").split(',')
        name, age = input_value[0], int(input_value[1])
        user = User(name=name, age=age)
        print(user.display_msg())
    except ValueError as value_error:
        print(f'ValueError -> {value_error}')
    except IndexError as index_error:
        print(f'IndexError -> {index_error}')
    except AttributeError as attr_error:
        print(f'AttributeError -> {attr_error}')
