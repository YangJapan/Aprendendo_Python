import colorama
from colorama import Fore, Style
nome = input(Fore.LIGHTBLUE_EX+'Digite o seu nome para saber se tem silva: ')
nome = nome.title()
print(Fore.LIGHTWHITE_EX +f'Tem silva no nome? ')
print('Silva' in nome)