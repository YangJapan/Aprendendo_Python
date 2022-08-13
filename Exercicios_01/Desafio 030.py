
from colorama import Fore, Style
numero = int(input(Fore.CYAN+'Digite um numero para saber se e par ou não: '))

if numero % 2 == 0:
    print(Fore.MAGENTA+'O numero é par.')
else:
    print(Fore.LIGHTYELLOW_EX+'O numero é impar.')