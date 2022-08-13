import colorama
from colorama import Fore, Style
cidade = input(Fore.GREEN+'Digite o nome da sua cidade: ')
cidade = cidade.title()
lista = cidade.split()
print (Fore.LIGHTCYAN_EX +f'A cidade de: {cidade.title()}, começa com santo no nome? ', end='')
print('Santo' in lista[0])