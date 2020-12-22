"""
Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2 і цей скрипт
використати в іншому модулі, в якому ми запитуємо користувача площу якої фігури він хоче обчислити.

(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі, модуль1,
який містить три функції для знаходження площ, модуль2, в якому імпортований модуль1 і
виконується основна логіка програми).
"""
from area_module import *

if __name__ == '__main__':
    while True:
        choice_string = input('Make your choice: Square(triangle, rectangle, circle), or exit to stop: ')

        if choice_string == 'triangle':
            # Formula -> ½ × b × h
            base_side = int(input('    Enter base side of triangle: '))
            high = int(input('    Enter high of triangle: '))
            print(f'    square -> {triangle_square(base_side, high)}')
            break
        elif choice_string == 'rectangle':
            # Formula -> Area = w × h
            side_one = int(input('    Enter first side of rectangle: '))
            side_two = int(input('    Enter second of rectangle: '))
            print(f'    square -> {rectangle_square(side_one, side_two)}')
            break
        elif choice_string == 'circle':
            # Formula -> Area = π × r2
            radius = int(input('    Enter radius of circle: '))
            print(f'    square -> {circle_square(radius)}')
            break
        else:
            if choice_string.lower() == 'exit':
                print(f'Program was stopped by typing -> {choice_string}.')
                break
            else:
                print(f'Entered choice {choice_string} is wrong!!! Make your choice again!!!.')

