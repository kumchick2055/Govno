from math import sqrt

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

d = b**2 - 4*a*c
if d < 0:
    print('Корней нет')
if d == 0:
    print(f'X = {(-b+sqrt(d))/(2*a)}')
if d > 0:
    print(f'X1 = {(-b+sqrt(d))/(2*a)}')
    print(f'X2 = {(-b-sqrt(d))/(2*a)}')
