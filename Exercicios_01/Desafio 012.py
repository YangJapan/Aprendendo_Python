import colorama
from colorama import Fore, Style
PreçoOriginal = float(input(Fore.GREEN+'Digite o preço para saber os 5% de desconto: R$'))
desconto = (PreçoOriginal * 5 /100)
print(Fore.CYAN+ f'O valor descontado foi de: {(PreçoOriginal - desconto):.2f} , O valor do desconto foi de: {desconto:.2f}')
