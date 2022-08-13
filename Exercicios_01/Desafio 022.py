import colorama
from colorama import Fore, Style
nome = input(Fore.WHITE+'Digite seu nome completo: ').strip()
print(Fore.CYAN +f'O nome todo em maiusculo: {nome.upper()}')
print(f'O nome todo em minusculo: {nome.lower()}')
lista = nome.split()
semEspaco = nome.replace(' ', '')
print(Fore.MAGENTA +f'O nome tem: {len(semEspaco)}, letras sem contar o espaço')
print(f'O primeiro nome tem: {len(lista[0])}, letras')
