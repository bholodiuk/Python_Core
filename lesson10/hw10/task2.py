"""
Write a program that analyzes the entered number and, depending on the number, gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
Take into account cases of entering numbers from 8 and more, as well as cases of entering non-numerical data.
"""


def day_of_week(day):
    day_week = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    try:
        if type(day) != int:
            raise Exception("You did not enter a number! Please try again.")
        elif not 0 < day <= 7:
            raise Exception("There is no such day of the week! Please try again.")
        return f'{day_week[day]}'
    except Exception as error:
        return f'{error}'

if __name__ == '__main__':
    print(day_of_week("6"))

def is_day_of_week(day):
    check_result = True
    try:
        int(day)
    except ValueError:
        check_result = False
    return check_result


def day_of_week(day):
    week_day = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Tuesday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        if is_day_of_week(day):
            return week_day[day]
    except KeyError:
        return "There is no such day of the week! Please try again."


##############################
def check_odd_even(number):
    try:
        if type(number) != int:
            raise Exception('You entered not a number.')
        else:
            if number % 2 == 0:
                return 'Entered number is even'
            else:
                return 'Entered number is odd'
    except Exception as error:
        return error


#######################################
def divide(numerator, denominator):
    try:
        if (type(numerator), type(denominator)) != (int, int):
            raise Exception('Value Error! You did not enter a number!')
        elif denominator == 0:
            raise Exception(f'Oops, {numerator}/{denominator}, division by zero is error!!!')
        else:
            return f'Result is {round(numerator/denominator, 2)}'
    except Exception as error:
        return error


############################################
class ToSmallNumberGroupError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

def check_number_group(number):
    def is_number(checked_number):
        try:
            int(checked_number)
            return False
        except ValueError:
            return True

    try:
        if is_number(number):
            raise ToSmallNumberGroupError('You entered incorrect data. Please try again.')
        else:
            if float(number) > 10:
                return f'Number of your group {number} is valid'
            else:
                return 'We obtain error:Number of your group can\'t be less than 10'

    except ToSmallNumberGroupError as error:
        return error



###############################
class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

def check_positive(number):
    try:
        number = float(number)
        if number > 0:
            return f'You input positive number: {number}'
        else:
            raise MyError(f'You input negative number: {number}. Try again.')
    except MyError as my_error:
        return my_error
    except:
        return f'Error type: ValueError!'


#######################################
def solve_quadric_equation(a, b, c):
    try:
        D = pow(float(b), 2) - 4 * float(a) * float(c)

        if a == 0:
            raise ZeroDivisionError('Zero Division Error')

        x1 = (-b + pow(D, 0.5)) / 2 * a
        x2 = (-b - pow(D, 0.5)) / 2 * a
        return f'The solution are x1=({int(x2)}-0j) and x2=({int(x1)}+0j)'
    except ZeroDivisionError as zero_error:
        return zero_error
    except TypeError:
        return 'Could not convert string to float'









