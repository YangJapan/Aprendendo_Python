import colorama
from colorama import Fore, Style
km = float(input(Fore.LIGHTCYAN_EX+'Digite quantos KM voce andou de carro: '))
dias = int(input('Digite quantos dias voce alugou o carro:'))
print(Fore.LIGHTBLUE_EX +f'O preço total foi de: {(dias*60)+(km*0.15)}')