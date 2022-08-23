'''
from math import factorial
num = int(input('Digite um numero: '))
f = factorial(num)
print(f'O fatorial de {num} é {f}')
'''
num = int(input('Digite um numero: '))
c = num
f = 1
while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f = f * c
    c -= 1
print(f'{f}')
