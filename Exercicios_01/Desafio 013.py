import colorama
from colorama import Fore, Style
salario = float(input(Fore.GREEN+'Digite seu salario: '))
aumento = (salario * 15 / 100) + salario
print(Fore.MAGENTA+ f'Seu salario era de {salario:.2f} é passou a ser de {aumento:.2f}!')
