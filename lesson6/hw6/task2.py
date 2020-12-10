"""
Write a script that checks the login that the user enters.
If the login is "First", then greet the users. If the login is different, send an error message.
(need to use loop while)
"""

def user_authentication():
    user_login_correct = 'First'
    detect_correct_answer = True

    while detect_correct_answer:
        user_login = input('Enter user login: ')

        if user_login == user_login_correct:
            print(f'Authentication is success, welcome user: {user_login}')
            break
        else:
            print(f'User login -> {user_login} is incorrect')


if __name__ == '__main__':
    user_authentication()