from colorama import Fore, Style
n1 = int(input(Fore.LIGHTRED_EX+'Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o ultimo numero: '))

if n1 > n2 and n1 > n3:
    print(Fore.LIGHTGREEN_EX+f'O maior é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior é {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor é {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor é {n3}')