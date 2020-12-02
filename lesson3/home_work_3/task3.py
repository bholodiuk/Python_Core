number_one = int(input('Enter number_one:'))
number_two = int(input('Enter number_two:'))

print(f'Input values before replace -> number_one: {number_one}, number_two: {number_two}')

number_two, number_one = number_one, number_two

print(f'Input values after replace -> number_one: {number_one}, number_two: {number_two}')