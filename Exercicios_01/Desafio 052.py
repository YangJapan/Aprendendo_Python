from colorama import Fore, Style
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print(Fore.GREEN, end='')
        tot += 1
    else:
        print(Fore.WHITE, end='')
    print(f'{c}', end=' ')
print(Style.RESET_ALL, f'\nO numero {num} foi divisível {tot} vezes!')
if tot == 2:
    print(f'O numero {num} é um numero primo!')
else:
    print(f'O numero {num} não é um numero primo!')
