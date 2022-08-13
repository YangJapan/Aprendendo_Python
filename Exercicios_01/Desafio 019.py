import colorama
from colorama import Fore, Style
import random
nome1 = input(Fore.LIGHTGREEN_EX+'Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
print(Fore.LIGHTMAGENTA_EX+'O aluno escolhido foi: {random.choice(lista)}')