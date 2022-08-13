import colorama
from colorama import Fore, Style

palavra = str(input(Fore.BLUE+'Digite uma frase: ')).strip().upper()
print(Fore.BLACK +f'Sua palavra tem {palavra.count("A")}')
print(f'A primeira letra A aparece na casa de numero: {palavra.find("A") + 1}')
print(f'A ultima letra A aparece na casa de numero: {palavra.rfind("A") + 1}')
print(f'A frase escrita foi: {palavra.title()}')
