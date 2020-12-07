"""
Create a list that contains elements of integer type, then use the
loop to change the type of these elements to a floating type.
(Hint: use the built-in float () function).
"""

def int_to_float_convertor(value: list):
    try:
        if value:
            return [float(digit) for digit in value]
        else:
            return 'Empty list was inputted'
    except BaseException as base_exeption:
        return f'Some wrong happened {base_exeption}'

if __name__ == '__main__':
    # value_list0 = [] # for test
    value_list1 = [1, 2, 3, 4, 234, 542, 12]
    # value_list2 = ['s', 2, (1, 2)] # for test

    # print(int_to_float_convertor(value=value_list0))
    print(int_to_float_convertor(value=value_list1))
    # print(int_to_float_convertor(value=value_list2))