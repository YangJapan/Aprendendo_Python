import colorama
from colorama import Fore, Style
import random
n1 = input(Fore.YELLOW+'Digite um nome: ')
n2 = input('Digite outro nome: ')
n3 = input('Digite mais um nome: ')
n4 = input('Digite um ultimo nome: ')
'''

Jeito numero 1: 

pessoas = [n1, n2, n3, n4]
lista = random.shuffle(pessoas)
print(Fore.YELLOW +f'A lista: {pessoas}')

'''
'''

Jeito numero 2: 

lista = random.sample([n1, n2, n3, n4], k=4)
print(Fore.YELLOW + f'A lista: {lista}')

'''