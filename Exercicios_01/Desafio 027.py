import colorama
from colorama import Fore, Style

nome = str(input(Fore.LIGHTBLACK_EX+'Digite seu nome completo: ')).strip()
lista = nome.split()
print(Fore.LIGHTRED_EX +f'Seu primeiro nome é: {lista[0]}')
print(f'O seu ultimo nome é: {lista[-1]}')