"""
Unfinished Loop - Bug Fixing #1
Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!
"""

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res

if __name__ == '__main__':
    print(create_array(1), [1])
    print(create_array(2), [1, 2])
    print(create_array(3), [1, 2, 3])
    print(create_array(4), [1, 2, 3, 4])
    print(create_array(5), [1, 2, 3, 4, 5])